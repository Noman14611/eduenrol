# ---------------- Show All Courses ----------------
st.subheader("📋 Available Courses")

if not courses:
    st.info("No courses added yet.")
else:
    for idx, course in enumerate(courses):
        st.markdown(f"### 🎓 {course['title']}")
        st.markdown(f"**Fee:** Rs {course['fee']}  |  **Duration:** {course['duration']}")
        st.markdown(f"{course['desc']}")

        # ✅ Video embed here
        if course.get("video"):
            st.video(course["video"])

        st.markdown("---")
