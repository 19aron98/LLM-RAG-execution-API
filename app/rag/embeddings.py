# Embedding creation

from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model="Alibaba-NLP/gte-large-en-v1.5"):
        """
        Initializes the embedding model.
        
        Args:
            model_name (str): The name of the Hugging Face Embedding model to use
        """
        self.embeddings = SentenceTransformer(model, trust_remote_code=True)
    
    def create_embedding(self, text):
        """
        Creates an embedding for the given text.
        
        Args:
            text (str): The text to create an embedding for
            
        Returns:
            numpy.ndarray: The embedding vector
        """
        return self.embeddings.encode(text)