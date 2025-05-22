import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def show_contact_form():
    st.header("📬 Contact Me")

    try:
        EMAIL_ADDRESS = st.secrets["email"]["address"]
        EMAIL_PASSWORD = st.secrets["email"]["password"]
    except KeyError:
        st.warning("⚠️ Contact form is disabled. Email credentials are not configured in `secrets.toml`.")
        return

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name", max_chars=50)
        email = st.text_input("Your Email", max_chars=50)
        message = st.text_area("Your Message", max_chars=1000)
        submitted = st.form_submit_button("Send Message")

        if submitted:
            if not name or not email or not message:
                st.error("Please fill out all fields before submitting.")
            elif "@" not in email or "." not in email:
                st.error("Please enter a valid email address.")
            else:
                try:
                    send_email(name, email, message, EMAIL_ADDRESS, EMAIL_PASSWORD)
                    st.success("✅ Your message has been sent successfully!")
                except Exception as e:
                    st.error(f"❌ Failed to send message. Error: {e}")

def send_email(name, sender_email, message_body, EMAIL_ADDRESS, EMAIL_PASSWORD):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg["Subject"] = f"New Contact Message from {name}"

    body = f"""
    You have received a new message via your portfolio contact form.

    Name: {name}
    Email: {sender_email}
    Message:
    {message_body}
    """

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)