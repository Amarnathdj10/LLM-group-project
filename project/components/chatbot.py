import streamlit as st

from utils import api


def render_chat(role: str, user: dict):
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.subheader("AI Assistant")

    query = st.text_input("Ask a question", key="chat_input")
    if st.button("Send") and query:
        st.session_state.chat_history.append({"role": "user", "text": query})
        with st.spinner("Thinking…"):
            if role == "student":
                response = api.student_chat(user.get("univ_reg_no"), query)
            else:
                response = api.faculty_chat(query)

        answer = response.get("response") or response.get("error") or "No response received."
        st.session_state.chat_history.append({"role": "assistant", "text": answer})

    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['text']}")
        else:
            st.markdown(f"**AI:** {msg['text']}")
