import streamlit as st
import pandas as pd

from components.achievement_comparison import render_achievement_comparison
from components.analytics_charts import (
    render_certificate_breakdown,
    render_cgpa_distribution,
    render_overview_cards,
    render_skills_popularity,
)
from components.chatbot import render_chat
from components.student_profile import render_student_profile
from utils.dataset_loader import load_students_dataset


def _search_students(students: list[dict], query: str) -> list[dict]:
    q = query.strip().lower()
    if not q:
        return students
    return [
        s
        for s in students
        if q in s.get("name", "").lower() or q in s.get("univ_reg_no", "").lower()
    ]


def show_faculty_dashboard(user: dict, page: str = "Dashboard", selected_student: dict | None = None):
    st.title("Faculty Dashboard")
    students = load_students_dataset()

    if page == "Dashboard":
        render_overview_cards(students)
        st.markdown("---")
        st.subheader("Student Records")
        df = pd.DataFrame(students)
        if not df.empty:
            df = df[["name", "univ_reg_no", "cgpa", "skills"]]
            st.dataframe(df)
        else:
            st.info("No student records are available.")

    elif page == "Student Search":
        st.subheader("Search Students")
        query = st.text_input("Search by name or KTU ID", key="faculty_search_query")

        # Reset selection when search changes
        if st.session_state.get("last_search_query") != query:
            st.session_state.last_search_query = query
            st.session_state.selected_student = None

        matching = _search_students(students, query)

        if not matching:
            st.info("No students match your search.")
            st.session_state.selected_student = None
        else:
            options = [f"{s.get('name')} ({s.get('univ_reg_no')})" for s in matching]
            selected = st.selectbox(
                "Select a student",
                options=options,
                key="faculty_student_select",
                index=0,
            )
            idx = options.index(selected)
            st.session_state.selected_student = matching[idx]
            render_student_profile(matching[idx])

    elif page == "Student Profile":
        st.subheader("Student Profile")
        if selected_student:
            render_student_profile(selected_student)
        else:
            st.info("Use Student Search to select a student.")

    elif page == "Achievement Comparison":
        st.subheader("Achievement Comparison")
        student_names = [f"{s.get('name')} ({s.get('univ_reg_no')})" for s in students]
        selected = st.multiselect(
            "Select students to compare",
            options=student_names,
            default=[],
        )
        selected_list = [
            s for s in students if f"{s.get('name')} ({s.get('univ_reg_no')})" in selected
        ]
        render_achievement_comparison(students, selected_list)

    elif page == "Academic Analytics":
        st.subheader("Academic Analytics")
        render_overview_cards(students)
        st.markdown("---")
        render_cgpa_distribution(students)
        render_skills_popularity(students)
        render_certificate_breakdown(students)

    elif page == "AI Assistant":
        render_chat("faculty", user)
