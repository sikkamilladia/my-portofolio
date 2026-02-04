import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
from PIL import Image  # Required to open local images

# --- FUNCTION TO LOAD LOTTIE ANIMATION ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Sikka's Portfolio", page_icon="🎓", layout="wide")

# --- CUSTOM CSS (FORCE POPPINS FONT) ---
st.markdown("""
    <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        /* Apply Poppins to all text */
        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif !important;
        }
        
        /* Make H1 headers thicker & aesthetic */
        h1, h2, h3 {
            font-weight: 700 !important;
            letter-spacing: -1px;
        }
    </style>
""", unsafe_allow_html=True)

# Load Assets (Animation)
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# --- 2. SIDEBAR (PROFILE) ---
with st.sidebar:
    # --- PROFILE PICTURE SECTION ---
    # Using try-except to prevent errors if file is missing
    try:
        image = Image.open("profile.jpg") # Ensure filename matches
        st.image(image, width=200)
    except FileNotFoundError:
        st.warning("File 'profile.jpg' not found in folder.")
        st.image("https://placehold.co/400x400/png?text=No+Image", width=200)

    st.title("Sikka Fazzad Milladia")
    st.subheader("CS Student @ NTHU | Data Enthusiast")
    
    st.write("---")
    st.write("""
    📍 **Hsinchu City, Taiwan**
    I build machine learning models and interactive dashboards to solve real-world problems.
    """)
    
    st.write("### 🛠 Tech Stack")
    st.caption("Python, SQL, Pandas, NumPy, Scikit-learn, XGBoost, Tableau.")
    
    st.write("---")
    # Social Media Links
    st.link_button("🔗 LinkedIn", "https://linkedin.com/in/sikka-fazzad")
    st.link_button("🐙 GitHub", "https://github.com/sikkamilladia")
    st.link_button("📧 Email Me", "mailto:sikkamilladia97@gmail.com")

# --- 3. HERO SECTION ---
col1, col2 = st.columns([1, 2])

with col1:
    st_lottie(lottie_coding, height=300, key="coding")

with col2:
    st.title("Turning Data into Decisions 🚀")
    st.write("""
    ### Hi, I'm Sikka!
    I am a **Computer Science student at National Tsing Hua University**.
    
    I specialize in **Machine Learning**, **Data Visualization**, and **Web Development**.
    My goal is to leverage data to create impactful business solutions.
    """)
    st.info("Check out my interactive 'Business Advisor' demo below! 👇")

st.divider()

# --- MAIN TABS ---
tab_projects, tab_exp, tab_visual = st.tabs(["📊 Data Projects", "💼 Experience", "📷 Visual Gallery"])

# === TAB 1: DATA PROJECTS ===
with tab_projects:
    st.header("Featured Projects")

    # --- PROJECT 1: BUSINESS ADVISOR ---
    with st.container(border=True):
        st.subheader("1. Business Advisor Software (Interactive Demo)")
        st.write("*Tech Stack: Python, Pandas, Matplotlib, Seaborn, Streamlit*")
        
        # Data Simulation
        sales_data = pd.DataFrame({
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
            'Revenue': [4500, 5200, 4800, 6100, 5900, 7200, 8100, 7900],
            'Profit': [1200, 1500, 1100, 2100, 1900, 2800, 3200, 3000],
            'Expenses': [3300, 3700, 3700, 4000, 4000, 4400, 4900, 4900]
        })
        
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Total Revenue", "$49,700", "12%")
        col_m2.metric("Avg Profit Margin", "35%", "5%")
        col_m3.metric("Cust. Satisfaction", "4.8/5.0", "0.2")

        chart_type = st.radio("Select View:", ["Revenue Trend", "Profit Analysis"], horizontal=True)
        
        if chart_type == "Revenue Trend":
            fig = px.line(sales_data, x='Month', y='Revenue', markers=True, title="Monthly Revenue Growth")
        else:
            fig = px.bar(sales_data, x='Month', y=['Profit', 'Expenses'], title="Profit vs Expenses Breakdown", barmode='group')
            
        st.plotly_chart(fig, use_container_width=True)

    # --- PROJECT 2 & 3 ---
    st.divider()
    col_p2, col_p3 = st.columns(2)
    
    with col_p2:
        with st.container(border=True):
            st.subheader("2. Titanic Survival Prediction")
            st.write("ML pipeline predicting passenger survival with **82% accuracy** using XGBoost.")
            st.link_button("View Code", "https://github.com/sikkamilladia/titanic-survival-prediction")

    with col_p3:
        with st.container(border=True):
            st.subheader("3. Movie Rec. System")
            st.write("Content-based recommendation engine using **Cosine Similarity**.")
            st.link_button("View Code", "https://github.com/sikkamilladia/movie-recommendation-system")

# === TAB 2: EXPERIENCE ===
with tab_exp:
    st.header("Professional Experience")
    
    # --- 1. EECS-GSA (MARKETING) ---
    with st.container(border=True):
        col_text, col_img = st.columns([2, 1])
        with col_text:
            st.subheader("📢 Marketing Director")
            st.write("**EECS-GSA (Global Student Association)** | *June 2025 - Present*")
            st.write("""
            - 📈 Analyzed social media metrics to **increase event attendance by 20%**.
            - 🎯 Refined messaging for diverse international student demographics.
            - 🤝 Collaborated with cross-functional teams for brand consistency.
            """)
        with col_img:
            try:
                st.image("doc_gsa.JPG", caption="Marketing Strategy Meeting", use_container_width=True)
            except:
                st.info("📸 (Please provide file 'doc_gsa.JPG')")

    # --- 2. FSA (DOCUMENTATION) ---
    with st.container(border=True):
        col_text, col_img = st.columns([2, 1])
        with col_text:
            st.subheader("📸 Public Relations (Documentation)")
            st.write("**Foreign Student Association (FSA)** | *June 2025 - Present*")
            st.write("""
            Responsible for capturing and archiving major student events.
            - 🎥 Produced high-quality photo & video documentation for internal & social media use.
            - 🖼️ Managed digital assets and visual storytelling for the organization.
            - 🤝 Supported PR division in creating engaging visual content.
            """)
        with col_img:
            try:
                st.image("doc_fsa.JPG", caption="Documentation Duty at FSA", use_container_width=True)
            except:
                st.info("📸 (Please provide file 'doc_fsa.JPG')")

    # --- 3. MTsN 2 BEKASI (TEACHER/ADMIN) ---
    with st.container(border=True):
        col_text, col_img = st.columns([2, 1])
        with col_text:
            st.subheader("🏫 Apprentice Teacher & Admin Officer")
            st.write("**MTsN 2 Bekasi, Indonesia** | *July 2022 - July 2023*")
            st.write("""
            - 📂 Managed academic records for **300+ students** with 100% accuracy.
            - 📊 Streamlined library inventory tracking using **Excel**.
            - ⚡ Improved organizational efficiency in administrative workflows.
            """)
        with col_img:
            try:
                st.image("doc_mts.jpg", caption="Teaching & Admin Activities", use_container_width=True)
            except:
                st.info("📸 (Please provide file 'doc_mts.jpg')")

# === TAB 3: VISUAL GALLERY ===
with tab_visual:
    st.header("Visual Portfolio")
    st.write("A glimpse of my shots. Click the button below for the full album.")
    
    # --- LOCAL PHOTO GRID (TEASER) ---
    col_a, col_b = st.columns(2)
    
    with col_a:
        try:
            st.image("foto1.JPG", caption="Shot 1")
            st.image("foto2.JPG", caption="Shot 2")
        except:
            st.error("File foto1.JPG / foto2.JPG not found.")
            
    with col_b:
        try:
            st.image("foto3.JPG", caption="Shot 3")
            st.image("foto4.JPG", caption="Shot 4")
        except:
            st.error("File foto3.JPG / foto4.JPG not found.")

    st.divider()
    
    # --- GOOGLE DRIVE BUTTON ---
    # st.success("Want to see full resolution and more collections?")
    # st.link_button("📂 Open Full Gallery (Google Drive)", "https://drive.google.com/drive/u/0/")
    

    st.info("More collections coming soon! Stay tuned. 📸")
