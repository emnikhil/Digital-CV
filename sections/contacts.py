import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Access credentials from secrets.toml
EMAIL_ADDRESS = st.secrets["email"]["address"]
EMAIL_PASSWORD = st.secrets["email"]["password"]
RECEIVER_EMAIL = st.secrets["email"].get("receiver", EMAIL_ADDRESS)

def send_email(name, email, message):
    subject = f"New Contact Form Submission from {name}"
    body = f"""
            You have received a new message from your contact form.

            Name: {name}
            Email: {email}
            Message:
            {message}
            """

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

def show_contact_form():
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
            if send_email(name, email, message):
                st.success("Thank you for reaching out! I'll get back to you soon.")
            else:
                st.error("Failed to send your message. Please try again later.")
