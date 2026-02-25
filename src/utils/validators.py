import re
from typing import Tuple, Optional

class Validators:
    """Input validation utilities"""
    
    @staticmethod
    def validate_product_name(name: str) -> Tuple[bool, Optional[str]]:
        """Validate product name"""
        if not name or not name.strip():
            return False, "Product name is required"
        if len(name) > 100:
            return False, "Product name must be less than 100 characters"
        if not re.match(r'^[a-zA-Z0-9\s\-_]+$', name):
            return False, "Product name can only contain letters, numbers, spaces, hyphens and underscores"
        return True, None
    
    @staticmethod
    def validate_quantity(quantity: str) -> Tuple[bool, Optional[str], Optional[int]]:
        """Validate quantity input"""
        if not quantity or not quantity.strip():
            return False, "Quantity is required", None
        
        try:
            qty = int(quantity)
            if qty < 0:
                return False, "Quantity must be a positive number", None
            if qty > 999999:
                return False, "Quantity exceeds maximum limit", None
            return True, None, qty
        except ValueError:
            return False, "Quantity must be a valid number", None
    
    @staticmethod
    def validate_value(value: str) -> Tuple[bool, Optional[str], Optional[str]]:
        """Validate value/price input"""
        if not value or not value.strip():
            return True, None, "0"
        
        try:
            # Remove currency symbols and commas
            cleaned = re.sub(r'[$,]', '', value)
            float_val = float(cleaned)
            if float_val < 0:
                return False, "Value must be a positive number", None
            if float_val > 999999.99:
                return False, "Value exceeds maximum limit", None
            return True, None, f"{float_val:.2f}"
        except ValueError:
            return False, "Value must be a valid number", None
    
    @staticmethod
    def validate_category(category: str) -> Tuple[bool, Optional[str]]:
        """Validate category"""
        if category and len(category) > 50:
            return False, "Category must be less than 50 characters"
        return True, None
    
    @staticmethod
    def validate_description(description: str) -> Tuple[bool, Optional[str]]:
        """Validate description"""
        if description and len(description) > 500:
            return False, "Description must be less than 500 characters"
        return True, None