import streamlit as st
import pandas as pd

from components.certificate_upload import certificate_uploader
from components.chatbot import render_chat
from components.profile_card import render_profile_card


def _render_academic_performance(student: dict):
    st.header("Academic Performance")

    sgpa = student.get("sgpa", {})
    df = pd.DataFrame(
        {"Semester": list(sgpa.keys()), "SGPA": list(sgpa.values())}
    )
    st.table(df)

    st.write("**Overall CGPA:**", student.get("cgpa", "-"))
    st.line_chart(df.set_index("Semester"))


def _render_skills(student: dict):
    st.header("Skills")
    skills = student.get("skills", [])
    cols = st.columns(4)
    for i, skill in enumerate(skills):
        with cols[i % 4]:
            st.success(skill)


def _render_achievements(student: dict):
    st.header("Achievements")
    certs = student.get("uploaded_certificates", {})
    for category in ["sports", "hackathons", "cultural"]:
        items = certs.get(category, [])
        if not items:
            continue
        st.subheader(category.capitalize())
        for item in items:
            st.write(f"- {item.get('event', 'Untitled')} ({item.get('year', '')})")


def _render_internships(student: dict):
    st.header("Internships")
    internships = student.get("internships", [])
    if not internships:
        st.info("No internships added yet.")
        return
    for i, internship in enumerate(internships, start=1):
        st.write(f"**{i}. {internship.get('role', 'Intern')}**")
        st.write(f"Company: {internship.get('company', 'Unknown')}")
        st.write(f"Duration: {internship.get('duration', '')}")
        st.write("---")


def show_student_dashboard(student: dict, page: str = "Dashboard"):
    if student is None:
        st.error("No student data available. Please login.")
        return

    if page == "Dashboard":
        st.title("Student Dashboard")
        render_profile_card(student)
        _render_academic_performance(student)
        _render_skills(student)

    elif page == "Academic Performance":
        _render_academic_performance(student)

    elif page == "Achievements":
        _render_achievements(student)

    elif page == "Certificates":
        certificate_uploader(student)

    elif page == "Skills":
        _render_skills(student)

    elif page == "Internships":
        _render_internships(student)

    elif page == "AI Assistant":
        render_chat("student", student)
