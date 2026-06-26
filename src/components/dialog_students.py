import streamlit as st
import pandas as pd

from src.database.db import get_enrolled_students


@st.dialog("Enrolled Students")
def students_dialog(subject_id):

    students = get_enrolled_students(subject_id)

    if not students:
        st.info("No students enrolled.")
        return

    rows = []

    for row in students:
        student = row["students"]

        rows.append({
            "Student ID": student["student_id"],
            "Name": student["name"]
        })

    st.dataframe(
        pd.DataFrame(rows),
        use_container_width=True,
        hide_index=True
    )