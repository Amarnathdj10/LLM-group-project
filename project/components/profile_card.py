import streamlit as st


def render_profile_card(student: dict):
    st.markdown("### Student Profile")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Name**")
        st.write(student.get("name", "-"))

        st.write("**KTU Registration**")
        st.write(student.get("univ_reg_no", "-"))

        st.write("**Department**")
        st.write(student.get("department", "Computer Science"))

    with col2:
        st.write("**Current Semester**")
        st.write(student.get("current_semester", "4"))

        st.write("**CGPA**")
        st.write(student.get("cgpa", "-") )

    with col3:
        st.write("**Skills**")
        skills = student.get("skills", [])
        for skill in skills:
            st.button(skill, key=f"skill_{skill}")
