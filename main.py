#!/usr/bin/env python3
"""
Inventory Management System
Main entry point for the application
"""

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.app import InventoryApp

def main():
    """Main function to run the application"""
    app = InventoryApp()
    app.run()

if __name__ == "__main__":
    main()