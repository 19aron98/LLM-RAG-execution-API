# FastAPI app entry point

from app.create_metadata import collect_function_metadata
from app.rag.vector_store import connect_to_milvus, ensure_collection_exists, ensure_database_exists, insert_metadata_into_collection
from app.rag.retriever import search_milvus
from app.code_gen.generator import generate_code
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create metadata of automatic functions
metadata = collect_function_metadata()

# Connection with Milvus database
connect_to_milvus()
ensure_database_exists("metadb")
collection = ensure_collection_exists("functions")
insert_metadata_into_collection(collection, metadata)


# Initialize FastAPI app
app = FastAPI()

class ExecuteRequest(BaseModel):
    prompt: str

@app.post("/execute")
def execute_function(request: ExecuteRequest):
    """API endpoint to retrieve function based on user prompt"""

    result = search_milvus(request.prompt, collection)

    if not result:
        raise HTTPException(status_code=404, detail="No matching function found")
    
    func_name, generated_code = generate_code(result)

    return {"function": func_name, "code": generated_code.content}