import os
import json
from typing import Optional

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


class LazyRAG:
    """
    LazyRAG handles package imports and API documentation retrieval:
    1. Logs import errors for further integration
    2. Retrieves relevant function documentation for code generation
    """
    def __init__(self, ctx):
        self.logger = ctx.logger
        self.embeddings = OpenAIEmbeddings(**ctx.openai_cfg, model=ctx.embedding_model)
        self.db_path = ctx.vec_db_dir
        self.pkg_info_path = ctx.pkg_info_path
        self.missing_pkg_path = os.path.join(ctx.code_dir, "missing_packages.txt")

        if not os.path.exists(self.db_path):
            self.logger.warning("Local vector database not found. Please run build_vector_db.py first.")
            raise FileNotFoundError("Local vector database not found. Please run build_vector_db.py first.")
        else:
            self.vector_db = FAISS.load_local(self.db_path, self.embeddings, allow_dangerous_deserialization=True)
        
        # Load package info
        with open(self.pkg_info_path, 'r') as f:
            self.pkg_info = json.load(f)
            self.pkg_names = [pkg['name'].lower() for pkg in self.pkg_info]
    
    def handle_import_error(self, error: ImportError):
        """Log missing packages into text file"""
        missing_module = str(error).split("No module named '")[-1].strip("'")
        
        with open(self.missing_pkg_path, 'a') as f:
            f.write(missing_module + "\n")

        self.logger.warning(f"Missing package '{missing_module}' logged. Please install it manually.")

    def find_pkg_info(self, code_snippet: str, top_k: int = 3) -> Optional[str]:
        """Find package documentation based on code snippet"""
        if not code_snippet:
            return None
        
        try:
            docs = self.vector_db.similarity_search(code_snippet, k=top_k)
            # Clean and remove consecutive newlines and spaces from each doc
            cleaned_docs = [
                ' '.join(' '.join(line.split()) for line in doc.page_content.splitlines() if line.strip())
                for doc in docs
            ]
            return "\n".join(cleaned_docs)
        except Exception as e:
            self.logger.error(f"Error retrieving documentation: {e}")
            return None
        
