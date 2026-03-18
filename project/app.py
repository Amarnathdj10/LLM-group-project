import streamlit as st

from components.login import faculty_login_form, student_login_form
from components.sidebar import render_sidebar
from pages.faculty_dashboard import show_faculty_dashboard
from pages.student_dashboard import show_student_dashboard

st.set_page_config(page_title="Academic AI Portal", layout="wide", page_icon="🎓")

if "role" not in st.session_state:
    st.session_state.role = None
    st.session_state.user = None
    st.session_state.page = "landing"
    st.session_state.subpage = "Dashboard"


def set_role(role: str):
    st.session_state.role = role
    st.session_state.page = "login"
    st.session_state.subpage = "Dashboard"


def logout():
    st.session_state.role = None
    st.session_state.user = None
    st.session_state.page = "landing"
    st.session_state.subpage = "Dashboard"
    st.session_state.selected_student = None
    st.session_state.last_search_query = None


def landing_page():
    st.title("Academic AI Portal")
    st.write("A modern student/faculty ERP portal with AI assistance.")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🎓 Student Login", use_container_width=True):
            set_role("student")

    with col2:
        if st.button("👨‍🏫 Faculty Login", use_container_width=True):
            set_role("faculty")


def login_page():
    st.header("Login")

    if st.session_state.role == "student":
        student = student_login_form()
        if student:
            st.session_state.user = student
            st.session_state.page = "dashboard"

    elif st.session_state.role == "faculty":
        faculty = faculty_login_form()
        if faculty:
            st.session_state.user = faculty
            st.session_state.page = "dashboard"
            st.session_state.selected_student = None


def dashboard_page():
    if st.session_state.role == "student":
        render_sidebar(
            [
                "Dashboard",
                "Academic Performance",
                "Achievements",
                "Certificates",
                "Skills",
                "Internships",
                "AI Assistant",
                "Logout",
            ],
            selected=st.session_state.subpage,
            on_logout=logout,
        )

        if st.session_state.subpage == "Dashboard":
            show_student_dashboard(st.session_state.user)

        elif st.session_state.subpage == "Academic Performance":
            show_student_dashboard(st.session_state.user, page="Academic Performance")

        elif st.session_state.subpage == "Achievements":
            show_student_dashboard(st.session_state.user, page="Achievements")

        elif st.session_state.subpage == "Certificates":
            show_student_dashboard(st.session_state.user, page="Certificates")

        elif st.session_state.subpage == "Skills":
            show_student_dashboard(st.session_state.user, page="Skills")

        elif st.session_state.subpage == "Internships":
            show_student_dashboard(st.session_state.user, page="Internships")

        elif st.session_state.subpage == "AI Assistant":
            show_student_dashboard(st.session_state.user, page="AI Assistant")

        elif st.session_state.subpage == "Logout":
            logout()

    elif st.session_state.role == "faculty":
        render_sidebar(
            [
                "Dashboard",
                "Student Search",
                "Student Profile",
                "Achievement Comparison",
                "Academic Analytics",
                "AI Assistant",
                "Logout",
            ],
            selected=st.session_state.subpage,
            on_logout=logout,
        )

        # Ensure selected student state exists (even if None)
        if "selected_student" not in st.session_state:
            st.session_state.selected_student = None

        show_faculty_dashboard(
            st.session_state.user,
            page=st.session_state.subpage,
            selected_student=st.session_state.selected_student,
        )


def main():
    if st.session_state.page == "landing":
        landing_page()
    elif st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "dashboard":
        dashboard_page()


if __name__ == "__main__":
    main()
