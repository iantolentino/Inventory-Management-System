# Inventory Management System

A modern, feature-rich inventory management application built with Python and CustomTkinter. Perfect for small to medium-sized businesses to track products, manage stock levels, and monitor inventory value.

![Inventory Management System](screenshot.png)

##  Features

### Core Features
- **📊 Dashboard Statistics**: Real-time overview of total products, low stock items, out-of-stock products, and total inventory value
- **🔍 Advanced Search**: Search products by name, category, or SKU
- **🏷️ Categories**: Organize products with custom categories
- **📈 Stock Alerts**: Visual indicators for low stock and overstocked items
- **💾 Persistent Storage**: Automatic JSON file storage with data persistence
- **🎨 Modern UI**: Clean, professional interface with smooth animations

### Product Management
- **➕ Add Products**: Comprehensive product form with validation
- **📝 Product Details**: Track name, SKU, category, description, and value
- **📦 Quantity Control**: Easy increment/decrement buttons
- **⚠️ Stock Limits**: Set minimum and maximum stock levels
- **🗑️ Delete Products**: Remove products with confirmation

### Advanced Features
- **🔎 Real-time Filtering**: Instant search results as you type
- **📱 Touch Support**: Optimized for touchscreen devices
- **⌨️ Keyboard Shortcuts**: Quick access to common functions
- **📋 Sorting**: Sort products by name, quantity, value, or category
- **🎯 Visual Status**: Color-coded stock status indicators

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/inventory-management-system.git
cd inventory-management-system
Install dependencies
```
```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

## 📖 Usage Guide
1. First Time Setup
2. Launch the application
3. The inventory will be empty initially
4. Start adding your products using the form on the left
5. Adding a Product
6. Fill in the required fields:
    - Product Name (required)
    - Quantity (required)
    - Category (optional, defaults to "Uncategorized")
    - Value (optional)
    - Description (optional)
    - Min/Max Stock (optional)
    - Click "Add Product" to save
    - The product will appear in the list on the right

## Managing Products
➕ Increase Stock: Click the "+" button on any product card
➖ Decrease Stock: Click the "-" button
🗑️ Delete: Click the red "Delete" button (confirmation required)
🔍 Search: Type in the search bar to filter products
📊 Sort: Use the dropdown to sort products

## Understanding Status Indicators
🟢 Green: Normal stock level
🟡 Yellow: Low stock (at or below minimum)
🔴 Red: Out of stock
🟠 Orange: Overstocked (at or above maximum)

## Keyboard Shortcuts
- Shortcut	Action
- Ctrl + N	Focus product name field
- Ctrl + F	Focus search bar
- F5	Refresh display
- Esc	Exit application

##🏗️ Project Structure
```bash
inventory-management-system/
│
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── README.md              # Documentation
├── .gitignore             # Git ignore file
│
├── src/                    # Source code
│   ├── app.py             # Main application class
│   ├── assets/            # Static assets and styles
│   │   └── styles.py      # Centralized styling
│   ├── models/            # Data models
│   │   └── product.py     # Product model
│   ├── views/             # UI components
│   │   ├── main_window.py # Main window
│   │   ├── product_card.py # Product display card
│   │   ├── add_product_panel.py # Add product form
│   │   ├── statistics_panel.py # Statistics dashboard
│   │   └── components/    # Reusable components
│   │       ├── modern_button.py # Styled buttons
│   │       └── search_bar.py    # Search component
│   ├── controllers/        # Business logic
│   │   └── inventory_controller.py
│   ├── utils/             # Utilities
│   │   ├── file_handler.py
│   │   └── validators.py
│   └── config/            # Configuration
│       └── settings.py
│
└── data/                   # Data storage
    └── inventory.json      # Inventory data file
```

## ⚙️ Configuration
### Customizing Colors and Styles
- Edit src/assets/styles.py to modify the color scheme:

```python
class AppStyles:
    PRIMARY = "#2C3E50"      # Change primary color
    SECONDARY = "#3498DB"     # Change secondary color
    SUCCESS = "#27AE60"       # Change success color
    DANGER = "#E74C3C"        # Change danger color
Changing Data Location
Edit src/config/settings.py to change where data is stored:
```
```python
DATA_DIR = os.path.join(BASE_DIR, "custom_data_path")
INVENTORY_FILE = os.path.join(DATA_DIR, "custom_filename.json")
```
## 🔧 Development
- Running Tests
```bash
python -m unittest discover tests
Building Executable
Create a standalone executable:

# Install pyinstaller
```bash
pip install pyinstaller
```
# Build executable
```bash
pyinstaller --onefile --windowed --name "InventoryPro" main.py
```
# The executable will be in the 'dist' folder
## 🤝 Contributing
- Fork the repository
- Create a feature branch (git checkout -b feature/AmazingFeature)
- Commit your changes (git commit -m 'Add some AmazingFeature')
- Push to the branch (git push origin feature/AmazingFeature)
- Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add docstrings for new functions
- Update README for significant changes
- Test your changes thoroughly

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments
- Built with CustomTkinter
- Icons and emojis from the Unicode standard

## 📧 Support
- For support, email: iantolentino@gmail.com
- Or open an issue on GitHub Issues

## 📊 Changelog
- Version 1.0.0 (Current)
### Initial release
- Basic CRUD operations
- Modern UI with statistics dashboard
- Search and filter functionality
- Stock level alerts
- Touch support
- Keyboard shortcuts

