import streamlit as st

from sections.header import show_header
from sections.experience import show_experience
from sections.skills import show_skills
from sections.work_history import show_work_history
from sections.projects import show_projects
from sections.certificates import show_certificates
from sections.contacts import show_contact_form

st.set_page_config(page_title="Digital CV | Nikhil Gupta", page_icon=":wave:", layout="wide")

def load_css(file_path):
    with open(file_path, "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css("styles/main.css") 

def main():

    show_header()
    show_experience()
    show_skills()
    show_work_history()
    show_projects()
    show_certificates()
    show_contact_form()

if __name__ == "__main__":
    main()