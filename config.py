from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

PROFILE_PIC_PATH = current_dir / "assets" / "photos" / "profile.png"
RESUME_PATH = current_dir / "assets" / "Resume(Nikhil Gupta).pdf"

EXL_LOGO_PATH = current_dir / "assets" / "photos" / "EXL_Service_logo.png"
ACCENTURE_LOGO_PATH = current_dir / "assets" / "photos" / "Accenture_logo.png"
KMITL_LOGO_PATH = current_dir / "assets" / "photos" / "KMITL_logo.png"

PROJECT_MEDIA = {
    "Sign Language to Text Conversion": current_dir / "assets" / "photos" / "sign_language.png",
    "Crypto Data Pipeline": current_dir / "assets" / "photos" / "crypto_data_pipeline.png",
    "ArchitectureGen": current_dir / "assets" / "photos" / "ArchitectureGen.png"
}

PROJECT_DESCRIPTIONS = {
    "Sign Language to Text Conversion": "Real-time system using CNN-based computer vision to convert sign language gestures into text for hearing and speaking impaired.",
    "Crypto Data Pipeline": "An end-to-end data pipeline for cryptocurrency market data ingestion, processing, and visualization using cloud tools.",
    "ArchitectureGen": "Automated project architecture visualization tool using Python and MermaidJS for GitHub repos."
}

CERTIFICATES = [
    {
        "name": "Databricks Certified Data Engineer Associate",
        "img_path": current_dir / "assets" / "photos" /"Databricks_Certificate.png"
    },
    {
        "name": "ACE: Growth Catalyst Award - (FY22 Q4)",
        "img_path": current_dir / "assets" / "photos" / "Ace_Award.png"
    },
    {
        "name": "Internationl Exchange Program",
        "img_path": current_dir / "assets" / "photos" / "internship.png"
    }
]

PAGE_TITLE = "Digital CV | Nikhil Gupta"
PAGE_ICON = ":wave:"
NAME = "Nikhil Gupta"
DESCRIPTION = "Data Engineering Consultant with a strong foundation in big data ecosystems, cloud infrastructure (GCP), and scalable pipeline automation. Passionate about building end-to-end data solutions that power advanced analytics and real-world AI applications."
EMAIL = "emnikkhil@gmail.com"
MOBILE = "+91-9858463809"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/guptanikhil1/",
    "GitHub": "https://github.com/emnikhil"
}

PROJECTS = {
    "Sign Language to Text Conversion": "https://github.com/emnikhil/Sign-Language-To-Text-Conversion",
    "Crypto Data Pipeline": "https://github.com/emnikhil/Crypto-Data-Pipeline",
    "ArchitectureGen": "https://github.com/emnikhil/ArchitectureGen"
}