import streamlit as st
from utils.helpers import load_data, save_data

COURSE_FILE = "data/courses.json"

def course_section():
    st.header("📚 Course Management")

    courses = load_data(COURSE_FILE)

    # ---------------- Add New Course ----------------
    with st.expander("➕ Add New Course"):
        title = st.text_input("Course Title")
        desc = st.text_area("Description")
        fee = st.number_input("Course Fee", min_value=0)
        duration = st.text_input("Duration (e.g., 4 weeks)")
        video_url = st.text_input("https://youtube.com/playlist?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0&si=d4AUDQPaG5YZ2riK")

        if st.button("Add Course"):
            if not title or not desc or not duration:
                st.error("Please fill in all required fields.")
            else:
                courses.append({
                    "title": title,
                    "desc": desc,
                    "fee": fee,
                    "duration": duration,
                    "video": video_url  # ✅ Video field added
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
            st.markdown(f"{course['desc']}")

            # ✅ Show video if exists
            if course.get("video"):
                st.video(course["video"])

            st.markdown("---")
