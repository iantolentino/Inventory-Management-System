import customtkinter as ctk
from src.assets.styles import AppStyles

class StatisticsPanel(ctk.CTkFrame):
    """Compact statistics dashboard panel"""
    
    def __init__(self, parent, controller, **kwargs):
        super().__init__(
            parent,
            fg_color=AppStyles.WHITE,
            corner_radius=AppStyles.RADIUS_MD,
            **kwargs
        )
        
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        # Configure grid for 4 columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        
        # Stat cards in a single row
        self.total_products_card = self._create_stat_card("Total", "0", AppStyles.PRIMARY, 0)
        self.low_stock_card = self._create_stat_card("Low Stock", "0", AppStyles.WARNING, 1)
        self.out_of_stock_card = self._create_stat_card("Out of Stock", "0", AppStyles.DANGER, 2)
        self.total_value_card = self._create_stat_card("Total Value", "$0", AppStyles.SUCCESS, 3)
    
    def _create_stat_card(self, title, value, color, column):
        """Create a compact statistics card"""
        card = ctk.CTkFrame(
            self,
            fg_color="transparent",
            height=80
        )
        card.grid(row=0, column=column, padx=5, pady=10, sticky="nsew")
        
        # Value (large)
        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Segoe UI", 20, "bold"),
            text_color=color
        )
        value_label.pack(expand=True)
        
        # Title
        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 12),
            text_color=AppStyles.GRAY
        )
        title_label.pack()
        
        # Store reference to value label
        card.value_label = value_label
        return card
    
    def update_statistics(self, products):
        """Update statistics based on current products"""
        total_products = len(products)
        low_stock = sum(1 for p in products.values() if p.is_low_stock())
        out_of_stock = sum(1 for p in products.values() if p.quantity == 0)
        
        total_value = 0
        for product in products.values():
            try:
                value = float(product.value) if product.value else 0
                total_value += value * product.quantity
            except ValueError:
                pass
        
        self.total_products_card.value_label.configure(text=str(total_products))
        self.low_stock_card.value_label.configure(text=str(low_stock))
        self.out_of_stock_card.value_label.configure(text=str(out_of_stock))
        self.total_value_card.value_label.configure(text=f"${total_value:,.0f}")