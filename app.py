import streamlit as st
from chatbot.graph import stream_graph_updates
from utils.validation import is_valid_input
from chatbot.vector_db import add_to_vector_db 

if 'responses' not in st.session_state:
    st.session_state.responses = []

# Título da aplicação
st.title("Chatbot da Wa Project.")

# Caixa de entrada de texto
user_input = st.text_input("Você:", key="input_text", placeholder="Digite sua mensagem aqui...")

if st.button("Enviar") and user_input:
    if user_input.lower() in ["quit", "exit", "sair"]:
        st.write("Tchau")
    else:
        if is_valid_input(user_input):
            # Adiciona o input válido ao banco de dados vetorial (FAISS)
            add_to_vector_db(user_input)
        else:
            st.write("Essa informação não é válida para nós.")
        
        # Processa a interação com o chatbot
        responses = stream_graph_updates(user_input)
        st.session_state.responses.extend(responses)  # Armazena as respostas
        for response in responses:
            st.write("Assistente:", response)
