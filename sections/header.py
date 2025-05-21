import streamlit as st
from PIL import Image
from config import PROFILE_PIC_PATH, RESUME_PATH, SOCIAL_MEDIA, NAME, DESCRIPTION, EMAIL, MOBILE
from helpers import load_css
from pathlib import Path

def show_header():
    current_dir = Path(__file__).parent.parent
    profile_pic = Image.open(PROFILE_PIC_PATH)

    with open(RESUME_PATH, "rb") as f:
        resume_bytes = f.read()

    css_file = current_dir / "styles" / "main.css"
    st.markdown(load_css(css_file), unsafe_allow_html=True)

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
            file_name=RESUME_PATH.name,
            mime="application/pdf",
        )
        cols = st.columns(len(SOCIAL_MEDIA))
        for idx, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            cols[idx].markdown(f"[{platform}]({link})")

    st.markdown("---")