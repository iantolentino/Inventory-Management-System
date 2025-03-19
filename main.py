import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import json
import os

# Path for the JSON file
inventory_dir = r"C:\Projects\Inventory Management System\inventory"
inventory_file = os.path.join(inventory_dir, "inventory.json")
os.makedirs(inventory_dir, exist_ok=True)

# Load existing inventory data
if os.path.exists(inventory_file):
    with open(inventory_file, "r") as file:
        try:
            products = json.load(file)
        except json.JSONDecodeError:
            products = {}
else:
    products = {}

def save_inventory():
    with open(inventory_file, "w") as file:
        json.dump(products, file, indent=4)

def add_product():
    name = entry_name.get().strip()
    value = entry_value.get().strip() or "0"
    quantity = entry_quantity.get().strip()

    if not name or not quantity:
        messagebox.showwarning("Warning", "Product name and quantity are required!")
        return

    try:
        quantity = int(quantity)
    except ValueError:
        messagebox.showwarning("Warning", "Quantity must be a number!")
        return

    if name in products:
        messagebox.showwarning("Warning", "Product already exists!")
    else:
        products[name] = {"value": value, "quantity": quantity}
        update_product_display()
        save_inventory()
        entry_name.delete(0, ctk.END)
        entry_value.delete(0, ctk.END)
        entry_quantity.delete(0, ctk.END)

def update_quantity(name, delta):
    if name in products:
        products[name]["quantity"] = max(0, products[name]["quantity"] + delta)
        update_product_display()
        save_inventory()

def delete_product(name):
    if name in products:
        del products[name]
        update_product_display()
        save_inventory()

def update_product_display():
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    for name in reversed(list(products.keys())):
        data = products[name]
        product_item = ctk.CTkFrame(scrollable_frame, fg_color="#FFFFFF", corner_radius=10)
        product_item.pack(fill="x", pady=10, padx=10)

        # Configure grid
        product_item.columnconfigure(0, weight=1)
        product_item.columnconfigure(1, weight=0)

        # Product name/value
        details = ctk.CTkLabel(product_item, text=f"{name} | Value: {data['value']}", anchor="w",
                               text_color="#000000", font=font_settings)
        details.grid(row=0, column=0, padx=(20, 0), pady=20, sticky="w")

        # Buttons frame
        btn_frame = ctk.CTkFrame(product_item, fg_color="#FFFFFF")
        btn_frame.grid(row=0, column=1, padx=0, pady=10, sticky="e")

        add_button = ctk.CTkButton(btn_frame, text="+", width=60, height=60,
                                   command=lambda n=name: update_quantity(n, 1),
                                   fg_color="#000000", text_color="#FFFFFF", font=font_settings)
        add_button.pack(side="left", padx=5)

        quantity_label = ctk.CTkLabel(btn_frame, text=f"{data['quantity']}", text_color="#000000", font=font_settings)
        quantity_label.pack(side="left", padx=5)

        minus_button = ctk.CTkButton(btn_frame, text="-", width=60, height=60,
                                     command=lambda n=name: update_quantity(n, -1),
                                     fg_color="#000000", text_color="#FFFFFF", font=font_settings)
        minus_button.pack(side="left", padx=5)

        delete_btn = ctk.CTkButton(btn_frame, text="Delete", width=100, height=60,
                                   command=lambda n=name: delete_product(n),
                                   fg_color="#FF0000", text_color="#FFFFFF", font=font_settings)
        delete_btn.pack(side="left", padx=5)

def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def on_touch_scroll_start(event):
    canvas.scan_mark(event.x, event.y)

def on_touch_scroll_move(event):
    canvas.scan_dragto(event.x, event.y, gain=1)

def resize_scrollable_frame(event):
    canvas.itemconfig(scrollable_window, width=event.width)

def confirm_exit():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        app.destroy()

# --- UI Setup ---
ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("Inventory System")
app.attributes("-fullscreen", True)
app.configure(fg_color="#FFFFFF")

font_settings = ("Arial", 30)

# Exit Button
exit_button = ctk.CTkButton(app, text="X", width=60, height=60, command=confirm_exit,
                            fg_color="#000000", text_color="#FFFFFF", font=("Arial", 30, "bold"))
exit_button.place(relx=0.98, rely=0.02, anchor="ne")

# Add Product Section
add_frame = ctk.CTkFrame(app, fg_color="#FFFFFF")
add_frame.pack(pady=20)

entry_name = ctk.CTkEntry(add_frame, placeholder_text="Product Name", width=250, height=60, font=font_settings)
entry_name.grid(row=0, column=0, padx=10)

entry_value = ctk.CTkEntry(add_frame, placeholder_text="Value (Optional)", width=250, height=60, font=font_settings)
entry_value.grid(row=0, column=1, padx=10)

entry_quantity = ctk.CTkEntry(add_frame, placeholder_text="Quantity", width=250, height=60, font=font_settings)
entry_quantity.grid(row=0, column=2, padx=10)

add_btn = ctk.CTkButton(add_frame, text="Add Product", command=add_product, fg_color="#000000",
                        text_color="#FFFFFF", width=200, height=60, font=font_settings)
add_btn.grid(row=0, column=3, padx=10)

# Scrollable Product List
product_frame = ctk.CTkFrame(app, fg_color="#F0F0F0", corner_radius=10)
product_frame.pack(fill="both", expand=True, padx=0, pady=0)  # Removed padding

canvas = tk.Canvas(product_frame, bg="#F0F0F0", highlightthickness=0)
scrollbar = tk.Scrollbar(product_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#F0F0F0")

# Create window reference to control width
scrollable_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Bind resizing
canvas.bind("<Configure>", resize_scrollable_frame)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Bind scrolling
canvas.bind_all("<MouseWheel>", on_mouse_wheel)  # Trackpad scroll
canvas.bind("<ButtonPress-1>", on_touch_scroll_start)  # Touch scroll start
canvas.bind("<B1-Motion>", on_touch_scroll_move)  # Touch scroll move

# Load product list
update_product_display()

app.mainloop()
