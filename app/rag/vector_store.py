# Vector database implementation

from pymilvus import connections, db, utility, Collection, CollectionSchema, FieldSchema, DataType
from app.rag.embeddings import EmbeddingModel

def connect_to_milvus(host="localhost", port="19530"):
    """Connect to Milvus and return connection status."""
    connections.connect("default", host=host, port=port)
    if connections.has_connection("default"):
        print("✅ Connection to Milvus is successful!")
    else:
        raise ConnectionError("❌ Failed to connect to Milvus.")

def ensure_database_exists(db_name="metadb"):
    """Check if the database exists, if not create it."""
    if db_name not in db.list_database():
        db.create_database(db_name)
        print(f"✅ Database '{db_name}' created.")
    db.using_database(db_name=db_name)

def ensure_collection_exists(collection_name="functions"):
    """Check if the collection exists, if not create it."""
    if utility.has_collection(collection_name):
        print(f"✅ Collection '{collection_name}' already exists. Skipping creation.")
        return Collection(collection_name)  # Load existing collection
    
    print(f"🛠️ Creating collection '{collection_name}'...")
    schema = CollectionSchema(fields=[
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="Module", dtype=DataType.VARCHAR, max_length=255),
        FieldSchema(name="Function_Name", dtype=DataType.VARCHAR, max_length=255),
        FieldSchema(name="Metadata", dtype=DataType.FLOAT_VECTOR, dim=1024)
    ])
    collection = Collection(name=collection_name, schema=schema)
    
    # Create Index
    index_params = {
        "index_type": "HNSW",
        "metric_type": "L2",
        "params": {"M": 20, "efConstruction": 300}
    }
    collection.create_index(field_name="Metadata", index_params=index_params)
    print(f"✅ Collection '{collection_name}' created with index.")
    return collection

def insert_metadata_into_collection(collection, metadata):
    """Insert metadata into the collection if it's not already populated."""
    if collection.num_entities > 0:
        print("✅ Data already exists in the collection. Skipping insertion.")
        return

    embedding = EmbeddingModel()
    module = [data['module'] for data in metadata]
    function_name = [data['function_name'] for data in metadata]
    description = [embedding.create_embedding(data['description']) for data in metadata]

    collection.insert(data=[module, function_name, description])
    collection.load()
    print("✅ Metadata inserted and collection loaded.")