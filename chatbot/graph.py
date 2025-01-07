from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from chatbot.llm import chatbot_logic

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot_logic)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

def stream_graph_updates(user_input: str):
    responses = []
    for event in graph.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            responses.append(value["messages"][-1].content)
    return responses
