import streamlit as st
from utils.helpers import load_data, save_data

COURSE_FILE = "data/courses.json"

def course_section():
    st.header("📚 Course Management")

    courses = load_data(COURSE_FILE)

    with st.expander("➕ Add New Course"):
        title = st.text_input("Course Title")
        desc = st.text_area("Description")
        fee = st.number_input("Course Fee", min_value=0)
        duration = st.text_input("Duration (e.g., 4 weeks)")
        if st.button("Add Course"):
            courses.append({
                "title": title,
                "desc": desc,
                "fee": fee,
                "duration": duration
            })
            save_data(COURSE_FILE, courses)
            st.success("Course added successfully!")

    st.subheader("📋 Available Courses")
    for idx, course in enumerate(courses):
        st.markdown(f"### {course['title']}")
        st.markdown(f"**Fee:** Rs {course['fee']}  |  **Duration:** {course['duration']}")
        st.markdown(f"{course['desc']}")
        st.markdown("---")

