import streamlit as st
from config import CERTIFICATES
from helpers import get_base64_encoded_image 

def show_certificates():
    st.subheader("Certificates & Awards")

    cols = st.columns(len(CERTIFICATES))

    for idx, cert in enumerate(CERTIFICATES):
        encoded_img = get_base64_encoded_image(cert["img_path"])
        html = f"""
        <div class="cert-box">
            <img src="data:image/png;base64,{encoded_img}" class="cert-img" />
            <div class="cert-title">{cert["name"]}</div>
        </div>
        """
        cols[idx].markdown(html, unsafe_allow_html=True)

    st.markdown("---")