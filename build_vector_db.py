import os
import json
import yaml
import argparse
from typing import Dict
import shutil

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
    # TODO: optimize the WebBaseLoader logic
    if 'doc_url' in pkg_info:
        return WebBaseLoader(pkg_info['doc_url'])
        
    if 'git_url' in pkg_info:
        repo_path = os.path.join(config['pkg_repo_dir'], pkg_info['name'])
        return GitLoader(
            clone_url=pkg_info['git_url'],
            repo_path=repo_path,
            branch=pkg_info['git_branch']
        )
        
    raise ValueError(f"No valid documentation source for {pkg_info['name']}")

def main(config: Dict):
    """Build vector database from package documentation"""
    
    # Load package info
    with open(config['pkg_info_path'], 'r') as f:
        pkg_info = json.load(f)
    
    # Setup document splitting
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    
    # Process each package
    documents = []
    for pkg in pkg_info:
        try:
            print(f"Processing documentation for {pkg['name']}...")
            # Get appropriate loader
            loader = get_loader_for_package(pkg)
            docs = loader.load()
            split_docs = text_splitter.split_documents(docs)
            documents.extend(split_docs)
        except Exception as e:
            print(f"Error processing {pkg['name']}: {e}")
            continue
    if documents:
        # Create and save vector database
        vector_db = FAISS.from_documents(documents, embeddings)
        vector_db.save_local(config['vec_db_dir'])
        print("Vector database built successfully")
    else:
        print("No documents processed, vector database not created")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build vector database from package documentation')
    parser.add_argument('--config', default='./etc/config_template.yaml', type=str, help='Path to config file')
    parser.add_argument('--query', '-q', type=str, help='query to test vector db') # if specified, will not build db
    
    args = parser.parse_args()

    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    # Create embeddings instance
    embeddings = OpenAIEmbeddings(**config['openai_cfg'], model=config['embedding_model'])

    # setup directory
    os.makedirs(config['vec_db_dir'], exist_ok=True)
    os.makedirs(config['pkg_repo_dir'], exist_ok=True)

    if args.query:
        vector_db = FAISS.load_local(config['vec_db_dir'], embeddings, allow_dangerous_deserialization=True)
        docs = vector_db.similarity_search_with_relevance_scores(args.query, k=3)
        for doc, score in docs:
            print(f"Page Content:\n{doc.page_content}\nRelevance Score: {score}")

    else:
        # Build database
        main(config) 
