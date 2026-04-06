import tkinter as tk
from services.hotel_service import get_menu
from ui.cart_ui import open_cart

cart = []

def open_menu(parent, hotel):
    window = tk.Toplevel(parent)
    window.title("Menu")
    window.geometry("500x400")
    window.configure(bg="#f5f7fa")

    frame = tk.Frame(window, bg="#f5f7fa")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text=hotel[1],
             font=("Arial", 16, "bold"),
             bg="#f5f7fa").pack(pady=10)

    items = get_menu(hotel[0])

    for item in items:
        name, price = item   # ✅ FIX HERE

        tk.Button(frame,
                  text=f"{name} - ₹{price}",
                  width=25,
                  bg="#FF9800",
                  fg="white",
                  command=lambda n=name, p=price: add_to_cart(n, p)).pack(pady=5)

    tk.Button(frame,
              text="Go to Cart",
              bg="#4CAF50",
              fg="white",
              command=lambda: open_cart(window, hotel, cart)).pack(pady=15)


def add_to_cart(name, price):
    cart.append({
        "name": name,
        "price": int(price)   # safe now
    })
    print("Cart:", cart)