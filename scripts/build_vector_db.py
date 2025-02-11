import os
import json
import yaml
import argparse
import logging
import time
from typing import Dict
from dotenv import load_dotenv
from tqdm import tqdm

from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import WebBaseLoader, GitLoader

def get_loader_for_package(pkg_info: Dict):
    """
    Get appropriate document loader based on package info
    
    Priorities:
    1. doc_url (official documentation)
    2. git_url (GitHub repository)
    """
    if 'doc_url' in pkg_info:
        loader = WebBaseLoader(pkg_info['doc_url'])
        return loader
        
    if 'git_url' in pkg_info:
        repo_path = os.path.join(config['pkg_repo_dir'], pkg_info['name'])
        return GitLoader(
            clone_url=pkg_info['git_url'],
            repo_path=repo_path,
            branch=pkg_info['git_branch'],
            file_filter=lambda x: x.endswith((".md", ".rst"))
        )
        
    raise ValueError(f"No valid documentation source for {pkg_info['name']}")

def main(config: Dict):
    """Build vector database from package documentation"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(config['vec_db_dir'], 'build.log'), mode='w'),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)
    
    # Load package info
    if not os.path.exists(config['pkg_info_path']):
        raise FileNotFoundError(f"Package info file not found at {config['pkg_info_path']}")
        
    with open(config['pkg_info_path'], 'r') as f:
        pkg_info = json.load(f)
    
    # Setup document splitting
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""],
        is_separator_regex=False
    )
    
    # Initialize lists to accumulate all documents
    all_texts = []
    all_metadatas = []
    
    total_packages = len(pkg_info)
    logger.info(f"Starting to process {total_packages} packages")
    
    for idx, pkg in enumerate(pkg_info, 1):
        try:
            logger.info(f"[{idx}/{total_packages}] Processing {pkg['name']}...")
            
            # Load and split documents
            loader = get_loader_for_package(pkg)
            docs = loader.load()
            split_docs = text_splitter.split_documents(docs)
            
            # Process each document chunk
            for doc in split_docs:
                # Enhance metadata with package info
                metadata = doc.metadata.copy()  # Preserve existing metadata from loader
                metadata.update({
                    'package_name': pkg['name'],
                    'source_type': 'documentation' if 'doc_url' in pkg else 'github',
                    'url': pkg.get('doc_url', pkg.get('git_url', 'unknown')),
                    'timestamp': time.strftime('%Y-%m-%d'),  # When the doc was processed
                    'chunk_id': f"{pkg['name']}_{len(all_texts)}"  # Unique identifier for each chunk
                })
                
                all_texts.append(doc.page_content)
                all_metadatas.append(metadata)
            
            logger.info(f"Successfully processed {pkg['name']}: {len(split_docs)} chunks created")
            
        except Exception as e:
            logger.error(f"Error processing {pkg['name']}: {e}")
            continue

    if all_texts:
        logger.info(f"Total documents to process: {len(all_texts)}")
        
        # Create embeddings for all texts
        text_embeddings = list(zip(
            all_texts,
            embeddings.embed_documents(all_texts)
        ))
        
        # Create single vector store with all documents
        vector_db = FAISS.from_embeddings(
            text_embeddings,
            embeddings,
            metadatas=all_metadatas
        )
        
        logger.info(f"Saving vector database to {config['vec_db_dir']}")
        vector_db.save_local(config['vec_db_dir'])
        logger.info("Vector database built successfully")
    else:
        logger.warning("No documents processed, vector database not created")

if __name__ == "__main__":
    load_dotenv()
    
    parser = argparse.ArgumentParser(description='Build vector database from package documentation')
    parser.add_argument('--config', default='./etc/vec-db.yaml', type=str, help='Path to config file')
    parser.add_argument('--query', '-q', type=str, help='query to test vector db') # if specified, will not build db
    
    args = parser.parse_args()

    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    # Create embeddings instance
    embeddings = OpenAIEmbeddings(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
        model=config['embedding_model'],
    )

    # setup directory
    os.makedirs(config['vec_db_dir'], exist_ok=True)
    os.makedirs(config['pkg_repo_dir'], exist_ok=True)

    if args.query:
        vector_db = FAISS.load_local(config['vec_db_dir'], embeddings, allow_dangerous_deserialization=True)
        docs = vector_db.similarity_search_with_relevance_scores(args.query, k=3)
        for doc, score in docs:
            print(f"Page Content:\n{doc.page_content}\nMetadata: {doc.metadata}\nRelevance Score: {score}")
    else:
        # Build database
        main(config) 
