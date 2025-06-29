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
        - Spearheaded the optimization of large-scale data pipelines on **BigQuery**, enhancing data staging logic and 
        integrating **Airflow-based orchestration** to support real-time and scheduled analytics across business domains.

        - Developed a scalable internal **Architecture Visualization Tool** using **Python**, **GitHub APIs**, and **MermaidJS**, 
        enabling organization-wide understanding of legacy codebases and improving cross-functional onboarding and audits.

        - Collaborated with business stakeholders to design and deploy **interactive market research dashboards** using **React.js** 
        and GCP services, delivering deep insights into US healthcare trends, user demographics, and campaign outreach zones.

        - Led the development of **cloud-native reporting frameworks** using **BigQuery procedures**, **SQL automation**, and 
        **Python scripts**, tracking multi-channel user engagement across email, SMS, and postal campaigns.

        - Integrated **machine learning models** to analyze campaign responses and user behavior, enabling predictive targeting 
        for healthcare plan recommendations and boosting marketing efficiency at scale.

        - Worked closely with Data Science, Engineering, and Analytics teams to align cloud resource utilization with budgetary 
        goals, driving cost-effective solutions and improving project efficiency metrics across the data lifecycle.

        - Delivered business impact by enabling leadership to make data-driven decisions through automated reporting, ML-based 
        insights, and unified views of operational KPIs across campaigns, teams, and customer segments.
        """
    )

    work_entry(
        accenture_logo,
        "Accenture, India | Data Engineer",
        "Jan' 2022 - Jan' 2025",
        """
        - Played a key role in an enterprise-scale **on-prem to GCP migration**, moving multi-source data from **MySQL**, 
        **Oracle**, **raw JSON**, and **CSV** formats to the cloud, using **Apache Spark** and **Scala** on **Dataproc** 
        clusters for processing, and **Hive** for data warehousing.

        - Built robust **ETL pipelines** where data landed in GCP **Coldline Storage**, then transformed and archived to 
        **Geo-redundant storage**, ensuring traceability, rollback capabilities, and long-term reliability.

        - Orchestrated all pipeline workflows using **Apache Airflow**, writing modular DAGs and optimizing them for 
        job dependencies and scheduling, significantly improving reliability and reducing execution errors.

        - Tuned **Spark jobs** for performance on Dataproc clusters by managing memory configurations, caching strategies, 
        and job parallelism—resulting in faster execution, reduced compute costs, and more resilient pipelines.

        - Led automation efforts in a cloud data warehouse modernization project, eliminating manual handoffs, 
        implementing **data integrity checks**, and improving platform availability and trust in analytics delivery.

        - Migrated legacy **Spark** and **Presto** jobs to **BigQuery** procedures, modernizing stakeholder dashboards 
        and enabling faster, cost-efficient reporting with seamless integration into visualization layers.

        - Designed and deployed **stored procedures** to track **retail user activity**, orders, shipments, and 
        offline store inventory, enabling real-time insights into consumer behavior, product movement, and cost flows.
        """
    )

    work_entry(
        kmitl_logo,
        "KMITL, Thailand | Research Intern",
        "Sept' 19 - Oct' 19",
        """
        - Collaborated with the **Thailand Department of Livestock** on a research project to automate the grading of 
        beef steak quality using image-based classification aligned with national food safety and livestock standards.

        - Designed and developed a **Convolutional Neural Network (CNN)** model integrated with **image preprocessing pipelines** 
        to classify steak based on visible fat content using real-time image inputs.

        - Employed tools like **Python**, **OpenCV**, and **MATLAB** for image segmentation, enhancement, and model prototyping, 
        ensuring clean inputs and improving classification accuracy.

        - Trained the model on raw image datasets provided by the department, applying iterative preprocessing techniques to 
        enhance feature extraction and model precision.

        - Achieved **92% classification accuracy**, contributing to the potential adoption of AI-driven meat grading tools 
        in Thailand’s livestock and food quality assurance ecosystem.
        """
    )
    
    st.markdown("---")