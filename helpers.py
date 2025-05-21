import base64
from io import BytesIO
from PIL import Image
from pathlib import Path

def project_img_to_base64(img: Image.Image) -> str:
    """Convert PIL Image to base64 (for PNG images only)."""
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def file_to_base64(path) -> str:
    """Convert any file (PNG, GIF, etc.) to base64 string."""
    with open(path, "rb") as file:
        data = file.read()
    return base64.b64encode(data).decode()

def get_base64_encoded_image(image_path: Path) -> str:
    with open(image_path, "rb") as img_file:
        data = img_file.read()
    return base64.b64encode(data).decode()


def load_css(file_path) -> str:
    with open(file_path) as f:
        return f"<style>{f.read()}</style>"