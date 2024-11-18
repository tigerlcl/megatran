import os
import json
from typing import List, Optional

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
        self.embeddings = OpenAIEmbeddings(**ctx.openai_cfg)
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

    def find_pkg_info(self, import_stmts: List[str]) -> Optional[str]:
        """
        Find package information based on import statements
            
        Example:
            import_stmts = ['import utm', 'from mgrs import MGRS']
            docs = find_pkg_info(import_stmts)
        """
            
        # Process each import statement
        docs = []
        for stmt in import_stmts:
            # Handle 'import pkg' and 'from pkg import x'
            if stmt.startswith('from'):
                pkg = stmt.split()[1]
            else:
                pkg = stmt.split()[1].split('.')[0]
            
            # Filter out packages we have docs
            if pkg not in self.pkg_names:
                self.logger.warning(f"No documentation indexed in DB for package {pkg}")
                continue

            try:
                current_docs = self._retrieve_docs(stmt)
                docs.extend(current_docs)
            except Exception as e:
                self.logger.error(f"Error retrieving documentation: {e}")

        # remove duplicated docs if two statements import the same package
        docs = list(set(docs))

        return "\n".join(docs) if docs else None

    def _retrieve_docs(self, query: str, k: int = 3) -> List[str]:
        """Retrieve relevant documentation based on query"""
        docs = self.vector_db.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]
        
