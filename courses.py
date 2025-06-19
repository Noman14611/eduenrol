import streamlit as st
from utils.helpers import load_data, save_data

COURSE_FILE = "data/courses.json"

def course_section():
    st.header("📚 Course Management")

    # Load existing courses
    courses = load_data(COURSE_FILE)

    # ---------------- Add New Course ----------------
    with st.expander("➕ Add New Course"):
        title = st.text_input("Course Title")
        desc = st.text_area("Description")
        fee = st.number_input("Course Fee", min_value=0)
        duration = st.text_input("Duration (e.g., 4 Weeks)")
        video_url = st.text_input("Video URL (YouTube or Drive Preview Link)")

        if st.button("Add Course"):
            if not title or not desc or not duration:
                st.error("Please fill all fields.")
            else:
                # Add course to data
                courses.append({
                    "title": title,
                    "desc": desc,
                    "fee": fee,
                    "duration": duration,
                    "video": video_url  # ✅ Add video field
                })
                save_data(COURSE_FILE, courses)
                st.success("✅ Course added successfully!")

    # ---------------- Show All Courses ----------------
    st.subheader("📋 Available Courses")

    if not courses:
        st.info("No courses added yet.")
    else:
        for idx, course in enumerate(courses):
            st.markdown(f"### 🎓 {course['title']}")
            st.markdown(f"**Fee:** Rs {course['fee']}  |  **Duration:** {course['duration']}")
            st.markdown(course['desc'])

            # ✅ Embed video if available
            if course.get("video"):
                st.video(course["https://youtube.com/playlist?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0&si=d4AUDQPaG5YZ2riK"])

            st.markdown("---")
