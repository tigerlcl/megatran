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
        
        # regexes
        self.import_stmt_patterns = [
            r'import\s+([\w\s,]+)',  # matches: import numpy, pandas
            r'from\s+([\w.]+)\s+import'  # matches: from numpy import array
        ]

        if not os.path.exists(ctx.vec_db_dir):
            self.logger.warning("Local vector database not found. Please run build_vector_db.py first.")
            raise FileNotFoundError("Local vector database not found. Please run build_vector_db.py first.")
        else:
            self.vector_db = FAISS.load_local(ctx.vec_db_dir, self.embeddings, allow_dangerous_deserialization=True)

        # load package info list
        try:
            with open(ctx.pkg_info_path, 'r') as f:
                pkg_list = json.load(f)
                self.pkg_info = [pkg['name'] for pkg in pkg_list]
        except FileNotFoundError:
            self.pkg_info = []
        

    def _check_import_pkg(self, code_snippet: str) -> bool:
        """
        Check if any missing package appears in import statements
        Simple string matching against missing packages
        """
        if not self.pkg_info:
            return False
            
        # Only proceed if this is an import statement
        if not ('import' in code_snippet or 'from' in code_snippet):
            return False
            
        # Check if RAG supported package appears in the statement
        return any(pkg in code_snippet for pkg in self.pkg_info)

    def find_pkg_info(self, code_snippet: str, top_k: int = 3) -> Optional[str]:
        """Retrieve package documentation based on code snippet"""
        if not code_snippet or not self._check_import_pkg(code_snippet):
            return None
        

        self.logger.info(f"Retrieving package info...")
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
        
