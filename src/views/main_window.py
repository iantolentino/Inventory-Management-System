import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from src.assets.styles import AppStyles
from src.views.add_product_panel import AddProductPanel
from src.views.statistics_panel import StatisticsPanel
from src.views.product_card import ProductCard
from src.views.components.search_bar import SearchBar
from src.views.components.modern_button import ModernButton
from src.config.settings import APP_TITLE

class MainWindow:
    """Enhanced main application window"""
    
    def __init__(self, controller):
        self.controller = controller
        self.controller.set_view(self)
        
        # Setup main window
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        self.app = ctk.CTk()
        self.app.title(APP_TITLE)
        self.app.geometry("1400x900")
        self.app.configure(fg_color=AppStyles.LIGHT)
        
        # Center window on screen
        self.app.update_idletasks()
        width = self.app.winfo_width()
        height = self.app.winfo_height()
        x = (self.app.winfo_screenwidth() // 2) - (width // 2)
        y = (self.app.winfo_screenheight() // 2) - (height // 2)
        self.app.geometry(f'{width}x{height}+{x}+{y}')
        
        # Variables
        self.filtered_products = {}
        self.search_text = ""
        
        self._setup_ui()
        self._setup_bindings()
    
    def _setup_ui(self):
        """Setup the main UI components"""
        # Top bar
        self._create_top_bar()
        
        # Main content area
        self._create_main_content()
    
    def _create_top_bar(self):
        """Create the top navigation bar"""
        top_bar = ctk.CTkFrame(
            self.app,
            fg_color=AppStyles.WHITE,
            height=70,
            corner_radius=0
        )
        top_bar.pack(fill="x", padx=0, pady=(0, 1))
        top_bar.pack_propagate(False)
        
        # Logo/Title
        title_frame = ctk.CTkFrame(top_bar, fg_color="transparent")
        title_frame.pack(side="left", padx=20)
        
        title_label = ctk.CTkLabel(
            title_frame,
            text="📦",
            font=AppStyles.get_font(32),
            text_color=AppStyles.PRIMARY
        )
        title_label.pack(side="left", padx=(0, 10))
        
        title_text = ctk.CTkLabel(
            title_frame,
            text="Inventory Pro",
            font=AppStyles.get_font(AppStyles.FONT_XL, "bold"),
            text_color=AppStyles.DARK
        )
        title_text.pack(side="left")
        
        # Search bar
        self.search_bar = SearchBar(
            top_bar,
            on_search=self._on_search,
            placeholder="Search products by name, category, or SKU..."
        )
        self.search_bar.pack(side="left", padx=20)
        
        # Exit button
        exit_button = ModernButton(
            top_bar,
            text="✕",
            variant="danger",
            size="md",
            width=40,
            command=self._confirm_exit
        )
        exit_button.pack(side="right", padx=20)
    
    def _create_main_content(self):
        """Create the main content area"""
        main_container = ctk.CTkFrame(self.app, fg_color="transparent")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Left panel (Add product form)
        left_panel = ctk.CTkFrame(main_container, fg_color="transparent", width=500)
        left_panel.pack(side="left", fill="y", padx=(0, 20))
        left_panel.pack_propagate(False)
        
        # Statistics panel
        self.stats_panel = StatisticsPanel(left_panel, self.controller)
        self.stats_panel.pack(fill="x", pady=(0, 20))
        
        # Add product form
        self.add_panel = AddProductPanel(left_panel, self.controller)
        self.add_panel.pack(fill="both", expand=True)
        
        # Right panel (Product list)
        right_panel = ctk.CTkFrame(
            main_container,
            fg_color=AppStyles.WHITE,
            corner_radius=AppStyles.RADIUS_LG
        )
        right_panel.pack(side="right", fill="both", expand=True)
        
        # Product list header
        header_frame = ctk.CTkFrame(right_panel, fg_color="transparent", height=60)
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        header_frame.pack_propagate(False)
        
        header_title = ctk.CTkLabel(
            header_frame,
            text="Product Inventory",
            font=AppStyles.get_font(AppStyles.FONT_XL, "bold"),
            text_color=AppStyles.DARK
        )
        header_title.pack(side="left")
        
        # Product count
        self.count_label = ctk.CTkLabel(
            header_frame,
            text="",
            font=AppStyles.get_font(AppStyles.FONT_MD),
            text_color=AppStyles.GRAY
        )
        self.count_label.pack(side="left", padx=(10, 0))
        
        # Sort dropdown
        sort_var = ctk.StringVar(value="Sort by")
        sort_menu = ctk.CTkOptionMenu(
            header_frame,
            values=["Name", "Quantity", "Value", "Category"],
            variable=sort_var,
            command=self._on_sort,
            fg_color=AppStyles.LIGHT,
            button_color=AppStyles.PRIMARY,
            text_color=AppStyles.DARK,
            font=AppStyles.get_font(AppStyles.FONT_SM)
        )
        sort_menu.pack(side="right")
        
        # Scrollable product list
        self._create_product_list(right_panel)
    
    def _create_product_list(self, parent):
        """Create the scrollable product list"""
        # Canvas and scrollbar
        canvas_frame = ctk.CTkFrame(parent, fg_color="transparent")
        canvas_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        self.canvas = tk.Canvas(
            canvas_frame,
            bg=AppStyles.WHITE,
            highlightthickness=0
        )
        
        scrollbar = tk.Scrollbar(
            canvas_frame,
            orient="vertical",
            command=self.canvas.yview
        )
        
        self.scrollable_frame = tk.Frame(self.canvas, bg=AppStyles.WHITE)
        
        # Create window reference
        self.scrollable_window = self.canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor="nw",
            width=self.canvas.winfo_width()
        )
        
        # Bindings
        def configure_canvas(event):
            self.canvas.itemconfig(self.scrollable_window, width=event.width)
        
        self.canvas.bind("<Configure>", configure_canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def _setup_bindings(self):
        """Setup event bindings"""
        # Scroll bindings
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)
        self.canvas.bind("<ButtonPress-1>", self._on_touch_scroll_start)
        self.canvas.bind("<B1-Motion>", self._on_touch_scroll_move)
        
        # Keyboard shortcuts
        self.app.bind("<Control-n>", lambda e: self.add_panel.entry_name.focus())
        self.app.bind("<Control-f>", lambda e: self.search_bar.search_entry.focus())
        self.app.bind("<Escape>", lambda e: self._confirm_exit())
        self.app.bind("<F5>", lambda e: self.refresh_display())
    
    def _on_mouse_wheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def _on_touch_scroll_start(self, event):
        """Handle touch scroll start"""
        self.canvas.scan_mark(event.x, event.y)
    
    def _on_touch_scroll_move(self, event):
        """Handle touch scroll move"""
        self.canvas.scan_dragto(event.x, event.y, gain=1)
    
    def _on_search(self, search_text):
        """Handle search"""
        self.search_text = search_text.lower()
        self.refresh_display()
    
    def _on_sort(self, sort_by):
        """Handle sort"""
        # Store sort preference
        self.sort_by = sort_by.lower()
        self.refresh_display()
    
    def _confirm_exit(self):
        """Confirm exit dialog"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.app.destroy()

    def _create_top_bar(self):
        """Create the top navigation bar"""
        top_bar = ctk.CTkFrame(
            self.app,
            fg_color=AppStyles.WHITE,
            height=70,
            corner_radius=0
        )
        top_bar.pack(fill="x", padx=0, pady=(0, 1))
        top_bar.pack_propagate(False)
        
        # Logo/Title
        title_frame = ctk.CTkFrame(top_bar, fg_color="transparent")
        title_frame.pack(side="left", padx=20)
        
        title_label = ctk.CTkLabel(
            title_frame,
            text="📦",
            font=AppStyles.get_font(32),
            text_color=AppStyles.PRIMARY
        )
        title_label.pack(side="left", padx=(0, 10))
        
        title_text = ctk.CTkLabel(
            title_frame,
            text="Inventory Management System",
            font=AppStyles.get_font(AppStyles.FONT_XL, "bold"),
            text_color=AppStyles.DARK
        )
        title_text.pack(side="left")
        
        # Search bar
        self.search_bar = SearchBar(
            top_bar,
            on_search=self._on_search,
            placeholder="Search products by name, category, or SKU..."
        )
        self.search_bar.pack(side="left", padx=20, fill="x", expand=True)
        
        # Exit button - Fixed: Remove width parameter since it's set in ModernButton
        exit_button = ModernButton(
            top_bar,
            text="✕",
            variant="danger",
            size="md",
            command=self._confirm_exit
        )
        exit_button.pack(side="right", padx=20)
    
    def refresh_display(self):
        """Refresh the product display"""
        # Get all products
        all_products = self.controller.get_all_products()
        
        # Filter products based on search
        filtered = {}
        if self.search_text:
            for name, product in all_products.items():
                if (self.search_text in name.lower() or
                    self.search_text in product.category.lower() or
                    self.search_text in product.sku.lower()):
                    filtered[name] = product
        else:
            filtered = all_products
        
        # Sort products
        if hasattr(self, 'sort_by'):
            if self.sort_by == "name":
                filtered = dict(sorted(filtered.items()))
            elif self.sort_by == "quantity":
                filtered = dict(sorted(filtered.items(), key=lambda x: x[1].quantity))
            elif self.sort_by == "value":
                filtered = dict(sorted(filtered.items(), key=lambda x: float(x[1].value or 0)))
            elif self.sort_by == "category":
                filtered = dict(sorted(filtered.items(), key=lambda x: x[1].category))
        
        self.filtered_products = filtered
        
        # Update statistics
        self.stats_panel.update_statistics(all_products)
        
        # Update count label
        total = len(all_products)
        shown = len(filtered)
        self.count_label.configure(text=f"({shown} of {total} products)")
        
        # Clear existing widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        # Show message if no products
        if not filtered:
            no_products_frame = ctk.CTkFrame(
                self.scrollable_frame,
                fg_color="transparent"
            )
            no_products_frame.pack(expand=True, fill="both", pady=100)
            
            icon_label = ctk.CTkLabel(
                no_products_frame,
                text="📦",
                font=AppStyles.get_font(AppStyles.FONT_XXXL)
            )
            icon_label.pack()
            
            message = "No products found"
            if self.search_text:
                message += f" matching '{self.search_text}'"
            
            no_products_label = ctk.CTkLabel(
                no_products_frame,
                text=message,
                font=AppStyles.get_font(AppStyles.FONT_XL),
                text_color=AppStyles.GRAY
            )
            no_products_label.pack(pady=10)
            
            if self.search_text:
                clear_btn = ModernButton(
                    no_products_frame,
                    text="Clear Search",
                    variant="outline",
                    command=lambda: self.search_bar.clear_search()
                )
                clear_btn.pack()
        
        # Recreate product cards
        else:
            for name in reversed(list(filtered.keys())):
                product_card = ProductCard(
                    self.scrollable_frame,
                    filtered[name],
                    self.controller
                )
                product_card.pack(fill="x", pady=(0, 10), padx=10)
    
    def run(self):
        """Run the application"""
        self.refresh_display()
        self.app.mainloop()