# Inventory Management System

A modern, full-screen inventory management application built with Python and CustomTkinter. Perfect for small to medium-sized businesses to track product quantities and values.

## Features

- **Full-Screen Interface**: Optimized for touchscreen devices
- **Product Management**: Add, update, and delete products
- **Quantity Tracking**: Increment/decrement product quantities
- **Persistent Storage**: Automatic JSON file storage
- **Scrollable Interface**: Smooth scrolling for many products
- **Touch-Support**: Works with both mouse and touch input

## Screenshots

[Add screenshots here]

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/inventory-management-system.git
cd inventory-management-system

2. Install dependencies
```bash
pip install -r requirements.txt

3. Run the Application
```bash
python main.py

Usage
Adding a Product
Enter the product name in the "Product Name" field

(Optional) Enter a value/price

Enter the initial quantity

Click "Add Product"

Managing Products
Increase Quantity: Click the "+" button

Decrease Quantity: Click the "-" button

Delete Product: Click the "Delete" button

Scroll: Use mouse wheel or touch to scroll through products

Exiting
Click the "X" button in the top-right corner to exit the application.

Project Structure
text
inventory-management-system/
│
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
│
├── src/                   # Source code
│   ├── app.py            # Main application class
│   ├── models/           # Data models
│   ├── views/            # UI components
│   ├── controllers/       # Business logic
│   ├── utils/            # Utility functions
│   └── config/           # Configuration settings
│
└── data/                  # Data storage
    └── inventory.json     # Inventory data file
Configuration
You can modify the application settings in src/config/settings.py:

Font settings: Change font family and size

Colors: Customize the color scheme

Data location: Change where inventory data is stored

Data Storage
Inventory data is automatically saved to data/inventory.json in JSON format. Each product entry includes:

Name

Quantity

Value (optional)

Development
Running Tests
bash
python -m unittest discover tests
Building Executable
To create a standalone executable:

bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
Contributing
Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Built with CustomTkinter

Inspired by modern inventory management systems

Support
For support, email your-email@example.com or open an issue on GitHub.

Roadmap
Add search functionality

Export to CSV/Excel

Barcode scanning support

Multiple inventory locations

User authentication

Cloud backup integration

Version History
1.0.0 (Current)

Initial release

Basic CRUD operations

Full-screen interface

Touch support

text

This refactored code provides:

1. **Clean Separation of Concerns**: MVC pattern implementation
2. **Modular Structure**: Each component has a single responsibility
3. **Configuration Management**: Centralized settings
4. **Better Error Handling**: Proper exception handling
5. **Maintainability**: Easy to modify and extend
6. **Documentation**: Comprehensive README and code comments

The application will run the same as before but with much better organization and maintainability.