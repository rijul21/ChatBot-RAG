import streamlit as st
from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("HF_TOKEN")

st.title("🧠 Hugging Face Inference Bot")

user_input = st.text_input("Ask anything:")
if user_input:
    generator = pipeline("text-generation", model="gpt2", use_auth_token=token)
    output = generator(user_input, max_length=50)
    st.write("Response:", output[0]["generated_text"])
