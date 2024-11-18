import os
import json
import yaml
import argparse
from typing import Dict
import shutil

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader, GitLoader

def get_loader_for_package(pkg_info: Dict):
    """
    Get appropriate document loader based on package info
    
    Priorities:
    1. doc_url (official documentation)
    2. git_url (GitHub repository)
    3. pypi_url (PyPI page)
    """
    if 'doc_url' in pkg_info:
        return WebBaseLoader(pkg_info['doc_url'])
        
    if 'git_url' in pkg_info:
        repo_path = os.path.join(config['pkg_repo_dir'], pkg_info['name'])
        return GitLoader(
            clone_url=pkg_info['git_url'],
            repo_path=repo_path,
            branch="main"
        )
        
    if 'pypi_url' in pkg_info:
        return WebBaseLoader(pkg_info['pypi_url'])
        
    raise ValueError(f"No valid documentation source for {pkg_info['name']}")

def main(config: Dict):
    """Build vector database from package documentation"""
    # Create embeddings instance
    embeddings = OpenAIEmbeddings(**config['openai_cfg'], model=config['embedding_model'])
    
    # Load package info
    with open(config['pkg_info_path'], 'r') as f:
        pkg_info = json.load(f)
    
    # Setup document splitting
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    
    documents = []
    
    # Process each package
    for pkg in pkg_info:
        try:
            print(f"Processing documentation for {pkg['name']}...")
            
            # Get appropriate loader
            loader = get_loader_for_package(pkg)
            
            # Load and split documents
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
    
    args = parser.parse_args()

    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    # setup directory
    os.makedirs(config['vec_db_dir'], exist_ok=True)
    os.makedirs(config['pkg_repo_dir'], exist_ok=True)
    
    # Build database
    main(config) 
