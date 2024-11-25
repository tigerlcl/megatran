import os
import json
from typing import Optional

from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


class LazyRAG:
    """
    LazyRAG handles package imports and API documentation retrieval:
    1. Logs import errors for further integration
    2. Retrieves relevant function documentation for code generation
    """

    def __init__(self, ctx):
        self.oai_embedding = OpenAI(api_key=ctx.openai_api_key, base_url=ctx.openai_base_url)
        self.lc_embedding = OpenAIEmbeddings(api_key=ctx.openai_api_key, base_url=ctx.openai_base_url, model=ctx.embedding_model)
        self.embedding_model = ctx.embedding_model
        self.analyzer = ctx.result_analyzer
        self.logger = ctx.logger
        
        # regexes
        self.import_stmt_patterns = [
            r'import\s+([\w\s,]+)',  # matches: import numpy, pandas
            r'from\s+([\w.]+)\s+import'  # matches: from numpy import array
        ]

        # load vector database
        if not os.path.exists(ctx.vec_db_dir):
            raise FileNotFoundError("Local vector database not found. Please run build_vector_db.py first.")
        else:
            self.vector_db = FAISS.load_local(ctx.vec_db_dir, self.lc_embedding, allow_dangerous_deserialization=True)

        # load package info list (includes the code libs that are supported for RAG)
        if not os.path.exists(ctx.pkg_info_path):
            raise FileNotFoundError("Package info list not found. Please configure it first.")
        else:
            with open(ctx.pkg_info_path, 'r') as f:
                pkg_list = json.load(f)
                self.pkg_info = [pkg['name'] for pkg in pkg_list]
        

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
        
        
    def get_rag_prompt(self, code_snippet: str, top_k: int = 3) -> Optional[str]:
        """Build rag prompt Retrieve package documentation based on code snippet"""

        if not code_snippet or not self._check_import_pkg(code_snippet):
            self.logger.warning("No import statement found or unsupported package")
            return None
        
        self.logger.info(f"Retrieving package info...")
        try:
            # Calculate embedding once
            response = self.oai_embedding.embeddings.create(
                model=self.embedding_model,
                input=code_snippet
            )
            embedding = response.data[0].embedding
            
            # Keep existing logging
            self.logger.info(f"Embedding token usage: {response.usage.prompt_tokens}")
            
            # Add token tracking (for embeddings, we count it as prompt tokens)
            self.analyzer.add_token_usage("lazy_rag", response.usage.prompt_tokens, 0)
            
            # Use the pre-computed embedding
            docs = self.vector_db.similarity_search_by_vector(embedding, k=top_k)
            
            # Clean and remove consecutive newlines and spaces from each doc
            cleaned_docs = [
                ' '.join(' '.join(line.split()) for line in doc.page_content.splitlines() if line.strip())
                for doc in docs
            ]
            rag_doc = "\n".join(cleaned_docs)
        except Exception as e:
            self.logger.error(f"Error retrieving documentation: {e}")
            return None

        prompt = f"\n\n### Relevant Documentation ###\n{rag_doc}\n\nYou can use the above documentation to improve your code."

            
        return prompt
