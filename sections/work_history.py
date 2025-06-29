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
        "Jan' 2025 – Present",
        """
        - Optimized large-scale pipelines on **BigQuery** and improved staging logic with **Airflow-based orchestration** 
          for real-time and batch analytics across departments.

        - Built an internal **Architecture Visualization Tool** using **Python**, **GitHub APIs**, and **MermaidJS**, 
          simplifying legacy codebase discovery for tech and business teams.

        - Designed interactive dashboards in **React.js** backed by GCP to visualize market insights, healthcare trends, 
          and campaign performance across US regions.

        - Developed automated reporting using **BigQuery procedures**, **Python scripts**, and ML models to analyze 
          multi-channel engagement and recommend optimal healthcare plans.

        - Partnered with Data Science, Engineering, and Analytics teams to align cloud usage with budgets, improving 
          resource efficiency, decision-making, and KPI tracking.
        """
    )

    work_entry(
        accenture_logo,
        "Accenture, India | Data Engineer",
        "Jan' 2022 – Jan' 2025",
        """
        - Migrated multi-source data (MySQL, Oracle, JSON, CSV) from on-prem to GCP using **Spark (Scala)** on 
          **Dataproc**, with **Hive** for data warehousing.

        - Built ETL pipelines landing in **GCP Coldline Storage**, transforming and archiving data for traceability 
          and rollback support in high-volume environments.

        - Orchestrated and tuned DAGs in **Apache Airflow**, improving reliability and reducing pipeline errors and latency.

        - Optimized **Spark** jobs for memory use, caching, and parallelism, cutting execution time and cloud costs 
          while improving pipeline robustness.

        - Modernized reporting by migrating **Spark/Presto** jobs to **BigQuery**, and developed stored procedures to 
          analyze retail user behavior, inventory, and shipments.
        """
    )

    work_entry(
        kmitl_logo,
        "KMITL, Thailand | Research Intern",
        "Sept' 19 – Oct' 19",
        """
        - Built a **CNN-based classification model** for beef steak fat grading in collaboration with the **Thailand 
          Department of Livestock**, using real-time image data.

        - Employed **Python**, **OpenCV**, and **MATLAB** for image segmentation and enhancement, ensuring quality inputs 
          for accurate prediction.

        - Designed an end-to-end preprocessing pipeline for feature extraction, boosting classification precision 
          on raw image datasets.

        - Achieved **92% accuracy**, aligning output with national food safety grading standards and validating 
          model performance with stakeholders.

        - The research demonstrated practical use of AI in agriculture, with potential for adoption in Thailand’s 
          food quality assurance systems.
        """
    )

    st.markdown("---")
