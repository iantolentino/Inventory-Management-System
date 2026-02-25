from typing import Dict, Optional
from src.models.product import Product
from src.utils.file_handler import FileHandler
from src.config.settings import INVENTORY_FILE

class InventoryController:
    """Controller managing inventory operations"""
    
    def __init__(self):
        self.file_handler = FileHandler()
        self.products: Dict[str, Product] = {}
        self.view = None
        self.load_products()
    
    def set_view(self, view):
        """Set the view to update when data changes"""
        self.view = view
    
    def load_products(self):
        """Load products from file"""
        data = self.file_handler.load_inventory(INVENTORY_FILE)
        self.products = {
            name: Product.from_dict(name, product_data)
            for name, product_data in data.items()
        }
    
    def save_products(self):
        """Save products to file"""
        data = {
            name: product.to_dict()
            for name, product in self.products.items()
        }
        self.file_handler.save_inventory(INVENTORY_FILE, data)
    
    def add_product(self, name: str, quantity: int, value: str = "0") -> bool:
        """Add a new product"""
        if not name or not quantity:
            return False
        
        if name in self.products:
            return False
        
        self.products[name] = Product(name, quantity, value)
        self.save_products()
        self._notify_view()
        return True
    
    def update_quantity(self, name: str, delta: int):
        """Update product quantity"""
        if name in self.products:
            self.products[name].update_quantity(delta)
            self.save_products()
            self._notify_view()
    
    def delete_product(self, name: str):
        """Delete a product"""
        if name in self.products:
            del self.products[name]
            self.save_products()
            self._notify_view()
    
    def get_all_products(self) -> Dict[str, Product]:
        """Get all products"""
        return self.products
    
    def _notify_view(self):
        """Notify view to update display"""
        if self.view:
            self.view.refresh_display()