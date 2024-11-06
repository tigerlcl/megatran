from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, WebBaseLoader
import logging
import json
import os
from typing import List, Dict, Optional
import importlib
import pkg_resources
from pathlib import Path


class LazyRAG:
    """
    LazyRAG handles package imports and API documentation retrieval:
    1. Offline mode: Logs import errors and builds a vector DB of package documentation
    2. Online mode: Retrieves relevant function documentation for code generation
    """
    def __init__(self, ctx):
        self.logger = ctx.logger
        self.embeddings = OpenAIEmbeddings(**ctx.openai_cfg)
        self.vector_db = None
        self.db_path = os.path.join(ctx.code_dir, "package_docs")
        self.import_log_path = os.path.join(ctx.code_dir, "import_errors.json")
        self.mode = "online" if self._check_vectordb() else "offline"
        
        # Load or create import error log
        self.import_errors = self._load_import_errors()
    
    def _check_vectordb(self) -> bool:
        """Check if vector database exists"""
        return os.path.exists(self.db_path)
    
    def _load_import_errors(self) -> Dict:
        """Load or create import error log"""
        if os.path.exists(self.import_log_path):
            with open(self.import_log_path, 'r') as f:
                return json.load(f)
        return {"missing_packages": {}, "resolved_packages": []}

    def _save_import_errors(self):
        """Save import errors to JSON file"""
        with open(self.import_log_path, 'w') as f:
            json.dump(self.import_errors, f, indent=2)

    def handle_import_error(self, error: ImportError, chat_context: str) -> None:
        """
        Handle import errors in offline mode by logging them
        Args:
            error: The ImportError exception
            chat_context: The original chat message for context
        """
        missing_module = str(error).split("No module named '")[-1].strip("'")
        
        if missing_module not in self.import_errors["missing_packages"]:
            self.import_errors["missing_packages"][missing_module] = {
                "contexts": [chat_context],
                "error_msg": str(error)
            }
        elif chat_context not in self.import_errors["missing_packages"][missing_module]["contexts"]:
            self.import_errors["missing_packages"][missing_module]["contexts"].append(chat_context)
        
        self._save_import_errors()
        self.logger.warning(f"Missing package '{missing_module}' logged. Please install it manually.")

    async def build_vector_db(self):
        """
        Build vector database from package documentation in offline mode
        """
        documents = []
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        
        # Process each resolved package
        for package in self.import_errors.get("resolved_packages", []):
            try:
                # Get package documentation URL or local path
                pkg_info = pkg_resources.working_set.by_key[package]
                doc_url = self._get_package_doc_url(pkg_info)
                
                if doc_url.startswith('http'):
                    loader = WebBaseLoader(doc_url)
                else:
                    loader = TextLoader(doc_url)
                
                docs = loader.load()
                split_docs = text_splitter.split_documents(docs)
                documents.extend(split_docs)
                
            except Exception as e:
                self.logger.error(f"Error processing documentation for {package}: {e}")
        
        if documents:
            self.vector_db = FAISS.from_documents(documents, self.embeddings)
            self.vector_db.save_local(self.db_path)
            self.mode = "online"
            self.logger.info("Vector database built successfully")

    def retrieve_docs(self, query: str, k: int = 3) -> List[str]:
        """
        Retrieve relevant documentation in online mode
        Args:
            query: The search query
            k: Number of documents to retrieve
        Returns:
            List of relevant documentation strings
        """
        if self.mode != "online":
            self.logger.warning("RAG system is in offline mode, no documentation retrieval available")
            return []
            
        if not self.vector_db:
            self.vector_db = FAISS.load_local(self.db_path, self.embeddings)
            
        docs = self.vector_db.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]

    def _get_package_doc_url(self, pkg_info) -> str:
        """Helper method to get package documentation URL"""
        # Implementation depends on package metadata format
        # This is a simplified version
        metadata = pkg_info.get_metadata('PKG-INFO')
        for line in metadata.split('\n'):
            if line.startswith('Documentation: '):
                return line.split(': ')[1]
        return ""

    def get_function_context(self, chat: str) -> Optional[str]:
        """
        Get relevant function documentation based on chat
        Args:
            chat: The original chat message
        Returns:
            Documentation string if found, None otherwise
        """
        if self.mode == "online":
            docs = self.retrieve_docs(chat)
            if docs:
                return "\n".join(docs)
        return None 