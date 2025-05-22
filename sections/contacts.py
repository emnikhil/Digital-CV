import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def show_contact_form():
    try:
        EMAIL_ADDRESS = st.secrets["email"]["address"]
        EMAIL_PASSWORD = st.secrets["email"]["password"]
    except KeyError:
        st.warning("Contact form is disabled. Email credentials are not configured.")
        return

    st.header("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")

        if submitted:
            try:
                send_email(name, email, message, EMAIL_ADDRESS, EMAIL_PASSWORD)
                st.success("Thanks! Your message has been sent.")
            except Exception as e:
                st.error(f"Failed to send message. Error: {e}")

def send_email(name, sender_email, message_body, EMAIL_ADDRESS, EMAIL_PASSWORD):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg["Subject"] = f"New Contact Message from {name}"

    msg.attach(MIMEText(f"From: {name} <{sender_email}>\n\n{message_body}", "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)