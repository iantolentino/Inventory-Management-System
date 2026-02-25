"""Centralized styling for the application"""

class AppStyles:
    """Application-wide styles"""
    
    # Color scheme
    PRIMARY = "#2C3E50"
    SECONDARY = "#3498DB"
    SUCCESS = "#27AE60"
    DANGER = "#E74C3C"
    WARNING = "#F39C12"
    INFO = "#3498DB"
    LIGHT = "#ECF0F1"
    DARK = "#2C3E50"
    WHITE = "#FFFFFF"
    GRAY = "#95A5A6"
    
    # Gradients
    PRIMARY_GRADIENT = ["#3498DB", "#2980B9"]
    SUCCESS_GRADIENT = ["#27AE60", "#229954"]
    DANGER_GRADIENT = ["#E74C3C", "#B03A2E"]
    
    # Font sizes
    FONT_XS = 12
    FONT_SM = 14
    FONT_MD = 16
    FONT_LG = 20
    FONT_XL = 24
    FONT_XXL = 32
    FONT_XXXL = 48
    
    # Spacing
    SPACING_XS = 5
    SPACING_SM = 10
    SPACING_MD = 15
    SPACING_LG = 20
    SPACING_XL = 30
    SPACING_XXL = 50
    
    # Border radius
    RADIUS_SM = 5
    RADIUS_MD = 10
    RADIUS_LG = 15
    RADIUS_XL = 20
    RADIUS_CIRCLE = 100
    
    # Shadows
    SHADOW_CONFIG = {
        "light": {"offset": (2, 2), "blur": 4, "color": "#CCCCCC"},
        "medium": {"offset": (3, 3), "blur": 6, "color": "#999999"},
        "dark": {"offset": (4, 4), "blur": 8, "color": "#666666"}
    }
    
    # Animations
    ANIMATION_DURATION = 200  # ms
    HOVER_ALPHA = 0.9
    
    # Font family
    FONT_FAMILY = "Segoe UI"
    
    @classmethod
    def get_font(cls, size=FONT_MD, weight="normal"):
        """Get font configuration"""
        return (cls.FONT_FAMILY, size, weight)
    
    @classmethod
    def get_button_style(cls, variant="primary"):
        """Get button style based on variant"""
        styles = {
            "primary": {
                "fg_color": cls.PRIMARY,
                "hover_color": cls.DARK,
                "text_color": cls.WHITE
            },
            "success": {
                "fg_color": cls.SUCCESS,
                "hover_color": cls.SUCCESS_GRADIENT[1],
                "text_color": cls.WHITE
            },
            "danger": {
                "fg_color": cls.DANGER,
                "hover_color": cls.DANGER_GRADIENT[1],
                "text_color": cls.WHITE
            },
            "secondary": {
                "fg_color": cls.GRAY,
                "hover_color": cls.DARK,
                "text_color": cls.WHITE
            },
            "outline": {
                "fg_color": "transparent",
                "hover_color": cls.LIGHT,
                "text_color": cls.PRIMARY,
                "border_width": 2,
                "border_color": cls.PRIMARY
            }
        }
        return styles.get(variant, styles["primary"])