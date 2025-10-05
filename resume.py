# resume_app.py
import streamlit as st

# ---------- Page Config ----------
st.set_page_config(page_title="Sharrmini A/P Veeran - Resume", layout="centered")

# ---------- Custom Styling ----------
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: #fafafa;
        }
        h1, h2, h3 {
            color: #ffffff;
        }
        .section-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin-top: 25px;
            color: #ff4b4b;
        }
        .contact-info a {
            color: #58a6ff;
            text-decoration: none;
        }
        hr {
            border: 1px solid #333;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.title("Sharrmini A/P Veeran")
st.subheader("Final Year Student | Bachelor of Information Technology")

st.write("---")

# ---------- Contact Information ----------
st.markdown("### 📌 Contact Information")
st.markdown("""
**Email:** [sharrmini22@gmail.com](mailto:sharrmini22@gmail.com)  
**Phone:** 014-3063720  
**LinkedIn:** [Sharrmini Veeran](https://linkedin.com/in/sharrminiveeran)
""")

# ---------- About Me ----------
st.markdown("### 🧠 About Me")
st.write("""
I am a dedicated and detail-oriented final-year student pursuing a **Bachelor of Information Technology**
at **Universiti Malaysia Kelantan**.  
My academic and project experiences have developed strong skills in **IoT development, data analytics, and software engineering**.  
I am passionate about using technology to create efficient and sustainable solutions, particularly in smart systems and automation.  
My goal is to contribute to innovative digital transformation projects that bridge technical precision and real-world impact.
""")

# ---------- Education ----------
st.markdown("### 🎓 Education")
st.write("""
**Bachelor of Information Technology** — Universiti Malaysia Kelantan (2022 – Present)  
_Key Areas: IoT Systems, Machine Learning, Database Systems, Software Engineering_
""")

# ---------- Skills ----------
st.markdown("### 🧰 Skills")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - Python, Java, C++
    - HTML, CSS, JavaScript
    - SQL & Databases
    """)

with col2:
    st.markdown("""
    - IoT Development (Arduino, NodeMCU)
    - Data Analysis & Visualization
    - Problem-Solving & Team Collaboration
    """)

# ---------- Projects ----------
st.markdown("### 🚀 Projects")
st.markdown("**Solar-Powered Smart Hydroponic System**")
st.write("""
- Developed an IoT-based hydroponic farming system using Arduino Uno and NodeMCU  
- Integrated sensors for automation  
- Enabled real-time monitoring through a cloud dashboard
""")

# ---------- Additional Information ----------
st.markdown("### 🌟 Additional Information")
st.write("""
**Languages:** English, Tamil, Malay  
**Interests:** Technology, Research, Sustainable Agriculture, Innovation
""")

# ---------- Footer ----------
st.write("---")
st.markdown(
    "<p style='text-align:center; color:grey;'>Created with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
