import json
import os
from typing import Dict, Any
from tkinter import messagebox

class FileHandler:
    """Handles file operations for inventory data"""
    
    @staticmethod
    def load_inventory(file_path: str) -> Dict[str, Any]:
        """Load inventory data from JSON file"""
        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Inventory file is corrupted. Starting with empty inventory.")
                return {}
        return {}
    
    @staticmethod
    def save_inventory(file_path: str, data: Dict[str, Any]):
        """Save inventory data to JSON file"""
        try:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save inventory: {str(e)}")