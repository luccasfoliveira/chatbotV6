from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY, MODEL_LLM

llm = ChatGroq(api_key=GROQ_API_KEY, model=MODEL_LLM, temperature=0.5)

def chatbot_logic(state: dict) -> dict:
    return {"messages": [llm.invoke(state["messages"])]}
