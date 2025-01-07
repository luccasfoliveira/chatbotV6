import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from config.config import MODEL_EMBEDDINGS

model = SentenceTransformer(MODEL_EMBEDDINGS) 
dim = 384 
index = faiss.IndexFlatL2(dim)

def add_to_vector_db(text: str):
    embedding = model.encode([text])  
    embedding = np.array(embedding).astype("float32")

    # Verifica se o vetor tem o tamanho correto
    if embedding.shape[1] != dim:
        raise ValueError(f"O vetor de embedding tem o tamanho {embedding.shape[1]}, mas o esperado é {dim}.")

    embedding = embedding.reshape(1, -1)

    # Adiciona o vetor ao índice FAISS
    index.add(embedding)
    
    # Verificação do número de vetores no índice
    print(f"Total de vetores no índice FAISS: {index.ntotal}")
