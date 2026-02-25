import customtkinter as ctk
from src.assets.styles import AppStyles
from src.views.components.modern_button import ModernButton

class ProductCard(ctk.CTkFrame):
    """Modern product card component"""
    
    def __init__(self, parent, product, controller, **kwargs):
        super().__init__(
            parent,
            fg_color=AppStyles.WHITE,
            corner_radius=AppStyles.RADIUS_LG,
            border_width=1,
            border_color=AppStyles.LIGHT,
            **kwargs
        )
        
        self.product = product
        self.controller = controller
        
        self._setup_ui()
        self._apply_shadow()
    
    def _apply_shadow(self):
        """Apply shadow effect"""
        # Note: This is a visual approximation
        self.configure(border_width=1)
    
    def _setup_ui(self):
        # Status indicator
        status_color = self.product.get_status_color()
        status_frame = ctk.CTkFrame(
            self,
            fg_color=status_color,
            width=10,
            height=40,
            corner_radius=AppStyles.RADIUS_SM
        )
        status_frame.place(x=0, y=20, relheight=0.6)
        status_frame.pack_propagate(False)
        
        # Main content (with left padding for status)
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=(20, 15), pady=15)
        
        # Top section: Name and SKU
        top_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        top_frame.pack(fill="x", pady=(0, 10))
        
        # Product name and category
        name_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
        name_frame.pack(side="left", fill="x", expand=True)
        
        name_label = ctk.CTkLabel(
            name_frame,
            text=self.product.name,
            font=AppStyles.get_font(AppStyles.FONT_XL, "bold"),
            text_color=AppStyles.DARK,
            anchor="w"
        )
        name_label.pack(anchor="w")
        
        # Category and SKU
        info_frame = ctk.CTkFrame(name_frame, fg_color="transparent")
        info_frame.pack(anchor="w", pady=(5, 0))
        
        category_badge = ctk.CTkFrame(
            info_frame,
            fg_color=AppStyles.LIGHT,
            corner_radius=AppStyles.RADIUS_XL
        )
        category_badge.pack(side="left")
        
        category_label = ctk.CTkLabel(
            category_badge,
            text=self.product.category,
            font=AppStyles.get_font(AppStyles.FONT_XS),
            text_color=AppStyles.DARK,
            padx=10,
            pady=2
        )
        category_label.pack()
        
        sku_label = ctk.CTkLabel(
            info_frame,
            text=f"SKU: {self.product.sku}",
            font=AppStyles.get_font(AppStyles.FONT_XS),
            text_color=AppStyles.GRAY,
            padx=(10, 0)
        )
        sku_label.pack(side="left", padx=(10, 0))
        
        # Value badge (right side)
        if self.product.value and self.product.value != "0":
            value_badge = ctk.CTkFrame(
                top_frame,
                fg_color=AppStyles.SUCCESS_GRADIENT[0],
                corner_radius=AppStyles.RADIUS_XL
            )
            value_badge.pack(side="right")
            
            value_label = ctk.CTkLabel(
                value_badge,
                text=f"${self.product.value}",
                font=AppStyles.get_font(AppStyles.FONT_MD, "bold"),
                text_color=AppStyles.WHITE,
                padx=15,
                pady=5
            )
            value_label.pack()
        
        # Description
        if self.product.description:
            desc_label = ctk.CTkLabel(
                main_frame,
                text=self.product.description[:100] + "..." if len(self.product.description) > 100 else self.product.description,
                font=AppStyles.get_font(AppStyles.FONT_SM),
                text_color=AppStyles.GRAY,
                anchor="w",
                wraplength=400
            )
            desc_label.pack(fill="x", pady=(0, 15))
        
        # Quantity section
        quantity_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        quantity_frame.pack(fill="x", pady=(0, 15))
        
        quantity_label = ctk.CTkLabel(
            quantity_frame,
            text="Quantity:",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            text_color=AppStyles.GRAY
        )
        quantity_label.pack(side="left", padx=(0, 10))
        
        quantity_value = ctk.CTkLabel(
            quantity_frame,
            text=str(self.product.quantity),
            font=AppStyles.get_font(AppStyles.FONT_XL, "bold"),
            text_color=status_color
        )
        quantity_value.pack(side="left")
        
        # Stock status
        status_text = self.product.get_stock_status()
        if status_text != "In Stock":
            status_badge = ctk.CTkFrame(
                quantity_frame,
                fg_color=status_color,
                corner_radius=AppStyles.RADIUS_XL
            )
            status_badge.pack(side="left", padx=(15, 0))
            
            status_label = ctk.CTkLabel(
                status_badge,
                text=status_text,
                font=AppStyles.get_font(AppStyles.FONT_XS, "bold"),
                text_color=AppStyles.WHITE,
                padx=10,
                pady=2
            )
            status_label.pack()
        
        # Controls
        controls_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        controls_frame.pack(fill="x")
        
        # Left side: Min/Max indicators
        limits_frame = ctk.CTkFrame(controls_frame, fg_color="transparent")
        limits_frame.pack(side="left")
        
        if self.product.min_stock > 0:
            min_label = ctk.CTkLabel(
                limits_frame,
                text=f"Min: {self.product.min_stock}",
                font=AppStyles.get_font(AppStyles.FONT_XS),
                text_color=AppStyles.GRAY
            )
            min_label.pack(side="left", padx=(0, 10))
        
        if self.product.max_stock:
            max_label = ctk.CTkLabel(
                limits_frame,
                text=f"Max: {self.product.max_stock}",
                font=AppStyles.get_font(AppStyles.FONT_XS),
                text_color=AppStyles.GRAY
            )
            max_label.pack(side="left")
        
        # Right side: Action buttons
        actions_frame = ctk.CTkFrame(controls_frame, fg_color="transparent")
        actions_frame.pack(side="right")
        
        # Quantity adjust buttons
        btn_minus = ModernButton(
            actions_frame,
            text="−",
            variant="outline",
            size="sm",
            width=40,
            command=lambda: self._adjust_quantity(-1)
        )
        btn_minus.pack(side="left", padx=2)
        
        btn_plus = ModernButton(
            actions_frame,
            text="+",
            variant="primary",
            size="sm",
            width=40,
            command=lambda: self._adjust_quantity(1)
        )
        btn_plus.pack(side="left", padx=2)
        
        # Delete button
        btn_delete = ModernButton(
            actions_frame,
            text="Delete",
            variant="danger",
            size="sm",
            command=lambda: self._confirm_delete()
        )
        btn_delete.pack(side="left", padx=(10, 0))
    
    def _adjust_quantity(self, delta):
        """Adjust product quantity"""
        self.controller.update_quantity(self.product.name, delta)
    
    def _confirm_delete(self):
        """Show delete confirmation"""
        from tkinter import messagebox
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{self.product.name}'?"):
            self.controller.delete_product(self.product.name)