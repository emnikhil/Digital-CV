# Portfolio
Streamlit based Digital Resume/Portfolio

# Project Structure
```
Portfolio/
├── assets/
│   ├── Resume.pdf              # Resume file (PDF)
│   ├── photos/                 # Folder containing portfolio photos (png/jpg)
│   │   ├── photo1.png
│   │   ├── photo2.jpg
│   │   └── ...                 
│   └── .streamlit/
│       └── secrets.toml       # Streamlit secrets file (for sensitive info, gitignored)
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
```
