
import streamlit as st
import google.generativeai as genai

# Hard-code your Gemini API key **only if you're comfortable and understand the risk**
GEMINI_API_KEY = "AIzaSyAI4iwgMJa-XaHrjGLnwsQtfwLC0tcoZ3Y"

st.title("Gemini Chatbot")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

if "model" not in st.session_state:
    st.session_state.model = "gemini-2.0-flash"  # or gemini-1.5-pro
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# User input
if prompt := st.chat_input("Ask me something"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call Gemini
    model = genai.GenerativeModel(st.session_state.model)
    chat = model.start_chat(history=[
        {"role": msg["role"], "parts": [msg["content"]]} for msg in st.session_state.messages
    ])
    response = chat.send_message(prompt)

    reply = response.text
    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
