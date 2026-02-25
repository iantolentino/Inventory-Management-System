import customtkinter as ctk
from src.assets.styles import AppStyles

class StatisticsPanel(ctk.CTkFrame):
    """Modern statistics dashboard panel"""
    
    def __init__(self, parent, controller, **kwargs):
        super().__init__(
            parent,
            fg_color=AppStyles.WHITE,
            corner_radius=AppStyles.RADIUS_LG,
            **kwargs
        )
        
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        # Title
        title = ctk.CTkLabel(
            self,
            text="Inventory Statistics",
            font=AppStyles.get_font(AppStyles.FONT_LG, "bold"),
            text_color=AppStyles.DARK
        )
        title.pack(anchor="w", padx=20, pady=(20, 15))
        
        # Stats container
        stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        stats_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Configure grid
        stats_frame.grid_columnconfigure(0, weight=1)
        stats_frame.grid_columnconfigure(1, weight=1)
        
        # Stat cards
        self.total_products_card = self._create_stat_card(
            stats_frame, "Total Products", "0", AppStyles.PRIMARY, 0, 0
        )
        self.low_stock_card = self._create_stat_card(
            stats_frame, "Low Stock", "0", AppStyles.WARNING, 0, 1
        )
        self.out_of_stock_card = self._create_stat_card(
            stats_frame, "Out of Stock", "0", AppStyles.DANGER, 1, 0
        )
        self.total_value_card = self._create_stat_card(
            stats_frame, "Total Value", "$0", AppStyles.SUCCESS, 1, 1
        )
    
    def _create_stat_card(self, parent, title, value, color, row, col):
        """Create a statistics card"""
        card = ctk.CTkFrame(
            parent,
            fg_color=AppStyles.LIGHT,
            corner_radius=AppStyles.RADIUS_MD,
            height=100
        )
        card.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        card.grid_propagate(False)
        
        # Title
        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=AppStyles.get_font(AppStyles.FONT_SM),
            text_color=AppStyles.GRAY
        )
        title_label.pack(pady=(15, 5))
        
        # Value
        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=AppStyles.get_font(AppStyles.FONT_XL, "bold"),
            text_color=color
        )
        value_label.pack()
        
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
        self.total_value_card.value_label.configure(text=f"${total_value:,.2f}")