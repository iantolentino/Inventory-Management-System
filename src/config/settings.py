import os
from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).parent.parent.parent
DATA_DIR = os.path.join(BASE_DIR, "data")
INVENTORY_FILE = os.path.join(DATA_DIR, "inventory.json")

# UI Settings
APP_TITLE = "Inventory Management System"
FONT_FAMILY = "Arial"
FONT_SIZE = 24
FONT_SETTINGS = (FONT_FAMILY, FONT_SIZE)

# Colors
COLORS = {
    "bg_light": "#FFFFFF",
    "bg_dark": "#F0F0F0",
    "text_primary": "#000000",
    "button_primary": "#000000",
    "button_danger": "#FF0000",
    "button_text": "#FFFFFF"
}

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)