import streamlit as st

from utils import api


def student_login_form():
    st.subheader("Student Login")
    with st.form("student_login_form"):
        reg_no = st.text_input("KTU Registration Number", placeholder="SCT23AM001")
        password = st.text_input("Password", type="password", placeholder="student123")
        submitted = st.form_submit_button("Login")

    if submitted:
        with st.spinner("Verifying credentials…"):
            result = api.login_etlab(reg_no, password)

        if result.get("error"):
            st.error(result["error"])
            return None

        if result.get("status") == "ok":
            st.success("Login successful")
            return result.get("student")

        st.error("Invalid login")
    return None


def faculty_login_form():
    st.subheader("Faculty Login")
    with st.form("faculty_login_form"):
        username = st.text_input("Username", placeholder="faculty")
        password = st.text_input("Password", type="password", placeholder="faculty123")
        submitted = st.form_submit_button("Login")

    if submitted:
        with st.spinner("Verifying credentials…"):
            result = api.faculty_login(username, password)

        if result.get("error"):
            st.error(result["error"])
            return None

        if result.get("status") == "ok":
            st.success("Login successful")
            return {"username": username}

        st.error("Invalid login")
    return None
