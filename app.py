import streamlit as st
from agent import chat

st.set_page_config(
    page_title="TailorTalk Drive Agent",
    page_icon="🗂️",
    layout="centered"
)

st.title("🗂️ TailorTalk Drive Agent")
st.caption("Search your Google Drive files using natural language!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me to find files... e.g. 'Find all PDFs'"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching Drive..."):
            response = chat(prompt, st.session_state.messages)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})