from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from chatbot.llm import chatbot_logic

# Inicializa o grafo de estados
class State(TypedDict):
    messages: Annotated[list, add_messages]  # Definição do tipo de estado

graph_builder = StateGraph(State)

# Adiciona o nó chatbot ao grafo
graph_builder.add_node("chatbot", chatbot_logic)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# Compila o grafo
graph = graph_builder.compile()

# Função para processar atualizações no grafo
def stream_graph_updates(user_input: str):
    responses = []
    for event in graph.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            responses.append(value["messages"][-1].content)
    return responses
