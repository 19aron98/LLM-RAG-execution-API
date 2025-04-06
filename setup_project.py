import os

def create_file(file_path, content=""):
    with open(file_path, "w") as f:
        f.write(content)

def setup_project():
    base_dir = r"C:\\Users\\Swapnil Singh\\Desktop\\LLM+RAG API\\function_execution_api"
    sub_dirs = [
        "app",
        "app/function_registry",
        "app/rag",
        "app/code_gen",
        "app/session"
    ]
    
    files = {
        "app/__init__.py": "",
        "app/main.py": "# FastAPI app entry point\n",
        "app/function_registry/__init__.py": "",
        "app/function_registry/system_functions.py": "# System-related functions\n",
        "app/function_registry/application_functions.py": "# Application control functions\n",
        "app/function_registry/utility_functions.py": "# Utility functions\n",
        "app/rag/__init__.py": "",
        "app/rag/vector_store.py": "# Vector database implementation\n",
        "app/rag/embeddings.py": "# Embedding creation\n",
        "app/rag/retriever.py": "# Function retrieval\n",
        "app/code_gen/__init__.py": "",
        "app/code_gen/generator.py": "# Code generation logic\n",
        "app/session/__init__.py": "",
        "app/session/memory.py": "# Session-based memory\n",
        "requirements.txt": "# List dependencies here\n",
        "README.md": "# Project documentation\n",
        "notebook.ipynb": "{}"  # Empty Jupyter Notebook file
    }
    
    # Create directories
    for sub_dir in sub_dirs:
        os.makedirs(os.path.join(base_dir, sub_dir), exist_ok=True)
    
    # Create files
    for file_path, content in files.items():
        create_file(os.path.join(base_dir, file_path), content)
    
    print("Project structure created successfully at", base_dir)
    
if __name__ == "__main__":
    setup_project()