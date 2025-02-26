import streamlit as st
import pandas as pd
import random

# Page Configuration
st.set_page_config(
    page_title="Growth Mindset Project", 
    page_icon="✹",  # Corrected parameter
    layout="centered"
)

# Title
st.title("🌟 Growth Mindset Challenge 🌟")

# Images URLs from Google 
growth_images = [
    "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?ixlib=rb-1.2.1&auto=format&fit=crop&w=1348&q=80",
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-1.2.1&auto=format&fit=crop&w=1352&q=80",
    "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80"
]

# Random image select
selected_image = random.choice(growth_images)
st.image(selected_image, caption="Keep Growing! 🌱")

# Custom authentication logic
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None

if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":  # Replace with your logic
            st.session_state.logged_in = True
            st.session_state.username = username  # Store username in session state
            st.rerun()
        else:
            st.error("Invalid username or password")
    st.stop()

# Display user information
st.write(f"Hi, {st.session_state.username}")  # Access username from session state

# Logout button
if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = None  # Clear username from session state
    st.rerun()

# Welcome Section
st.header("🚀 Welcome to Your Growth Journey")
st.write("""
This is the beginning of an exciting path where every step you take brings new opportunities to learn, improve, and achieve your goals. 
Growth is not just about reaching a destination; it's about embracing challenges, gaining knowledge, and evolving into the best version of yourself. 
Stay consistent, stay curious, and remember—every small effort counts. Keep pushing forward, and success will follow! 🌟
""")

# Daily Quote Section
st.header("✨ Daily Quote to Inspire Your Growth Mindset ✨")
st.write("""
**"Success is not final, failure is not fatal: it is the courage to continue that counts."** – Winston Churchill
Every day is a new opportunity to grow, learn, and improve. Embrace challenges with a positive mindset, believe in your potential, and keep moving forward. 
Your journey to success is built on persistence and resilience. Stay inspired, stay motivated! 🚀
""")

# Challenge Section
st.header("💪 What's Your Challenge Today? 💪")
user_input = st.text_input("Describe a challenge you're facing today:")

if user_input:
    st.success(f"🌟 You're facing: **{user_input}**. Keep pushing forward! 🚀")
else:
    st.warning("💬 Tell Us About Your Challenge to Get Started! 💬")

# Reflection Section
st.header("🌱 Reflect on Your Growth and Progress 🌱")
reflection = st.text_area("Write down your thoughts and feelings about your progress:")

if reflection:
    st.success(f"📝 **Great Insight!** {reflection} Keep reflecting and growing! 🌟")
else:
    st.info("🔍 Reflecting on Past Experiences Helps You Grow! 🔍")

# Achievements Section
st.header("🎉 Celebrate Your Wins! 🎉")
achievement = st.text_input("🏆 Share Something You’ve Recently Accomplished! 🏆")

if achievement:
    st.success(f"🌟 **Amazing! You Achieved It!** {achievement} 🌟")
else:
    st.info("🎉 Big or Small, Every Achievement Counts! 🎉")

# Motivational Resources Section
st.header("📚 Motivational Resources 📚")
st.write("Here are some resources to keep you motivated:")
st.markdown("""
- [The Power of Belief](https://www.youtube.com/watch?v=pN34FNbOKXc) (Video)
- [Growth Mindset vs Fixed Mindset](https://www.youtube.com/watch?v=M1CHPnZfFmU) (Video)
- [10 Ways to Develop a Growth Mindset](https://www.forbes.com/sites/forbescoachescouncil/2021/03/16/10-ways-to-develop-a-growth-mindset/) (Article)
""")

# Progress Visualization
st.header("📊 Your Progress Overview 📊")
progress_data = {
    "Challenges": [user_input],
    "Reflections": [reflection],
    "Achievements": [achievement]
}
progress_df = pd.DataFrame(progress_data)
st.bar_chart(progress_df)

# Footer
st.write("---")
st.write("🌟 **Keep Believing in Yourself – Growth is a Journey!** 🌟")
st.write("✨ Created by **Muhammad Tahir Hasni** ✨")