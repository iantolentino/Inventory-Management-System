from datetime import datetime
from typing import Optional

class Product:
    """Enhanced product model with additional fields"""
    
    def __init__(self, name: str, quantity: int, value: str = "0", 
                 category: str = "Uncategorized", description: str = "",
                 min_stock: int = 0, max_stock: Optional[int] = None):
        self.name = name
        self.quantity = quantity
        self.value = value
        self.category = category
        self.description = description
        self.min_stock = min_stock
        self.max_stock = max_stock
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        self.sku = self._generate_sku()
    
    def _generate_sku(self) -> str:
        """Generate a unique SKU for the product"""
        import hashlib
        unique_string = f"{self.name}{datetime.now().timestamp()}"
        return hashlib.md5(unique_string.encode()).hexdigest()[:8].upper()
    
    def to_dict(self) -> dict:
        """Convert product to dictionary for JSON storage"""
        return {
            "name": self.name,
            "quantity": self.quantity,
            "value": self.value,
            "category": self.category,
            "description": self.description,
            "min_stock": self.min_stock,
            "max_stock": self.max_stock,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "sku": self.sku
        }
    
    @classmethod
    def from_dict(cls, name: str, data: dict):
        """Create product from dictionary data"""
        product = cls(
            name=name,
            quantity=data.get("quantity", 0),
            value=data.get("value", "0"),
            category=data.get("category", "Uncategorized"),
            description=data.get("description", ""),
            min_stock=data.get("min_stock", 0),
            max_stock=data.get("max_stock")
        )
        product.created_at = data.get("created_at", datetime.now().isoformat())
        product.updated_at = data.get("updated_at", datetime.now().isoformat())
        product.sku = data.get("sku", product._generate_sku())
        return product
    
    def update_quantity(self, delta: int) -> bool:
        """Update product quantity with bounds checking"""
        new_quantity = max(0, self.quantity + delta)
        
        # Check if new quantity violates min/max stock
        if self.min_stock and new_quantity < self.min_stock:
            return False
        if self.max_stock and new_quantity > self.max_stock:
            return False
        
        self.quantity = new_quantity
        self.updated_at = datetime.now().isoformat()
        return True
    
    def is_low_stock(self) -> bool:
        """Check if product is low on stock"""
        return self.min_stock > 0 and self.quantity <= self.min_stock
    
    def is_overstocked(self) -> bool:
        """Check if product is overstocked"""
        return self.max_stock and self.quantity >= self.max_stock
    
    def get_stock_status(self) -> str:
        """Get stock status string"""
        if self.is_low_stock():
            return "Low Stock"
        elif self.is_overstocked():
            return "Overstocked"
        elif self.quantity == 0:
            return "Out of Stock"
        else:
            return "In Stock"
    
    def get_status_color(self) -> str:
        """Get status color based on stock level"""
        if self.is_low_stock() or self.quantity == 0:
            return "#E74C3C"  # Red
        elif self.is_overstocked():
            return "#F39C12"  # Orange
        else:
            return "#27AE60"  # Green