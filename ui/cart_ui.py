import tkinter as tk
from services.order_service import place_order

def open_cart(parent, hotel, cart):
    window = tk.Toplevel(parent)
    window.title("Cart")
    window.geometry("450x400")
    window.configure(bg="#f5f7fa")

    frame = tk.Frame(window, bg="#f5f7fa")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Your Cart",
             font=("Arial", 16, "bold"),
             bg="#f5f7fa").pack(pady=10)

    total = 0

    if not cart:
        tk.Label(frame, text="Cart is empty",
                 bg="#f5f7fa", fg="red").pack()
        return

    for item in cart:
        tk.Label(frame,
                 text=f"{item['name']} - ₹{item['price']}",
                 bg="#f5f7fa").pack()

        total += item['price']

    tk.Label(frame,
             text=f"Total: ₹{total}",
             font=("Arial", 12, "bold"),
             bg="#f5f7fa").pack(pady=10)

    def order():
        place_order("Hari", hotel[1], cart)
        tk.Label(frame,
                 text="✅ Order Placed!",
                 fg="green",
                 bg="#f5f7fa").pack()

    tk.Button(frame,
              text="Place Order",
              bg="#4CAF50",
              fg="white",
              width=20,
              command=order).pack(pady=10)