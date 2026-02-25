import customtkinter as ctk
from tkinter import messagebox
from src.assets.styles import AppStyles
from src.views.components.modern_button import ModernButton
from src.utils.validators import Validators

class AddProductPanel(ctk.CTkFrame):
    """Enhanced add product panel with modern design"""
    
    def __init__(self, parent, controller, **kwargs):
        super().__init__(
            parent,
            fg_color=AppStyles.WHITE,
            corner_radius=AppStyles.RADIUS_LG,
            **kwargs
        )
        
        self.controller = controller
        self.validators = Validators()
        
        self._setup_ui()
    
    def _setup_ui(self):
        # Title
        title = ctk.CTkLabel(
            self,
            text="Add New Product",
            font=AppStyles.get_font(AppStyles.FONT_XL, "bold"),
            text_color=AppStyles.DARK
        )
        title.pack(anchor="w", padx=20, pady=(20, 10))
        
        # Subtitle
        subtitle = ctk.CTkLabel(
            self,
            text="Fill in the product details below",
            font=AppStyles.get_font(AppStyles.FONT_SM),
            text_color=AppStyles.GRAY
        )
        subtitle.pack(anchor="w", padx=20, pady=(0, 20))
        
        # Form container
        form_frame = ctk.CTkFrame(self, fg_color="transparent")
        form_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Configure grid
        form_frame.grid_columnconfigure(1, weight=1)
        
        # Product Name
        ctk.CTkLabel(
            form_frame,
            text="Product Name *",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            text_color=AppStyles.DARK
        ).grid(row=0, column=0, padx=(0, 10), pady=5, sticky="w")
        
        self.entry_name = ctk.CTkEntry(
            form_frame,
            placeholder_text="Enter product name",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            height=40,
            border_width=2,
            border_color=AppStyles.LIGHT,
            corner_radius=AppStyles.RADIUS_MD
        )
        self.entry_name.grid(row=0, column=1, columnspan=3, pady=5, sticky="ew")
        
        # Category
        ctk.CTkLabel(
            form_frame,
            text="Category",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            text_color=AppStyles.DARK
        ).grid(row=1, column=0, padx=(0, 10), pady=5, sticky="w")
        
        self.entry_category = ctk.CTkEntry(
            form_frame,
            placeholder_text="e.g., Electronics, Clothing",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            height=40,
            border_width=2,
            border_color=AppStyles.LIGHT,
            corner_radius=AppStyles.RADIUS_MD
        )
        self.entry_category.grid(row=1, column=1, columnspan=3, pady=5, sticky="ew")
        
        # Value and Quantity in same row
        # Value
        ctk.CTkLabel(
            form_frame,
            text="Value ($)",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            text_color=AppStyles.DARK
        ).grid(row=2, column=0, padx=(0, 10), pady=5, sticky="w")
        
        self.entry_value = ctk.CTkEntry(
            form_frame,
            placeholder_text="0.00",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            height=40,
            border_width=2,
            border_color=AppStyles.LIGHT,
            corner_radius=AppStyles.RADIUS_MD,
            width=150
        )
        self.entry_value.grid(row=2, column=1, pady=5, sticky="w")
        
        # Quantity
        ctk.CTkLabel(
            form_frame,
            text="Quantity *",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            text_color=AppStyles.DARK
        ).grid(row=2, column=2, padx=(20, 10), pady=5, sticky="w")
        
        self.entry_quantity = ctk.CTkEntry(
            form_frame,
            placeholder_text="0",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            height=40,
            border_width=2,
            border_color=AppStyles.LIGHT,
            corner_radius=AppStyles.RADIUS_MD,
            width=150
        )
        self.entry_quantity.grid(row=2, column=3, pady=5, sticky="w")
        
        # Stock Limits
        # Min Stock
        ctk.CTkLabel(
            form_frame,
            text="Min Stock",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            text_color=AppStyles.DARK
        ).grid(row=3, column=0, padx=(0, 10), pady=5, sticky="w")
        
        self.entry_min_stock = ctk.CTkEntry(
            form_frame,
            placeholder_text="Optional",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            height=40,
            border_width=2,
            border_color=AppStyles.LIGHT,
            corner_radius=AppStyles.RADIUS_MD,
            width=150
        )
        self.entry_min_stock.grid(row=3, column=1, pady=5, sticky="w")
        
        # Max Stock
        ctk.CTkLabel(
            form_frame,
            text="Max Stock",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            text_color=AppStyles.DARK
        ).grid(row=3, column=2, padx=(20, 10), pady=5, sticky="w")
        
        self.entry_max_stock = ctk.CTkEntry(
            form_frame,
            placeholder_text="Optional",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            height=40,
            border_width=2,
            border_color=AppStyles.LIGHT,
            corner_radius=AppStyles.RADIUS_MD,
            width=150
        )
        self.entry_max_stock.grid(row=3, column=3, pady=5, sticky="w")
        
        # Description
        ctk.CTkLabel(
            form_frame,
            text="Description",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            text_color=AppStyles.DARK
        ).grid(row=4, column=0, padx=(0, 10), pady=5, sticky="w")
        
        self.entry_description = ctk.CTkTextbox(
            form_frame,
            font=AppStyles.get_font(AppStyles.FONT_MD),
            height=100,
            border_width=2,
            border_color=AppStyles.LIGHT,
            corner_radius=AppStyles.RADIUS_MD,
            wrap="word"
        )
        self.entry_description.grid(row=4, column=1, columnspan=3, pady=5, sticky="ew")
        
        # Buttons
        buttons_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        buttons_frame.grid(row=5, column=0, columnspan=4, pady=(20, 0))
        
        self.add_button = ModernButton(
            buttons_frame,
            text="Add Product",
            variant="success",
            size="lg",
            command=self._add_product
        )
        self.add_button.pack(side="left", padx=5)
        
        self.clear_button = ModernButton(
            buttons_frame,
            text="Clear",
            variant="outline",
            size="lg",
            command=self._clear_form
        )
        self.clear_button.pack(side="left", padx=5)
    
    def _add_product(self):
        """Handle add product action with validation"""
        # Validate product name
        name_valid, name_error = self.validators.validate_product_name(self.entry_name.get())
        if not name_valid:
            messagebox.showwarning("Validation Error", name_error)
            self.entry_name.focus()
            return
        
        # Validate quantity
        qty_valid, qty_error, quantity = self.validators.validate_quantity(self.entry_quantity.get())
        if not qty_valid:
            messagebox.showwarning("Validation Error", qty_error)
            self.entry_quantity.focus()
            return
        
        # Validate value
        value_valid, value_error, value = self.validators.validate_value(self.entry_value.get())
        if not value_valid:
            messagebox.showwarning("Validation Error", value_error)
            self.entry_value.focus()
            return
        
        # Get category
        category = self.entry_category.get().strip() or "Uncategorized"
        category_valid, category_error = self.validators.validate_category(category)
        if not category_valid:
            messagebox.showwarning("Validation Error", category_error)
            self.entry_category.focus()
            return
        
        # Get description
        description = self.entry_description.get("1.0", "end-1c").strip()
        desc_valid, desc_error = self.validators.validate_description(description)
        if not desc_valid:
            messagebox.showwarning("Validation Error", desc_error)
            self.entry_description.focus()
            return
        
        # Get stock limits
        min_stock = 0
        if self.entry_min_stock.get().strip():
            try:
                min_stock = int(self.entry_min_stock.get())
            except ValueError:
                messagebox.showwarning("Validation Error", "Min stock must be a number")
                return
        
        max_stock = None
        if self.entry_max_stock.get().strip():
            try:
                max_stock = int(self.entry_max_stock.get())
            except ValueError:
                messagebox.showwarning("Validation Error", "Max stock must be a number")
                return
        
        # Add product
        success = self.controller.add_product(
            name=self.entry_name.get().strip(),
            quantity=quantity,
            value=value,
            category=category,
            description=description,
            min_stock=min_stock,
            max_stock=max_stock
        )
        
        if success:
            messagebox.showinfo("Success", f"Product '{self.entry_name.get()}' added successfully!")
            self._clear_form()
        else:
            messagebox.showwarning("Error", "Product already exists or invalid input!")
    
    def _clear_form(self):
        """Clear all form fields"""
        self.entry_name.delete(0, ctk.END)
        self.entry_category.delete(0, ctk.END)
        self.entry_value.delete(0, ctk.END)
        self.entry_quantity.delete(0, ctk.END)
        self.entry_min_stock.delete(0, ctk.END)
        self.entry_max_stock.delete(0, ctk.END)
        self.entry_description.delete("1.0", ctk.END)
        self.entry_name.focus()