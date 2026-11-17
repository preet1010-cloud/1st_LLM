import os
import streamlit as st
from openai import OpenAI

# Read backend URL and model from environment variables
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "qwen2.5:1.5b")

st.set_page_config(page_title="Local LLM Chat", page_icon="🤖")
st.title("Local LLM Chat-Bot")
st.write("using Ollama")

# Initialize OpenAI-compatible client pointing to Ollama
client = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")

# Sidebar controls (matching the video's generation settings)
with st.sidebar:
    st.header("Model Settings")
    st.info(f"**Active Model:** `{MODEL_NAME}`")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    top_p = st.slider("Top P", 0.1, 1.0, 0.9, 0.05)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user prompt
if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Stream response from Ollama's OpenAI-compatible endpoint
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            temperature=temperature,
            top_p=top_p,
            stream=True,
        )
        response = st.write_stream(stream)

    st.session_state.messages.append({"role": "assistant", "content": response})