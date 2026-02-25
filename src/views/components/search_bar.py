import customtkinter as ctk
from src.assets.styles import AppStyles

class SearchBar(ctk.CTkFrame):
    """Modern search bar component"""
    
    def __init__(self, parent, on_search=None, placeholder="Search products...", **kwargs):
        super().__init__(
            parent,
            fg_color=AppStyles.WHITE,
            corner_radius=AppStyles.RADIUS_XL,
            border_width=2,
            border_color=AppStyles.LIGHT,
            **kwargs
        )
        
        self.on_search = on_search
        self.search_var = ctk.StringVar()
        self.search_var.trace('w', self._on_search_change)
        
        self._setup_ui(placeholder)
    
    def _setup_ui(self, placeholder):
        # Search icon (emoji as placeholder, you can use actual icons with PIL)
        icon_label = ctk.CTkLabel(
            self,
            text="🔍",
            font=AppStyles.get_font(AppStyles.FONT_LG),
            text_color=AppStyles.GRAY
        )
        icon_label.pack(side="left", padx=(15, 5))
        
        # Search entry
        self.search_entry = ctk.CTkEntry(
            self,
            textvariable=self.search_var,
            placeholder_text=placeholder,
            font=AppStyles.get_font(AppStyles.FONT_MD),
            fg_color="transparent",
            border_width=0,
            width=300
        )
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0, 15), pady=8)
        
        # Clear button (initially hidden)
        self.clear_button = ctk.CTkButton(
            self,
            text="✕",
            width=30,
            height=30,
            command=self.clear_search,
            fg_color="transparent",
            hover_color=AppStyles.LIGHT,
            text_color=AppStyles.GRAY,
            corner_radius=AppStyles.RADIUS_CIRCLE
        )
    
    def _on_search_change(self, *args):
        """Handle search input changes"""
        search_text = self.search_var.get()
        
        # Show/hide clear button
        if search_text:
            if not self.clear_button.winfo_ismapped():
                self.clear_button.pack(side="right", padx=(0, 10))
        else:
            self.clear_button.pack_forget()
        
        # Trigger search callback
        if self.on_search:
            self.on_search(search_text)
    
    def clear_search(self):
        """Clear search input"""
        self.search_var.set("")
        self.search_entry.focus()
    
    def get_search_text(self):
        """Get current search text"""
        return self.search_var.get()