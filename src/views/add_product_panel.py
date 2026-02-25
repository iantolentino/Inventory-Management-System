import customtkinter as ctk
from tkinter import messagebox
from src.assets.styles import AppStyles
from src.views.components.modern_button import ModernButton
from src.utils.validators import Validators

class AddProductPanel(ctk.CTkFrame):
    """Compact add product panel"""
    
    def __init__(self, parent, controller, **kwargs):
        super().__init__(
            parent,
            fg_color=AppStyles.WHITE,
            corner_radius=AppStyles.RADIUS_MD,
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
            font=("Segoe UI", 16, "bold"),
            text_color=AppStyles.DARK
        )
        title.pack(anchor="w", padx=15, pady=(15, 5))
        
        # Form container
        form_frame = ctk.CTkFrame(self, fg_color="transparent")
        form_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        # Product Name
        name_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        name_frame.pack(fill="x", pady=(0, 8))
        
        name_label = ctk.CTkLabel(
            name_frame,
            text="Product Name *",
            font=("Segoe UI", 12),
            text_color=AppStyles.DARK,
            anchor="w"
        )
        name_label.pack(anchor="w")
        
        self.entry_name = ctk.CTkEntry(
            name_frame,
            placeholder_text="Enter product name",
            font=("Segoe UI", 13),
            height=35,
            border_width=1,
            border_color=AppStyles.LIGHT
        )
        self.entry_name.pack(fill="x", pady=(2, 0))
        
        # Category and Value row
        row1_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        row1_frame.pack(fill="x", pady=(0, 8))
        row1_frame.grid_columnconfigure(0, weight=1)
        row1_frame.grid_columnconfigure(1, weight=1)
        
        # Category
        cat_frame = ctk.CTkFrame(row1_frame, fg_color="transparent")
        cat_frame.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        
        cat_label = ctk.CTkLabel(
            cat_frame,
            text="Category",
            font=("Segoe UI", 12),
            text_color=AppStyles.DARK,
            anchor="w"
        )
        cat_label.pack(anchor="w")
        
        self.entry_category = ctk.CTkEntry(
            cat_frame,
            placeholder_text="Category",
            font=("Segoe UI", 13),
            height=35,
            border_width=1,
            border_color=AppStyles.LIGHT
        )
        self.entry_category.pack(fill="x", pady=(2, 0))
        
        # Value
        val_frame = ctk.CTkFrame(row1_frame, fg_color="transparent")
        val_frame.grid(row=0, column=1, sticky="ew", padx=(5, 0))
        
        val_label = ctk.CTkLabel(
            val_frame,
            text="Value ($)",
            font=("Segoe UI", 12),
            text_color=AppStyles.DARK,
            anchor="w"
        )
        val_label.pack(anchor="w")
        
        self.entry_value = ctk.CTkEntry(
            val_frame,
            placeholder_text="0.00",
            font=("Segoe UI", 13),
            height=35,
            border_width=1,
            border_color=AppStyles.LIGHT
        )
        self.entry_value.pack(fill="x", pady=(2, 0))
        
        # Quantity row
        row2_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        row2_frame.pack(fill="x", pady=(0, 8))
        
        qty_label = ctk.CTkLabel(
            row2_frame,
            text="Quantity *",
            font=("Segoe UI", 12),
            text_color=AppStyles.DARK,
            anchor="w"
        )
        qty_label.pack(anchor="w")
        
        self.entry_quantity = ctk.CTkEntry(
            row2_frame,
            placeholder_text="0",
            font=("Segoe UI", 13),
            height=35,
            border_width=1,
            border_color=AppStyles.LIGHT
        )
        self.entry_quantity.pack(fill="x", pady=(2, 0))
        
        # Stock Limits row
        row3_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        row3_frame.pack(fill="x", pady=(0, 8))
        row3_frame.grid_columnconfigure(0, weight=1)
        row3_frame.grid_columnconfigure(1, weight=1)
        
        # Min Stock
        min_frame = ctk.CTkFrame(row3_frame, fg_color="transparent")
        min_frame.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        
        min_label = ctk.CTkLabel(
            min_frame,
            text="Min Stock",
            font=("Segoe UI", 12),
            text_color=AppStyles.DARK,
            anchor="w"
        )
        min_label.pack(anchor="w")
        
        self.entry_min_stock = ctk.CTkEntry(
            min_frame,
            placeholder_text="Optional",
            font=("Segoe UI", 13),
            height=35,
            border_width=1,
            border_color=AppStyles.LIGHT
        )
        self.entry_min_stock.pack(fill="x", pady=(2, 0))
        
        # Max Stock
        max_frame = ctk.CTkFrame(row3_frame, fg_color="transparent")
        max_frame.grid(row=0, column=1, sticky="ew", padx=(5, 0))
        
        max_label = ctk.CTkLabel(
            max_frame,
            text="Max Stock",
            font=("Segoe UI", 12),
            text_color=AppStyles.DARK,
            anchor="w"
        )
        max_label.pack(anchor="w")
        
        self.entry_max_stock = ctk.CTkEntry(
            max_frame,
            placeholder_text="Optional",
            font=("Segoe UI", 13),
            height=35,
            border_width=1,
            border_color=AppStyles.LIGHT
        )
        self.entry_max_stock.pack(fill="x", pady=(2, 0))
        
        # Description
        desc_label = ctk.CTkLabel(
            form_frame,
            text="Description",
            font=("Segoe UI", 12),
            text_color=AppStyles.DARK,
            anchor="w"
        )
        desc_label.pack(anchor="w")
        
        self.entry_description = ctk.CTkTextbox(
            form_frame,
            font=("Segoe UI", 13),
            height=60,
            border_width=1,
            border_color=AppStyles.LIGHT,
            wrap="word"
        )
        self.entry_description.pack(fill="x", pady=(2, 10))
        
        # Buttons
        button_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        button_frame.pack(fill="x")
        
        self.add_button = ModernButton(
            button_frame,
            text="Add Product",
            variant="success",
            size="md",
            command=self._add_product
        )
        self.add_button.pack(side="left", padx=(0, 5), fill="x", expand=True)
        
        self.clear_button = ModernButton(
            button_frame,
            text="Clear",
            variant="outline",
            size="md",
            command=self._clear_form
        )
        self.clear_button.pack(side="right", padx=(5, 0), fill="x", expand=True)
    
    def _add_product(self):
        """Handle add product action"""
        try:
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
            
            # Get description
            description = self.entry_description.get("1.0", "end-1c").strip()
            
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
                messagebox.showinfo("Success", f"Product added successfully!")
                self._clear_form()
            else:
                messagebox.showwarning("Error", "Product already exists!")
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
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