import customtkinter as ctk
from tkinter import messagebox
from src.config.settings import COLORS, FONT_SETTINGS

class AddProductFrame(ctk.CTkFrame):
    """View component for adding new products"""
    
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, fg_color=COLORS["bg_light"], **kwargs)
        
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup the add product form UI"""
        # Product name entry
        self.entry_name = ctk.CTkEntry(
            self, 
            placeholder_text="Product Name", 
            width=250, 
            height=50, 
            font=FONT_SETTINGS
        )
        self.entry_name.grid(row=0, column=0, padx=10)
        
        # Value entry
        self.entry_value = ctk.CTkEntry(
            self, 
            placeholder_text="Value (Optional)", 
            width=250, 
            height=50, 
            font=FONT_SETTINGS
        )
        self.entry_value.grid(row=0, column=1, padx=10)
        
        # Quantity entry
        self.entry_quantity = ctk.CTkEntry(
            self, 
            placeholder_text="Quantity", 
            width=250, 
            height=50, 
            font=FONT_SETTINGS
        )
        self.entry_quantity.grid(row=0, column=2, padx=10)
        
        # Add button
        add_btn = ctk.CTkButton(
            self, 
            text="Add Product", 
            command=self._add_product,
            fg_color=COLORS["button_primary"],
            text_color=COLORS["button_text"], 
            width=200, 
            height=50, 
            font=FONT_SETTINGS
        )
        add_btn.grid(row=0, column=3, padx=10)
    
    def _add_product(self):
        """Handle add product action"""
        name = self.entry_name.get().strip()
        value = self.entry_value.get().strip() or "0"
        quantity = self.entry_quantity.get().strip()
        
        if not name or not quantity:
            messagebox.showwarning("Warning", "Product name and quantity are required!")
            return
        
        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showwarning("Warning", "Quantity must be a number!")
            return
        
        if self.controller.add_product(name, quantity, value):
            self._clear_entries()
        else:
            messagebox.showwarning("Warning", "Product already exists or invalid input!")
    
    def _clear_entries(self):
        """Clear all entry fields"""
        self.entry_name.delete(0, ctk.END)
        self.entry_value.delete(0, ctk.END)
        self.entry_quantity.delete(0, ctk.END)