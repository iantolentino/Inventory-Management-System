import customtkinter as ctk
from src.assets.styles import AppStyles
from src.views.components.modern_button import ModernButton

class ProductCard(ctk.CTkFrame):
    """Compact product card component"""
    
    def __init__(self, parent, product, controller, **kwargs):
        super().__init__(
            parent,
            fg_color=AppStyles.WHITE,
            corner_radius=AppStyles.RADIUS_MD,
            border_width=1,
            border_color=AppStyles.LIGHT,
            **kwargs
        )
        
        self.product = product
        self.controller = controller
        
        self._setup_ui()
    
    def _setup_ui(self):
        # Main content
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=12, pady=10)
        
        # Top row: Name, Category, Value
        top_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        top_frame.pack(fill="x", pady=(0, 8))
        
        # Name and category
        name_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
        name_frame.pack(side="left", fill="x", expand=True)
        
        name_label = ctk.CTkLabel(
            name_frame,
            text=self.product.name,
            font=("Segoe UI", 14, "bold"),
            text_color=AppStyles.DARK,
            anchor="w"
        )
        name_label.pack(anchor="w")
        
        # Category badge
        category_badge = ctk.CTkFrame(
            name_frame,
            fg_color=AppStyles.LIGHT,
            corner_radius=12,
            height=20
        )
        category_badge.pack(anchor="w", pady=(2, 0))
        
        category_label = ctk.CTkLabel(
            category_badge,
            text=self.product.category,
            font=("Segoe UI", 10),
            text_color=AppStyles.DARK,
            padx=8
        )
        category_label.pack()
        
        # Value badge (if exists)
        if self.product.value and self.product.value != "0":
            value_badge = ctk.CTkFrame(
                top_frame,
                fg_color=AppStyles.SUCCESS_GRADIENT[0],
                corner_radius=15,
                height=30
            )
            value_badge.pack(side="right")
            
            value_label = ctk.CTkLabel(
                value_badge,
                text=f"${self.product.value}",
                font=("Segoe UI", 13, "bold"),
                text_color=AppStyles.WHITE,
                padx=12
            )
            value_label.pack()
        
        # Stock status indicator
        status_color = self.product.get_status_color()
        status_text = self.product.get_stock_status()
        
        if status_text != "In Stock":
            status_badge = ctk.CTkFrame(
                top_frame,
                fg_color=status_color,
                corner_radius=12,
                height=24
            )
            status_badge.pack(side="right", padx=(0, 8))
            
            status_label = ctk.CTkLabel(
                status_badge,
                text=status_text,
                font=("Segoe UI", 11, "bold"),
                text_color=AppStyles.WHITE,
                padx=10
            )
            status_label.pack()
        
        # Bottom row: Quantity and controls
        bottom_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        bottom_frame.pack(fill="x")
        
        # Quantity
        qty_frame = ctk.CTkFrame(bottom_frame, fg_color="transparent")
        qty_frame.pack(side="left")
        
        qty_label = ctk.CTkLabel(
            qty_frame,
            text="Qty:",
            font=("Segoe UI", 12),
            text_color=AppStyles.GRAY
        )
        qty_label.pack(side="left", padx=(0, 5))
        
        qty_value = ctk.CTkLabel(
            qty_frame,
            text=str(self.product.quantity),
            font=("Segoe UI", 16, "bold"),
            text_color=status_color
        )
        qty_value.pack(side="left")
        
        # Stock limits
        limits = []
        if self.product.min_stock > 0:
            limits.append(f"Min: {self.product.min_stock}")
        if self.product.max_stock:
            limits.append(f"Max: {self.product.max_stock}")
        
        if limits:
            limits_label = ctk.CTkLabel(
                qty_frame,
                text=f"({', '.join(limits)})",
                font=("Segoe UI", 10),
                text_color=AppStyles.GRAY
            )
            limits_label.pack(side="left", padx=(8, 0))
        
        # Controls
        controls_frame = ctk.CTkFrame(bottom_frame, fg_color="transparent")
        controls_frame.pack(side="right")
        
        # Quantity buttons
        btn_minus = ModernButton(
            controls_frame,
            text="−",
            variant="outline",
            size="sm",
            width=30,
            height=30,
            command=lambda: self._adjust_quantity(-1)
        )
        btn_minus.pack(side="left", padx=2)
        
        btn_plus = ModernButton(
            controls_frame,
            text="+",
            variant="primary",
            size="sm",
            width=30,
            height=30,
            command=lambda: self._adjust_quantity(1)
        )
        btn_plus.pack(side="left", padx=2)
        
        # Delete button
        btn_delete = ModernButton(
            controls_frame,
            text="Delete",
            variant="danger",
            size="sm",
            width=60,
            height=30,
            command=lambda: self._confirm_delete()
        )
        btn_delete.pack(side="left", padx=(5, 0))
    
    def _adjust_quantity(self, delta):
        """Adjust product quantity"""
        self.controller.update_quantity(self.product.name, delta)
    
    def _confirm_delete(self):
        """Show delete confirmation"""
        from tkinter import messagebox
        if messagebox.askyesno("Confirm Delete", f"Delete '{self.product.name}'?"):
            self.controller.delete_product(self.product.name)