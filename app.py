from pathlib import Path
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# --- HELPER FUNCTIONS ---

def project_img_to_base64(img):
    """Convert PIL Image to base64 (for PNG images only)."""
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def file_to_base64(path):
    """Convert any file (PNG, GIF, etc.) to base64 string."""
    with open(path, "rb") as file:
        data = file.read()
    return base64.b64encode(data).decode()

def load_css(file_path):
    with open(file_path) as f:
        return f"<style>{f.read()}</style>"

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic_path = current_dir / "assets" / "profile.png"
resume_path = current_dir / "assets" / "Resume(Nikhil Gupta).pdf"

# Logos
exl_logo_path = current_dir / "assets" / "exl_service_logo.png"
accenture_logo_path = current_dir / "assets" / "accenture_logo.png"
kmitl_logo_path = current_dir / "assets" / "kmitl_logo.png"

# Project media (some are gifs)
project_media = {
    "Sign Language to Text Conversion": current_dir / "assets" / "sign_language.png",
    "Crypto Data Pipeline": current_dir / "assets" / "crypto_data_pipeline.png",
    "ArchitectureGen": current_dir / "assets" / "ArchitectureGen.png"
}

# Project descriptions for showing below the images
project_descriptions = {
    "Sign Language to Text Conversion": "Real-time system using CNN-based computer vision to convert sign language gestures into text for hearing and speaking impaired.",
    "Crypto Data Pipeline": "An end-to-end data pipeline for cryptocurrency market data ingestion, processing, and visualization using cloud tools.",
    "ArchitectureGen": "Automated project architecture visualization tool using Python and MermaidJS for GitHub repos."
}

# Certificates stored locally
certificates = [
    {
        "name": "Databricks Certified Data Engineer Associate",
        "img_path": current_dir / "assets" / "Databricks_Certificate.png"
    },
    {
        "name": "ACE: Growth Catalyst Award - Accenture Celebrate Excellence (FY22 Q4)",
        "img_path": current_dir / "assets" / "Ace_Award.png"
    }
]

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Nikhil Gupta"
PAGE_ICON = ":wave:"
NAME = "Nikhil Gupta"
DESCRIPTION = "Experienced Data Engineering Consultant specializing in cloud solutions and automation for scalable, data-driven outcomes."
EMAIL = "emnikkhil@email.com"
MOBILE = "+91-XXXXXXXXXX"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/guptanikhil1/",
    "GitHub": "https://github.com/emnikhil"
}

PROJECTS = {
    "Sign Language to Text Conversion": "https://github.com/emnikhil/Sign-Language-To-Text-Conversion",
    "Crypto Data Pipeline": "https://github.com/emnikhil/Crypto-Data-Pipeline",
    "ArchitectureGen": "https://github.com/emnikhil/ArchitectureGen"
}

# --- PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD IMAGE & RESUME ---
profile_pic = Image.open(profile_pic_path)
exl_logo = Image.open(exl_logo_path)
accenture_logo = Image.open(accenture_logo_path)
kmitl_logo = Image.open(kmitl_logo_path)
with open(resume_path, "rb") as f:
    resume_bytes = f.read()

# --- LOAD CSS ---
css_file = current_dir / "styles" / "main.css"
st.markdown(load_css(css_file), unsafe_allow_html=True)

# --- HEADER SECTION ---
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    st.image(profile_pic, width=180)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.markdown(f"📫 **Email:** {EMAIL}  \n📱 **Mobile:** {MOBILE}")
    st.download_button(
        label="📄 Download Resume",
        data=resume_bytes,
        file_name=resume_path.name,
        mime="application/pdf",
    )
    cols = st.columns(len(SOCIAL_MEDIA))
    for idx, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[idx].markdown(f"[{platform}]({link})")

st.markdown("---")

# --- EXPERIENCE & QUALIFICATIONS ---
st.subheader("Experience & Qualifications")
st.write(
    """
- **3.5+** years of experience designing and optimizing scalable data pipelines using **BigQuery**, **Airflow**, **Spark**, and **GCP**
- Proficient in developing end-to-end **ETL** and **ELT** workflows with strong hands-on expertise in **Python** automation and **SQL**
- Skilled in **cloud data migration**, **orchestration**, and **performance tuning**
- Bachelor of Technology **(Honours)** in **Computer Science and Engineering**
"""
)

st.markdown("---")

# --- SKILLS ---
st.subheader("Technical Skills")
st.write(
    """
- 👨‍💻 **Languages:** Scala, PySpark, Python, SQL  
- ⚙️ **Big Data:** Apache Spark, Apache Hive, Apache Airflow, Databricks
- 🗄️ **Databases:** Cassandra, BigQuery, MySQL, Oracle  
- ☁️ **Cloud (GCP):** Dataproc, Composer, SQL, Storage, BigQuery  
- 🧰 **Tools:** Git, Bitbucket, Streamlit
"""
)

st.markdown("---")

# --- WORK HISTORY ---
st.subheader("Work History")

def work_entry(logo, company, role_dates, description):
    col_logo, col_text = st.columns([1, 8], gap="small")
    with col_logo:
        st.image(logo, width=80)
    with col_text:
        st.markdown(f"**{company}**  \n*{role_dates}*")
        st.write(description)

work_entry(
    exl_logo,
    "Exl Service, India | Senior Business Analyst",
    "Jan' 2025 - Present",
    """
- Migrated and transformed multi-source data into BigQuery, automated schema validations.
- Automated GitHub project architecture visualizations using Python and MermaidJS.
- Collaborated with stakeholders and optimized pipeline performance using Airflow.
"""
)

work_entry(
    accenture_logo,
    "Accenture, India | Data Engineer",
    "Jan' 2022 - Jan' 2025",
    """
- Migrated Spark jobs to BigQuery procedures, enhancing workflow automation via Airflow.
- Optimized MySQL stored procedures for real-time GUI data handling.
- Reduced pipeline errors and execution time by 30% through DAG tuning and automation.
"""
)

work_entry(
    kmitl_logo,
    "KMITL, Thailand | Research Intern",
    "Sept' 19 - Oct' 19",
    """
- Developed a CNN-based Computer Vision solution for steak fat grading.
- Achieved 92% accuracy for the Thailand Livestock Development Department.
"""
)

st.markdown("---")

# --- PROJECTS SECTION ---
st.subheader("Projects")

projects_per_row = 2
project_names = list(PROJECTS.keys())
total_projects = len(project_names)

for i in range(0, total_projects, projects_per_row):
    cols = st.columns(projects_per_row)
    for idx, col in enumerate(cols):
        project_index = i + idx
        if project_index >= total_projects:
            break
        project_name = project_names[project_index]
        project_link = PROJECTS[project_name]
        project_media_path = project_media.get(project_name)
        project_desc = project_descriptions.get(project_name, "")

        if project_media_path and project_media_path.exists():
            media_base64 = file_to_base64(project_media_path)
            media_extension = project_media_path.suffix.lower()
            mime_type = "gif" if media_extension == ".gif" else "png"

            with col:
                st.markdown(
                    f"""
                    <a href="{project_link}" target="_blank" style="text-decoration:none; color:black;">
                        <div class="project-card">
                            <img src="data:image/{mime_type};base64,{media_base64}" class="project-img" />
                            <p class="project-title">{project_name}</p>
                            <p class="project-desc">{project_desc}</p>
                        </div>
                    </a>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            with col:
                st.markdown(f"[{project_name}]({project_link})")
                st.write(project_desc)

    st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")

# --- CERTIFICATIONS & ACCOMPLISHMENTS ---
st.subheader("Certifications & Accomplishments")

cert_cols = st.columns(len(certificates))
for idx, cert in enumerate(certificates):
    with cert_cols[idx]:
        if cert["img_path"].exists():
            img_base64 = file_to_base64(cert["img_path"])
            st.markdown(
                f"""
                <div class="cert-box">
                    <img src="data:image/png;base64,{img_base64}" class="cert-img"/>
                    <div class="cert-title">{cert['name']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.markdown("---")

# --- CONTACT FORM ---
st.header("Contact Me")

with st.form(key="contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit_button = st.form_submit_button("Send")

if submit_button:
    if not name or not email or not message:
        st.error("Please fill out all the fields before submitting.")
    else:
        st.success("Thank you for reaching out! I'll get back to you soon.")
