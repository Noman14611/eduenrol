import streamlit as st
from utils.helpers import load_data, save_data

COURSE_FILE = "data/courses.json"
ENROLL_FILE = "data/enrollments.json"

def enrollment_section():
    st.header("📝 Course Enrollment")

    courses = load_data(COURSE_FILE)
    enrollments = load_data(ENROLL_FILE)

    name = st.text_input("Student Name")
    email = st.text_input("Email")
    course_options = [course['title'] for course in courses]
    selected_course = st.selectbox("Select Course", course_options)
    paid = st.selectbox("Fee Status", ["Paid", "Unpaid"])

    if st.button("Enroll"):
        enrollments.append({
            "name": name,
            "email": email,
            "course": selected_course,
            "paid": paid
        })
        save_data(ENROLL_FILE, enrollments)
        st.success("Enrolled Successfully!")

    st.subheader("📌 All Enrollments")
    for enr in enrollments:
        st.markdown(f"**{enr['name']}** - {enr['course']} - *{enr['paid']}*")

