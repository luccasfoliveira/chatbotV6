FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV GROQ_API_KEY="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"
ENV MODEL_EMBEDDINGS="all-MiniLM-L6-v2"

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
