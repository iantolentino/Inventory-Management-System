from typing import Dict, Optional
from src.models.product import Product
from src.utils.file_handler import FileHandler
from src.config.settings import INVENTORY_FILE

class InventoryController:
    """Enhanced controller managing inventory operations"""
    
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
    
    def add_product(self, name: str, quantity: int, value: str = "0",
                   category: str = "Uncategorized", description: str = "",
                   min_stock: int = 0, max_stock: Optional[int] = None) -> bool:
        """Add a new product"""
        if not name or name in self.products:
            return False
        
        self.products[name] = Product(
            name=name,
            quantity=quantity,
            value=value,
            category=category,
            description=description,
            min_stock=min_stock,
            max_stock=max_stock
        )
        self.save_products()
        self._notify_view()
        return True
    
    def update_quantity(self, name: str, delta: int) -> bool:
        """Update product quantity"""
        if name in self.products:
            success = self.products[name].update_quantity(delta)
            if success:
                self.save_products()
                self._notify_view()
            return success
        return False
    
    def delete_product(self, name: str):
        """Delete a product"""
        if name in self.products:
            del self.products[name]
            self.save_products()
            self._notify_view()
    
    def get_all_products(self) -> Dict[str, Product]:
        """Get all products"""
        return self.products
    
    def get_product(self, name: str) -> Optional[Product]:
        """Get a specific product"""
        return self.products.get(name)
    
    def get_low_stock_products(self) -> Dict[str, Product]:
        """Get products with low stock"""
        return {
            name: product
            for name, product in self.products.items()
            if product.is_low_stock()
        }
    
    def get_out_of_stock_products(self) -> Dict[str, Product]:
        """Get out of stock products"""
        return {
            name: product
            for name, product in self.products.items()
            if product.quantity == 0
        }
    
    def get_total_value(self) -> float:
        """Calculate total inventory value"""
        total = 0
        for product in self.products.values():
            try:
                value = float(product.value) if product.value else 0
                total += value * product.quantity
            except ValueError:
                pass
        return total
    
    def _notify_view(self):
        """Notify view to update display"""
        if self.view:
            self.view.refresh_display()