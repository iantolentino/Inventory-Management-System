import customtkinter as ctk
from src.assets.styles import AppStyles

class ModernButton(ctk.CTkButton):
    """Modern, animated button component"""
    
    def __init__(self, parent, text="", variant="primary", icon=None,
                 command=None, size="md", **kwargs):
        
        style = AppStyles.get_button_style(variant)
        
        # Size configurations
        sizes = {
            "sm": {"width": 80, "height": 32, "font": AppStyles.get_font(AppStyles.FONT_SM)},
            "md": {"width": 120, "height": 40, "font": AppStyles.get_font(AppStyles.FONT_MD)},
            "lg": {"width": 160, "height": 48, "font": AppStyles.get_font(AppStyles.FONT_LG)},
            "xl": {"width": 200, "height": 56, "font": AppStyles.get_font(AppStyles.FONT_XL)}
        }
        
        size_config = sizes.get(size, sizes["md"])
        
        # Merge configurations, with kwargs taking precedence
        button_config = {
            "text": text,
            "command": command,
            "corner_radius": AppStyles.RADIUS_MD,
            "font": size_config["font"],
            "width": size_config["width"],
            "height": size_config["height"],
            "fg_color": style.get("fg_color"),
            "hover_color": style.get("hover_color"),
            "text_color": style.get("text_color"),
            "border_width": style.get("border_width", 0),
            "border_color": style.get("border_color", None),
        }
        
        # Update with any kwargs passed (these will override defaults)
        button_config.update(kwargs)
        
        super().__init__(
            parent,
            **button_config
        )
        
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
    
    def _on_enter(self, event):
        """Hover effect"""
        self.configure( opacity=AppStyles.HOVER_ALPHA)
    
    def _on_leave(self, event):
        """Remove hover effect"""
        self.configure( opacity=1)