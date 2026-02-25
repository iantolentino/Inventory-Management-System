import customtkinter as ctk
from src.assets.styles import AppStyles

class ModernButton(ctk.CTkButton):
    """Modern, animated button component"""
    
    def __init__(self, parent, text="", variant="primary", icon=None,
                 command=None, size="md", **kwargs):
        
        style = AppStyles.get_button_style(variant)
        
        # Size configurations
        sizes = {
            "sm": {"width": 80, "height": 32, "font": ("Segoe UI", 12)},
            "md": {"width": 120, "height": 40, "font": ("Segoe UI", 14)},
            "lg": {"width": 160, "height": 48, "font": ("Segoe UI", 16)},
            "xl": {"width": 200, "height": 56, "font": ("Segoe UI", 18)}
        }
        
        size_config = sizes.get(size, sizes["md"])
        
        # Base configuration
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
        
        # Remove None values
        button_config = {k: v for k, v in button_config.items() if v is not None}
        
        # Update with any kwargs passed
        button_config.update(kwargs)
        
        super().__init__(parent, **button_config)
        
        # Store original methods
        self._original_enter = None
        self._original_leave = None
        
    def _on_enter(self, event=None):
        """Handle mouse enter event - make event optional"""
        pass
    
    def _on_leave(self, event=None):
        """Handle mouse leave event - make event optional"""
        pass