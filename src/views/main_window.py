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
        
        # Get screen dimensions
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        
        # Set window size
        window_width = int(screen_width * 0.9)
        window_height = int(screen_height * 0.9)
        
        self.app.geometry(f"{window_width}x{window_height}+{int(screen_width*0.05)}+{int(screen_height*0.05)}")
        self.app.configure(fg_color=AppStyles.LIGHT)
        
        # Variables
        self.filtered_products = {}
        self.search_text = ""
        self.sort_by = "name"
        
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
            height=60,
            corner_radius=0
        )
        top_bar.pack(fill="x", padx=0, pady=(0, 10))
        top_bar.pack_propagate(False)
        
        # Logo/Title
        title_frame = ctk.CTkFrame(top_bar, fg_color="transparent")
        title_frame.pack(side="left", padx=15)
        
        title_label = ctk.CTkLabel(
            title_frame,
            text="📦",
            font=("Segoe UI", 24),
            text_color=AppStyles.PRIMARY
        )
        title_label.pack(side="left", padx=(0, 5))
        
        title_text = ctk.CTkLabel(
            title_frame,
            text="Inventory Pro",
            font=("Segoe UI", 18, "bold"),
            text_color=AppStyles.DARK
        )
        title_text.pack(side="left")
        
        # Search bar
        self.search_bar = SearchBar(
            top_bar,
            on_search=self._on_search,
            placeholder="Search products..."
        )
        self.search_bar.pack(side="left", padx=20, fill="x", expand=True)
        
        # Exit button
        exit_button = ModernButton(
            top_bar,
            text="Exit",
            variant="danger",
            size="sm",
            command=self._confirm_exit
        )
        exit_button.pack(side="right", padx=15)
    
    def _create_main_content(self):
        """Create the main content area"""
        # Main container
        main_container = ctk.CTkFrame(self.app, fg_color="transparent")
        main_container.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        
        # Configure grid
        main_container.grid_columnconfigure(0, weight=1, minsize=400)
        main_container.grid_columnconfigure(1, weight=3)
        
        # Left panel
        left_panel = ctk.CTkFrame(main_container, fg_color="transparent")
        left_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        # Statistics panel
        self.stats_panel = StatisticsPanel(left_panel, self.controller)
        self.stats_panel.pack(fill="x", pady=(0, 10))
        
        # Add product form
        self.add_panel = AddProductPanel(left_panel, self.controller)
        self.add_panel.pack(fill="both", expand=True)
        
        # Right panel
        right_panel = ctk.CTkFrame(
            main_container,
            fg_color=AppStyles.WHITE,
            corner_radius=AppStyles.RADIUS_MD
        )
        right_panel.grid(row=0, column=1, sticky="nsew")
        
        # Product list header
        self._create_product_list_header(right_panel)
        
        # Scrollable product list
        self._create_product_list(right_panel)
    
    def _create_product_list_header(self, parent):
        """Create the product list header"""
        header_frame = ctk.CTkFrame(parent, fg_color="transparent", height=50)
        header_frame.pack(fill="x", padx=15, pady=(15, 10))
        header_frame.pack_propagate(False)
        
        # Title and count
        title_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        title_frame.pack(side="left")
        
        header_title = ctk.CTkLabel(
            title_frame,
            text="Product Inventory",
            font=("Segoe UI", 18, "bold"),
            text_color=AppStyles.DARK
        )
        header_title.pack(side="left")
        
        self.count_label = ctk.CTkLabel(
            title_frame,
            text="",
            font=("Segoe UI", 14),
            text_color=AppStyles.GRAY
        )
        self.count_label.pack(side="left", padx=(10, 0))
        
        # Sort controls
        sort_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        sort_frame.pack(side="right")
        
        sort_label = ctk.CTkLabel(
            sort_frame,
            text="Sort by:",
            font=("Segoe UI", 14),
            text_color=AppStyles.GRAY
        )
        sort_label.pack(side="left", padx=(0, 5))
        
        sort_var = ctk.StringVar(value="Name")
        sort_menu = ctk.CTkOptionMenu(
            sort_frame,
            values=["Name", "Quantity", "Value", "Category"],
            variable=sort_var,
            command=self._on_sort,
            fg_color=AppStyles.LIGHT,
            button_color=AppStyles.PRIMARY,
            text_color=AppStyles.DARK,
            font=("Segoe UI", 12),
            width=100
        )
        sort_menu.pack(side="left")
    
    def _create_product_list(self, parent):
        """Create the scrollable product list"""
        # Canvas and scrollbar
        canvas_frame = ctk.CTkFrame(parent, fg_color="transparent")
        canvas_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        
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
            anchor="nw"
        )
        
        # Bindings
        def configure_canvas(event):
            self.canvas.itemconfig(self.scrollable_window, width=event.width)
        
        self.canvas.bind("<Configure>", configure_canvas)
        
        def configure_scrollable_frame(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        self.scrollable_frame.bind("<Configure>", configure_scrollable_frame)
        
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def _setup_bindings(self):
        """Setup event bindings"""
        # Scroll bindings
        def on_mouse_wheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        self.canvas.bind_all("<MouseWheel>", on_mouse_wheel)
    
    def _on_search(self, search_text):
        """Handle search"""
        self.search_text = search_text.lower()
        self.refresh_display()
    
    def _on_sort(self, sort_by):
        """Handle sort"""
        self.sort_by = sort_by.lower()
        self.refresh_display()
    
    def _confirm_exit(self):
        """Confirm exit dialog"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.app.quit()
            self.app.destroy()
    
    def refresh_display(self):
        """Refresh the product display"""
        # Get all products
        all_products = self.controller.get_all_products()
        
        # Filter products based on search
        filtered = {}
        if self.search_text:
            for name, product in all_products.items():
                if (self.search_text in name.lower() or
                    self.search_text in product.category.lower()):
                    filtered[name] = product
        else:
            filtered = all_products
        
        # Sort products
        if self.sort_by == "name":
            filtered = dict(sorted(filtered.items()))
        elif self.sort_by == "quantity":
            filtered = dict(sorted(filtered.items(), key=lambda x: x[1].quantity, reverse=True))
        elif self.sort_by == "value":
            filtered = dict(sorted(filtered.items(), 
                                 key=lambda x: float(x[1].value or 0), reverse=True))
        elif self.sort_by == "category":
            filtered = dict(sorted(filtered.items(), key=lambda x: x[1].category))
        
        self.filtered_products = filtered
        
        # Update statistics
        self.stats_panel.update_statistics(all_products)
        
        # Update count label
        total = len(all_products)
        shown = len(filtered)
        self.count_label.configure(text=f"({shown} of {total})")
        
        # Clear existing widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        # Show message if no products
        if not filtered:
            no_products_frame = ctk.CTkFrame(
                self.scrollable_frame,
                fg_color="transparent"
            )
            no_products_frame.pack(expand=True, fill="both", pady=50)
            
            icon_label = ctk.CTkLabel(
                no_products_frame,
                text="📦",
                font=("Segoe UI", 48)
            )
            icon_label.pack()
            
            message = "No products found"
            if self.search_text:
                message += f" matching '{self.search_text}'"
            
            no_products_label = ctk.CTkLabel(
                no_products_frame,
                text=message,
                font=("Segoe UI", 16),
                text_color=AppStyles.GRAY
            )
            no_products_label.pack(pady=10)
            
            if self.search_text:
                clear_btn = ModernButton(
                    no_products_frame,
                    text="Clear Search",
                    variant="outline",
                    size="md",
                    command=lambda: self.search_bar.clear_search()
                )
                clear_btn.pack()
        
        # Recreate product cards
        else:
            for name in list(filtered.keys()):
                product_card = ProductCard(
                    self.scrollable_frame,
                    filtered[name],
                    self.controller
                )
                product_card.pack(fill="x", pady=(0, 10))
    
    def run(self):
        """Run the application"""
        self.refresh_display()
        self.app.mainloop()