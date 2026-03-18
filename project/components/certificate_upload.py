import streamlit as st
from datetime import datetime

from utils import api


def certificate_uploader(user: dict):
    st.subheader("Upload Certificates")

    category = st.selectbox(
        "Category",
        ["sports", "cultural", "hackathons", "workshops", "internships"],
        format_func=lambda x: x.capitalize(),
    )
    title = st.text_input("Certificate Title")
    file = st.file_uploader("Upload file (PDF/PNG/JPG)", type=["pdf", "png", "jpg", "jpeg"])

    if st.button("Upload"):
        if not title or not file:
            st.error("Please provide a title and upload a file.")
            return

        # In a real app, you'd send file bytes to the backend. Here we just notify.
        ts = datetime.utcnow().isoformat()
        result = api.upload_certificate(user.get("univ_reg_no"), category, title, ts)

        if result.get("error"):
            st.error(result["error"])
        else:
            st.success("Certificate uploaded successfully (simulated)")

    st.markdown("---")
    st.write("#### Your certificates")
    certs = user.get("uploaded_certificates", {})
    for cat, items in certs.items():
        if not items:
            continue
        st.write(f"**{cat.capitalize()}**")
        for item in items:
            st.write(f"- {item.get('event', item.get('title', 'Untitled'))}")
