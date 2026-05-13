import streamlit as st
import os
from groq import Groq

# Function to load keys/configs from files
def load_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read().strip()
    return None

# Load API Key and System Message
api_key = load_file("config/api_key.txt")
system_prompt = load_file("config/system_prompt.txt")

st.set_page_config(page_title="Mazzu AI - Assistant", layout="wide")
st.title("🤖 Mazzu AI - Dev Assistant")

if not api_key:
    st.error("API Key not found! Please add it to config/api_key.txt")
    st.stop()

client = Groq(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []
    if system_prompt:
        st.session_state.messages.append({"role": "system", "content": system_prompt})

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("How can I help you with your code today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=st.session_state.messages,
            stream=True,
        )
        response = st.write_stream(stream)
    
    st.session_state.messages.append({"role": "assistant", "content": response})