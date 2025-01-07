from langchain_groq import ChatGroq
import os

groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(api_key=groq_api_key, model="llama-3.1-70b-versatile", temperature=0.5)

# Função para gerar a resposta com o modelo Groq
def chatbot_logic(state: dict) -> dict:
    return {"messages": [llm.invoke(state["messages"])]}
