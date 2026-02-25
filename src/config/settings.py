import os
from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).parent.parent.parent
DATA_DIR = os.path.join(BASE_DIR, "data")
INVENTORY_FILE = os.path.join(DATA_DIR, "inventory.json")
ASSETS_DIR = os.path.join(BASE_DIR, "src", "assets")

# UI Settings
APP_TITLE = "Inventory Management System"
APP_GEOMETRY = "1400x900"
FONT_FAMILY = "Segoe UI"  # or "Arial" as fallback

# Colors
COLORS = {
    "bg_primary": "#F5F7FA",
    "bg_secondary": "#FFFFFF",
    "bg_dark": "#2C3E50",
    "text_primary": "#2C3E50",
    "text_secondary": "#7F8C8D",
    "text_light": "#FFFFFF",
    "accent": "#3498DB",
    "accent_hover": "#2980B9",
    "success": "#27AE60",
    "warning": "#F39C12",
    "danger": "#E74C3C"
}

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)