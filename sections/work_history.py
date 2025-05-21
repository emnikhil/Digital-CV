import streamlit as st
from PIL import Image
from config import EXL_LOGO_PATH, ACCENTURE_LOGO_PATH, KMITL_LOGO_PATH

def work_entry(logo: Image.Image, company: str, role_dates: str, description: str):
    col_logo, col_text = st.columns([1, 8], gap="small")
    with col_logo:
        st.image(logo, width=80)
    with col_text:
        st.markdown(f"**{company}**  \n*{role_dates}*")
        st.write(description)

def show_work_history():
    exl_logo = Image.open(EXL_LOGO_PATH)
    accenture_logo = Image.open(ACCENTURE_LOGO_PATH)
    kmitl_logo = Image.open(KMITL_LOGO_PATH)

    st.subheader("Work History")

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