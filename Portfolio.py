import streamlit as st
from PIL import Image

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Data Analyst Portfolio", page_icon="📊", layout="wide")

# -----------------------------
# HEADER SECTION
# -----------------------------
st.title("📊 Data Analyst Portfolio")
st.subheader("Hi, I'm Parth Khillare")
st.write("Data Analyst | Business Intelligence | SQL | Python | Power BI")

# Add profile image (optional)
# profile_pic = Image.open("your_photo.jpg")
# st.image(profile_pic, width=180)

# -----------------------------
# ABOUT SECTION
# -----------------------------
st.header("About Me")
st.write("""
I am a passionate Data Analyst with expertise in transforming raw data into meaningful insights.  
I enjoy working with **SQL, Python, Power BI** to create impactful dashboards and reports that drive decision-making.  

- 🎯 Strong in **data cleaning, EDA, and visualization**  
- 📊 Skilled in **business analytics & reporting**  
- 🛠 Experienced with **Excel, Pandas, Numpy, and Streamlit**  
- 🤝 Looking for opportunities in **Data Analytics & Business Intelligence**
""")

# -----------------------------
# SKILLS SECTION
# -----------------------------
st.header("Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Programming")
    st.write("- Python (Pandas, Numpy, Matplotlib, Seaborn)")
    st.write("- SQL")

with col2:
    st.subheader("Visualization Tools")
    st.write("- Power BI")
    st.write("- Excel (Pivot Tables, VLOOKUP, Macros)")

with col3:
    st.subheader("Other Skills")
    st.write("- Data Cleaning & Transformation")
    st.write("- Statistical Analysis")
    st.write("- Machine Learning (Basics)")
    st.write("- Streamlit Web Apps")

# -----------------------------
# PROJECTS SECTION
# -----------------------------
st.header("Projects")

with st.expander("📊 Blinkit-Sales Dashboard (Power BI)"):
    st.write("""
    - Built an **interactive Power BI dashboard** for sales insights.  
    - Analyzed revenue trends, regional performance, and customer behavior.  
    - Helped the company identify **top-performing products**.  
    """)
    st.image("C:/Users/LENOVO/OneDrive - IIIT Bhopal/Documents/Python/Portfolio project/Blink-it_Output.png", use_container_width=True)
 # Add screenshot of dashboard if available


# -----------------------------
# RESUME SECTION
# -----------------------------
st.header("Resume")
st.write("📄 [My Resume](C:/Users/LENOVO\OneDrive - IIIT Bhopal/Documents/Python/Portfolio project/Parth_Resume.pdf)")

# -----------------------------
# CONTACT SECTION
# -----------------------------
st.header("Contact")
st.write("📧 [Email](https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox)")
st.write("🔗 [LinkedIn](https://www.linkedin.com/in/parth-khillare-b849bb269/)")
st.write("💻 [GitHub](https://github.com/DevilxHunter21)")

st.success("Thanks for visiting my portfolio! 🚀")
