import streamlit as st
from helpers import file_to_base64
from config import PROJECTS, PROJECT_MEDIA, PROJECT_DESCRIPTIONS

def show_projects():
    st.subheader("Projects")

    projects_per_row = 3
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
            project_media_path = PROJECT_MEDIA.get(project_name)
            project_desc = PROJECT_DESCRIPTIONS.get(project_name, "")

            if project_media_path and project_media_path.exists():
                media_base64 = file_to_base64(project_media_path)
                media_extension = project_media_path.suffix.lower()
                mime_type = "gif" if media_extension == ".gif" else "png"

                if media_base64.startswith("data:image"):
                    media_base64 = media_base64.split(",")[1]

                with col:
                    st.markdown(
                        f"""
                        <a href="{project_link}" target="_blank" style="text-decoration:none; color:black; display:inline-block;">
                            <div class="project-card" style="margin:0;">
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
                    st.markdown(
                        f"""
                        <a href="{project_link}" target="_blank" style="text-decoration:none; color:black; display:inline-block;">
                            <div class="project-card no-image-card" style="margin:0;">
                                <p class="project-title">{project_name}</p>
                                <p class="project-desc">{project_desc}</p>
                            </div>
                        </a>
                        """,
                        unsafe_allow_html=True,
                    )

        st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")