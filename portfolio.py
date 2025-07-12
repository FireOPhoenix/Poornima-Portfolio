import streamlit as st
from pathlib import Path
from PIL import Image

# --- PATH SETTINGS ---
profile_image = "Professional photo.jpg"
resume_file = "Poornima_Resume(8).pdf"

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Poornima Rana - Portfolio",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- LOAD ASSETS ---
img = Image.open(profile_image)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- SIDEBAR ---
st.sidebar.image(img, width=150)
st.sidebar.title("Poornima Rana")
st.sidebar.markdown("""
**Machine Learning Intern | Data Analyst | Software Developer**

📍 Gurugram, Haryana  
📧 [poornima.26official@gmail.com](mailto:poornima.26official@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/poornima-rana)  
🐱 [GitHub](https://github.com/FireOPhoenix)
""")
st.sidebar.download_button(
    label="📄 Download Resume",
    data=PDFbyte,
    file_name="Poornima_Rana_Resume.pdf",
    mime="application/pdf"
)

st.sidebar.markdown("---")
selected_section = st.sidebar.radio("📌Go to", [
    "Home", "Education", "Experience", "Skills", "Projects", "Certifications", "Achievements"
])

# --- CUSTOM CSS ---
st.markdown("""
<style>
body, html {
    font-family: 'Roboto', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# --- SECTIONS ---
if selected_section == "Home":
    st.markdown("<h1 class='main-header'>POORNIMA RANA</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class="contact-info">
            <p><b>📞</b> +91 7428919166</p>
            <p><b>📧</b> poornima.26official@gmail.com</p>
            <p>
                🔗 <a href="https://linkedin.com/in/poornima-rana" target="_blank">LinkedIn</a> |
                🐱 <a href="https://github.com/FireOPhoenix" target="_blank">GitHub</a>
            </p>
        </div>
    """, unsafe_allow_html=True)

elif selected_section == "Education":
    st.subheader("🎓Education")
    st.markdown("**Dronacharya College of Engineering**, Gurugram, Haryana, India")
    st.markdown("*B.Tech in Computer Science Engineering | CGPA: 7.82 | May 2026*")
    st.markdown("**Relevant Coursework**: Machine Learning, Deep Learning, Data Structures, DBMS, Statistical Analysis")

elif selected_section == "Experience":
    st.subheader("💼Experience")
    with st.expander("Austere Systems Pvt. Ltd. — Machine Learning Intern (June–July 2024)"):
        st.write("""
        - Built YOLOv3-based real-time facial recognition system with 92% accuracy.
        - Processed 10k+ images daily in detection pipeline.
        - Reduced training time by 35% using Pandas and NumPy.
        - Integrated models into production with cross-functional teams.
        """)
    with st.expander("Deloitte — Data Analyst Virtual Internship (March 2025)"):
        st.write("""
        - Built Tableau dashboard with 15+ KPIs.
        - Processed 50k+ records, applied statistical summaries.
        - Applied forensic analytics on $2M+ financial data.
        """)
    with st.expander("Walmart USA — Software Dev Intern (April 2025)"):
        st.write("""
        - Designed optimized heap in Java; improved logistics by 25%.
        - Managed Git/Subversion across 10+ remote projects.
        - Implemented UML diagrams and CI/CD practices.
        """)

elif selected_section == "Skills":
    st.subheader("🛠️ Technical Skills")
    st.markdown("""
    - **Languages**: Python, R, SQL, Java, JavaScript  
    - **ML Libraries**: Scikit-Learn, TensorFlow, PyTorch, Keras  
    - **Data Analysis**: Pandas, NumPy, Matplotlib, Seaborn, Statsmodels  
    - **Visualization**: Tableau, Power BI, Plotly, D3.js  
    - **Databases**: MySQL, PostgreSQL, MongoDB, Apache Spark  
    - **Cloud**: AWS, Azure, GCP, Docker  
    - **Tools**: Git, Jupyter, PyCharm, RStudio  
    - **Statistical Concepts**: Regression, A/B Testing, Time Series
    """)

elif selected_section == "Projects":
    st.subheader("📂Projects")
    with st.expander("Advanced Facial Recognition System"):
        st.write("""
        - CNN-based model trained on 10,000+ images with 94% accuracy.
        - Live camera detection at 30 FPS.
        """)
    with st.expander("Medical Diagnostic AI System"):
        st.write("""
        - Detected COVID/Pneumonia using deep learning on X-rays.
        - Used LIME for explainable AI interpretation.
        """)
    with st.expander("Multi-Class Object Detection"):
        st.write("""
        - YOLO-based detection on 80+ object classes with 89% mAP.
        - Achieved 45 FPS processing on standard systems.
        """)
    with st.expander("Retail Sales Forecasting Engine"):
        st.write("""
        - Built ARIMA/Exponential Smoothing model for Walmart sales.
        - Achieved 87% forecasting accuracy.
        """)

elif selected_section == "Certifications":
    st.subheader("🎓Certifications")
    st.markdown("""
    - Google Project Management Professional  
    - Data Analysis with R – Johns Hopkins University  
    - Python for Everybody – University of Michigan  
    - Convolutional Neural Networks – DeepLearning.AI
    """)

elif selected_section == "Achievements":
    st.subheader("🏆Achievements")
    st.markdown("""
    - Deployed 4+ ML models in production  
    - Processed 100,000+ records in analysis tasks  
    - Reduced training time by 35%  
    - Saved $15,000+ annually through ML optimization  
    """)

# --- FOOTER ---
st.markdown("---")
st.success("Thank you for visiting my portfolio! Let's connect on [LinkedIn](https://linkedin.com/in/poornima-rana).")
