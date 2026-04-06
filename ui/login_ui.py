import tkinter as tk
from services.auth_service import login_user
from ui.dashboard_ui import open_dashboard

def start_login():
    def login():
        username = entry_user.get()
        password = entry_pass.get()

        user = login_user(username, password)

        if user:
            open_dashboard(root, username)
        else:
            label.config(text="Invalid credentials", fg="red")

    root = tk.Tk()
    root.title("Food Order System")
    root.geometry("400x350")
    root.configure(bg="#f5f7fa")

    frame = tk.Frame(root, bg="#f5f7fa")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Login", font=("Arial", 18, "bold"),
             bg="#f5f7fa").pack(pady=10)

    entry_user = tk.Entry(frame, width=25)
    entry_user.pack(pady=5)

    entry_pass = tk.Entry(frame, show="*", width=25)
    entry_pass.pack(pady=5)

    tk.Button(frame, text="Login",
              bg="#4CAF50", fg="white",
              width=20, command=login).pack(pady=15)

    label = tk.Label(frame, text="", bg="#f5f7fa")
    label.pack()

    root.mainloop()