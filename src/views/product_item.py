import customtkinter as ctk
from src.config.settings import COLORS, FONT_SETTINGS

class ProductItem(ctk.CTkFrame):
    """View component for displaying a single product item"""
    
    def __init__(self, parent, product_name: str, product_data, controller, **kwargs):
        super().__init__(parent, fg_color=COLORS["bg_light"], corner_radius=10, **kwargs)
        
        self.product_name = product_name
        self.product_data = product_data
        self.controller = controller
        
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup the product item UI"""
        # Configure grid
        self.columnconfigure(0, weight=1)  # Name
        self.columnconfigure(1, weight=0)  # Value
        self.columnconfigure(2, weight=0)  # Buttons
        
        # Product name
        name_label = ctk.CTkLabel(
            self,
            text=self.product_name,
            anchor="w",
            text_color=COLORS["text_primary"],
            font=FONT_SETTINGS
        )
        name_label.grid(row=0, column=0, padx=(150, 10), pady=20, sticky="w")
        
        # Value label
        value_label = ctk.CTkLabel(
            self,
            text=f"Value: {self.product_data.value}",
            anchor="e",
            text_color=COLORS["text_primary"],
            font=FONT_SETTINGS
        )
        value_label.grid(row=0, column=1, padx=(10, 1000), pady=20, sticky="e")
        
        # Buttons frame
        btn_frame = ctk.CTkFrame(self, fg_color=COLORS["bg_light"])
        btn_frame.grid(row=0, column=2, padx=90, pady=10, sticky="e")
        
        # Add button
        add_button = ctk.CTkButton(
            btn_frame, 
            text="+", 
            width=50, 
            height=50,
            command=lambda: self.controller.update_quantity(self.product_name, 1),
            fg_color=COLORS["button_primary"], 
            text_color=COLORS["button_text"], 
            font=FONT_SETTINGS
        )
        add_button.pack(side="left", padx=10)
        
        # Quantity label
        self.quantity_label = ctk.CTkLabel(
            btn_frame,
            text=str(self.product_data.quantity),
            text_color=COLORS["text_primary"],
            font=FONT_SETTINGS,
            width=50,
            anchor="center"
        )
        self.quantity_label.pack(side="left", padx=5)
        
        # Minus button
        minus_button = ctk.CTkButton(
            btn_frame, 
            text="-", 
            width=50, 
            height=50,
            command=lambda: self.controller.update_quantity(self.product_name, -1),
            fg_color=COLORS["button_primary"], 
            text_color=COLORS["button_text"], 
            font=FONT_SETTINGS
        )
        minus_button.pack(side="left", padx=10)
        
        # Delete button
        delete_btn = ctk.CTkButton(
            btn_frame, 
            text="Delete", 
            width=80, 
            height=40,
            command=lambda: self.controller.delete_product(self.product_name),
            fg_color=COLORS["button_danger"], 
            text_color=COLORS["button_text"], 
            font=FONT_SETTINGS
        )
        delete_btn.pack(side="left", padx=25)
    
    def update_quantity_display(self, new_quantity: int):
        """Update the quantity display"""
        self.quantity_label.configure(text=str(new_quantity))