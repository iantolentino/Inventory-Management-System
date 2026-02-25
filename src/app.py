from src.controllers.inventory_controller import InventoryController
from src.views.main_window import MainWindow

class InventoryApp:
    """Main application class"""
    
    def __init__(self):
        self.controller = InventoryController()
        self.view = MainWindow(self.controller)
    
    def run(self):
        """Run the application"""
        self.view.run()