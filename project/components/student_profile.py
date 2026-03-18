import streamlit as st
import pandas as pd


def render_student_profile(student: dict):
    if not student:
        st.info("No student selected. Use Student Search to select a student.")
        return

    st.header("Student Profile")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader(student.get("name", "-"))
        st.write("**KTU Registration Number:**", student.get("univ_reg_no", "-"))
        st.write("**CGPA:**", student.get("cgpa", "-"))
        st.write("**Skills:**", ", ".join(student.get("skills", [])) or "-")

    with col2:
        st.metric("CGPA", student.get("cgpa", "-"))
        st.metric("Semester Count", len(student.get("sgpa", {})))

    st.markdown("---")
    st.subheader("Semester Performance")
    sgpa = student.get("sgpa", {})
    df = pd.DataFrame({"Semester": list(sgpa.keys()), "SGPA": list(sgpa.values())})
    st.table(df)
    st.line_chart(df.set_index("Semester"))
