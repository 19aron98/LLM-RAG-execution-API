# Creates Metadata

import inspect
import importlib
import sys
import os

project_root = r"C:\Users\Swapnil Singh\Desktop\LLM+RAG API\function_execution_api"
if project_root not in sys.path:
    sys.path.append(project_root)

def collect_function_metadata():
    folder_path = os.path.join(project_root, "app", "function_registry")
    all_metadata = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  # e.g. "application_functions"
            full_module_path = f"app.function_registry.{module_name}"
            
            module = importlib.import_module(full_module_path)
            
            for name, obj in inspect.getmembers(module, inspect.isfunction):
                docstring = inspect.getdoc(obj) or "No docstring"
                all_metadata.append({
                    "module": module_name,
                    "function_name": name,
                    "description": docstring
                })
    print(f"Created metadata of common automation functions")
    return all_metadata