import streamlit as st
from courses import course_section
from enrollments import enrollment_section

st.set_page_config(page_title="EduEnroll - LMS", layout="wide")

st.sidebar.title("EduEnroll 📘")
section = st.sidebar.selectbox("Choose Section", ["Course Management", "Enrollments"])

if section == "Course Management":
    course_section()
elif section == "Enrollments":
    enrollment_section()

