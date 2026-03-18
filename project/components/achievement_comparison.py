import streamlit as st
import pandas as pd


def _count_certs(student: dict) -> dict:
    certs = student.get("uploaded_certificates", {})
    return {
        "sports": len(certs.get("sports", [])),
        "cultural": len(certs.get("cultural", [])),
        "hackathons": len(certs.get("hackathons", [])),
    }


def render_achievement_comparison(students: list[dict], selected: list[dict]):
    if not selected:
        st.info("Select students to compare using the dropdown on the left.")
        return

    # Build comparison table
    rows = []
    for student in selected:
        cert_counts = _count_certs(student)
        rows.append(
            {
                "Student": student.get("name"),
                "KTU ID": student.get("univ_reg_no"),
                "Sports": cert_counts["sports"],
                "Cultural": cert_counts["cultural"],
                "Hackathons": cert_counts["hackathons"],
                "Internships": len(student.get("internships", [])),
            }
        )

    df = pd.DataFrame(rows)
    st.subheader("Achievement Comparison")
    st.dataframe(df)

    # Bar chart for certificates
    st.markdown("#### Certificates Comparison")
    cert_df = df[["Student", "Sports", "Cultural", "Hackathons"]].set_index("Student")
    st.bar_chart(cert_df)

    # CGPA comparison
    st.markdown("#### CGPA Comparison")
    cgpa_df = df[["Student", "KTU ID"]].copy()
    cgpa_df["CGPA"] = [s.get("cgpa", 0) for s in selected]
    cgpa_chart = cgpa_df.set_index("Student")
    st.bar_chart(cgpa_chart["CGPA"])

    # Skills comparison (unique skills)
    st.markdown("#### Skills Comparison")
    skill_sets = {s.get("name"): set(s.get("skills", [])) for s in selected}
    for name, skills in skill_sets.items():
        st.write(f"**{name}**: {', '.join(sorted(skills)) or 'No skills'}")
