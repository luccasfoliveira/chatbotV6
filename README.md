# chatbotV6


# Projeto Chatbot

Este projeto é um chatbot simples que pode ser executado localmente ou em um contêiner Docker. Abaixo estão as instruções sobre como rodar o projeto nas duas opções.

---

## Rodar no Docker

Para rodar o projeto utilizando Docker, siga os passos abaixo:

  - docker build -t chatbot . 
  - docker run -it --rm chatbot:latest

## Rodar Localmente

Para rodar o projeto localmente, siga os passos abaixo:

 - python -m venv venv
 - source venv/bin/activate
 - pip install -r requirements.txt
 - streamlit run app.py 

## Testes:

### Salva:
 - É verdade que o vôlei tem 6 jogadores em quadra.
 - Uma verdade, a terra não é plana.

 - Existe bola quadrada, isso é um fato interessante

### Não salva:
 - Existe bola quadrada!
