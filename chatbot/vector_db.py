import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from config.config import MODEL_EMBEDDINGS

# Inicializa o modelo de embeddings
model = SentenceTransformer(MODEL_EMBEDDINGS)  # Use seu modelo de embeddings aqui
dim = 384  # Atualizado para o tamanho correto do vetor de embeddings (384)
index = faiss.IndexFlatL2(dim)

# Função para adicionar dados na base de dados vetorial
def add_to_vector_db(text: str):
    # Gera o embedding do texto
    embedding = model.encode([text])  
    embedding = np.array(embedding).astype("float32")

    # Verifica se o vetor tem o tamanho correto
    if embedding.shape[1] != dim:
        raise ValueError(f"O vetor de embedding tem o tamanho {embedding.shape[1]}, mas o esperado é {dim}.")

    # Garantir que o vetor de embedding tenha formato 2D
    embedding = embedding.reshape(1, -1)  # Transforma o vetor 1D em uma matriz 2D (1, 384)

    # Adiciona o vetor ao índice FAISS
    index.add(embedding)
    
    # Verificação do número de vetores no índice
    print(f"Total de vetores no índice FAISS: {index.ntotal}")
