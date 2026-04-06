import tkinter as tk
from services.hotel_service import get_hotels
from ui.menu_ui import open_menu

def open_dashboard(root, username):
    root.destroy()

    window = tk.Tk()
    window.title("Dashboard")
    window.geometry("500x400")
    window.configure(bg="#f5f7fa")

    frame = tk.Frame(window, bg="#f5f7fa")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text=f"Welcome {username}",
             font=("Arial", 16, "bold"),
             bg="#f5f7fa").pack(pady=10)

    hotels = get_hotels()

    for h in hotels:
        tk.Button(frame,
                  text=h[1],
                  width=25,
                  bg="#2196F3",
                  fg="white",
                  command=lambda h=h: open_menu(window, h)).pack(pady=5)

    window.mainloop()