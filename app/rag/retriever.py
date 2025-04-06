# Function retrieval
from app.rag.embeddings import EmbeddingModel

embedding = EmbeddingModel()

def search_milvus(query, collection, limit=1):
    query_embedding = embedding.create_embedding(query)

    search_params = {
    "index_type": "HNSW",
    "metric_type": "L2",
    "params": {
        "M": 20,
        "efConstruction": 300
        }
    }

    results = collection.search(
        data = [query_embedding],
        anns_field = "Metadata",
        param = search_params,
        limit = limit,
        output_fields = ["Module", "Function_Name"]
    )

    data = {}
    module = []
    name = []
        
    for result in results[0]:
        name.append(result.entity.get("Function_Name"))
        module.append(result.entity.get("Module"))

    data["Module"] = module
    data["Function Name"] = name

    return data
