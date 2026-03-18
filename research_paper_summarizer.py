from langchain.chat_models import init_chat_model
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.header("Research Paper Summarizer")

model = init_chat_model("google_genai:gemini-2.5-flash-lite")

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)