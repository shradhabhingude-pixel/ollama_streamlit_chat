import streamlit as st
from ollama import chat

st.title("Chat with Gemma")

prompt = st.chat_input("Type a message")

if prompt:
    st.write("You:", prompt)

    response = chat(
        model="gemma3:1b",
        messages=[{"role": "user", "content": prompt}],
    )

    answer = response["message"]["content"]
    st.write("Gemma:", answer)