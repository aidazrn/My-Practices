import streamlit as st

prompt = st.chat_input("say something")
if prompt:
    st.write(f"user has sent the following prompt: {prompt}")