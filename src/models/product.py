class Product:
    """Product model representing an inventory item"""
    
    def __init__(self, name: str, quantity: int, value: str = "0"):
        self.name = name
        self.quantity = quantity
        self.value = value
    
    def to_dict(self) -> dict:
        """Convert product to dictionary for JSON storage"""
        return {
            "name": self.name,
            "quantity": self.quantity,
            "value": self.value
        }
    
    @classmethod
    def from_dict(cls, name: str, data: dict):
        """Create product from dictionary data"""
        return cls(
            name=name,
            quantity=data.get("quantity", 0),
            value=data.get("value", "0")
        )
    
    def update_quantity(self, delta: int):
        """Update product quantity with bounds checking"""
        self.quantity = max(0, self.quantity + delta)