import plotly.express as px
import streamlit as st


def _count_certificates(student: dict) -> int:
    certs = student.get("uploaded_certificates", {})
    return sum(len(items) for items in certs.values())


def render_overview_cards(students: list[dict]):
    total_students = len(students)
    avg_cgpa = round(sum(s.get("cgpa", 0) for s in students) / total_students, 2) if total_students else 0
    total_certs = sum(_count_certificates(s) for s in students)
    total_internships = sum(len(s.get("internships", [])) for s in students)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Students", total_students)
    col2.metric("Average CGPA", avg_cgpa)
    col3.metric("Total Certificates", total_certs)
    col4.metric("Total Internships", total_internships)


def render_cgpa_distribution(students: list[dict]):
    if not students:
        st.info("No student data available for CGPA distribution.")
        return

    fig = px.histogram(
        [s.get("cgpa", 0) for s in students],
        nbins=10,
        labels={"value": "CGPA"},
        title="CGPA Distribution",
    )
    st.plotly_chart(fig, use_container_width=True)


def render_skills_popularity(students: list[dict]):
    skill_counts = {}
    for s in students:
        for skill in s.get("skills", []):
            skill_counts[skill] = skill_counts.get(skill, 0) + 1

    if not skill_counts:
        st.info("No skills data available.")
        return

    df = {
        "Skill": list(skill_counts.keys()),
        "Count": list(skill_counts.values()),
    }
    fig = px.bar(df, x="Skill", y="Count", title="Skills Popularity")
    st.plotly_chart(fig, use_container_width=True)


def render_certificate_breakdown(students: list[dict]):
    categories = ["sports", "cultural", "hackathons"]
    counts = {c: 0 for c in categories}

    for s in students:
        certs = s.get("uploaded_certificates", {})
        for c in categories:
            counts[c] += len(certs.get(c, []))

    df = {"Category": list(counts.keys()), "Count": list(counts.values())}
    fig = px.bar(df, x="Category", y="Count", title="Certificates by Category")
    st.plotly_chart(fig, use_container_width=True)
