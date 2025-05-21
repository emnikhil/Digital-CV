# Digital CV

This is a personal digital resume and portfolio web app built using Streamlit. It showcases skills, experience, projects, certificates, and includes a contact form to reach out directly via email.

---

## Features

- Clean, responsive design with dark mode support
- Sections for Experience, Skills, Work History, Projects, Certificates
- Contact form with email sending functionality
- Easy to customize and extend

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager
- streamilt : ```pip install streamlit```

### Steps to Use

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
```
2. **Replace assets and photos**
   
Update the images and certificates inside the assets/ folder with your own images and files.

3. **Update your details**
   
Modify the Python files inside the ```sections/ directory``` to update your personal information, skills, experience, projects, and certificates.
Update ```config.py``` with your project and certificate details.

4. **Steps to implement email sending with your contact form:**

Setup: Allow Gmail SMTP access
   
Use a Gmail account to send emails.
  
Create an App Password (recommended) if you have 2FA enabled on your Google account:
  
```https://support.google.com/accounts/answer/185833```
  
Or allow "Less secure app access" (not recommended).

5. **Configure email for contact form**
   
Create or update the ```.streamlit/secrets.toml``` file (or use the existing one) with your email credentials for the contact form to function correctly.

```
[email]
address = "your.email@example.com"
password = "your_email_password"
```

6. **Run the app on local**

```
python3 -u portfolio/app.py
python3 -m streamlit run app.py
```

7. **Open in your browser**
   
Visit ```http://localhost:8501``` (or the URL Streamlit provides) to see your digital CV in action.

# Project Structure
```
Portfolio/
├── assets/
│   ├── Resume.pdf              # Resume file (PDF)
│   ├── photos/                 # Folder containing portfolio photos (png/jpg)
│   │   ├── photo1.png
│   │   ├── photo2.jpg
│   │   └── ...                 
│
├── .gitignore                 # Git ignore file (includes .streamlit/ and other ignores)
├── app.py                     # Main Streamlit application file
├── config.py                  # Constants, paths, social links, settings
├── helpers.py                 # Helper functions (base64, css loader, etc.)
├── sections/                  # Modular UI sections
│   ├── header.py              # Header section
│   ├── experience.py          # Experience & qualifications
│   ├── skills.py              # Technical skills section
│   ├── work_history.py        # Work history entries
│   ├── projects.py            # Projects section
│   ├── certificates.py        # Certificates & accomplishments
│   └── contact.py             # Contact form logic
├── styles/                    # CSS files for custom styling
│   └── main.css
└── README.md                  # Project README
├── .streamlit/
│   └── secrets.toml           # Streamlit secrets file (for sensitive info, gitignored)
```
