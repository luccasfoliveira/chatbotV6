import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_EMBEDDINGS = os.getenv("MODEL_EMBEDDINGS")
