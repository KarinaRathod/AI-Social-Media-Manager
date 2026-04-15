import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# -----------------------------
# LOAD ENV
# -----------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="AI Social Media Manager", layout="wide")
st.title("📱 AI Social Media Manager")
st.caption("Generate posts, captions & content strategies")

# -----------------------------
# SESSION STATE
# -----------------------------
if "posts" not in st.session_state:
    st.session_state.posts = []

# -----------------------------
# POST GENERATOR
# -----------------------------
st.subheader("✍️ Generate Post")

topic = st.text_input("Topic")
platform = st.selectbox("Platform", ["Instagram", "LinkedIn", "Twitter"])
tone = st.selectbox("Tone", ["Professional", "Casual", "Motivational", "Funny"])

if st.button("🚀 Generate Post"):
    if not topic.strip():
        st.warning("⚠️ Enter a topic")
    else:
        prompt = f"""
        Create a {platform} post about: {topic}

        Tone: {tone}

        Include:
        - Hook
        - Main content
        - CTA
        - Relevant hashtags
        """

        response = model.generate_content(prompt)
        post = response.text

        st.subheader("📄 Generated Post")
        st.write(post)

        st.session_state.posts.append(post)

# -----------------------------
# CONTENT CALENDAR
# -----------------------------
st.subheader("📅 Content Calendar")

days = st.selectbox("Select Duration", ["7 Days", "30 Days"])

if st.button("📊 Generate Calendar"):
    prompt = f"""
    Create a {days} social media content calendar.

    Include:
    - Daily post ideas
    - Platform suggestions
    - Content type
    """

    response = model.generate_content(prompt)
    st.write(response.text)

# -----------------------------
# CAPTION IMPROVER
# -----------------------------
st.subheader("🔥 Improve Caption")

caption = st.text_area("Enter caption")

if st.button("✨ Improve"):
    if caption.strip():
        prompt = f"""
        Improve this caption for engagement:

        {caption}

        Make it:
        - More engaging
        - Add hook
        - Add CTA
        """

        response = model.generate_content(prompt)
        st.write(response.text)

# -----------------------------
# SAVED POSTS
# -----------------------------
if st.session_state.posts:
    st.subheader("💾 Saved Posts")
    for p in st.session_state.posts[-5:]:
        st.info(p)