import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from src.views.add_product_frame import AddProductFrame
from src.views.product_item import ProductItem
from src.config.settings import COLORS, APP_TITLE, FONT_SETTINGS

class MainWindow:
    """Main application window"""
    
    def __init__(self, controller):
        self.controller = controller
        self.controller.set_view(self)
        
        # Setup main window
        self.app = ctk.CTk()
        self.app.title(APP_TITLE)
        self.app.attributes("-fullscreen", True)
        self.app.configure(fg_color=COLORS["bg_light"])
        
        self._setup_ui()
        self._setup_scroll_bindings()
    
    def _setup_ui(self):
        """Setup the main UI components"""
        # Exit button
        self._create_exit_button()
        
        # Add product section
        self.add_frame = AddProductFrame(self.app, self.controller)
        self.add_frame.pack(pady=20)
        
        # Scrollable product list
        self._create_product_list()
    
    def _create_exit_button(self):
        """Create the exit button"""
        exit_button = ctk.CTkButton(
            self.app,
            text="x",
            width=40,
            height=30,
            command=self._confirm_exit,
            fg_color=COLORS["bg_light"],
            text_color=COLORS["text_primary"],
            hover_color=COLORS["bg_light"],
            font=("Arial", 30)
        )
        exit_button.place(relx=0.99, rely=0.01, anchor="ne")
    
    def _create_product_list(self):
        """Create the scrollable product list area"""
        # Main container
        self.product_frame = ctk.CTkFrame(
            self.app, 
            fg_color=COLORS["bg_dark"], 
            corner_radius=10
        )
        self.product_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Canvas and scrollbar
        self.canvas = tk.Canvas(
            self.product_frame, 
            bg=COLORS["bg_dark"], 
            highlightthickness=0
        )
        self.scrollbar = tk.Scrollbar(
            self.product_frame, 
            orient="vertical", 
            command=self.canvas.yview
        )
        self.scrollable_frame = tk.Frame(
            self.canvas, 
            bg=COLORS["bg_dark"]
        )
        
        # Create window reference
        self.scrollable_window = self.canvas.create_window(
            (0, 0), 
            window=self.scrollable_frame, 
            anchor="nw"
        )
        
        # Bindings
        self.canvas.bind("<Configure>", self._resize_scrollable_frame)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
    
    def _setup_scroll_bindings(self):
        """Setup scroll bindings for mouse and touch"""
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)
        self.canvas.bind("<ButtonPress-1>", self._on_touch_scroll_start)
        self.canvas.bind("<B1-Motion>", self._on_touch_scroll_move)
    
    def _on_mouse_wheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def _on_touch_scroll_start(self, event):
        """Handle touch scroll start"""
        self.canvas.scan_mark(event.x, event.y)
    
    def _on_touch_scroll_move(self, event):
        """Handle touch scroll move"""
        self.canvas.scan_dragto(event.x, event.y, gain=1)
    
    def _resize_scrollable_frame(self, event):
        """Resize the scrollable frame"""
        self.canvas.itemconfig(self.scrollable_window, width=event.width)
    
    def _confirm_exit(self):
        """Confirm exit dialog"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.app.destroy()
    
    def refresh_display(self):
        """Refresh the product display"""
        # Clear existing widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        # Recreate product items
        products = self.controller.get_all_products()
        for name in reversed(list(products.keys())):
            product_item = ProductItem(
                self.scrollable_frame,
                name,
                products[name],
                self.controller
            )
            product_item.pack(fill="x", pady=10, padx=10)
    
    def run(self):
        """Run the application"""
        self.refresh_display()
        self.app.mainloop()