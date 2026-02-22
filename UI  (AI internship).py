import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext

main = tk.Tk()
main.geometry("1200x700")
main.configure(bg="black")
main.title("Chatbot App")

# ----- Container Frame -----
container = tk.Frame(main)
container.pack(fill="both", expand=True)

welcome_page = tk.Frame(container, bg="lightblue")
chatbot_page = tk.Frame(container, bg="lightgreen")

for page in (welcome_page, chatbot_page):
    page.grid(row=0, column=0, sticky="nsew")

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# ----- Switch Page Function -----
def sp(page):
    page.tkraise()

# ===============================
#         WELCOME PAGE
# ===============================

welcome_page.grid_rowconfigure(0, weight=1)
welcome_page.grid_rowconfigure(1, weight=1)
welcome_page.grid_rowconfigure(2, weight=1)
welcome_page.grid_columnconfigure(0, weight=1)

tk.Label(
    welcome_page,
    text="Welcome to Chatbot",
    font=("Arial", 30, "bold"),
    bg="lightblue",
    fg="black"
).grid(row=0, column=0)

un = tk.Entry(
    welcome_page,
    font=("Arial", 16),
    width=30,
    justify="center"
)
un.grid(row=1, column=0)

tk.Button(
    welcome_page,
    text="Start Chat",
    font=("Arial", 14),
    width=15,
    command=lambda: sp(chatbot_page)
).grid(row=2, column=0)

# ===============================
#         CHATBOT PAGE
# ===============================

chatbot_page.grid_rowconfigure(0, weight=1)
chatbot_page.grid_rowconfigure(1, weight=1)
chatbot_page.grid_rowconfigure(2, weight=1)
chatbot_page.grid_columnconfigure(0, weight=1)

tk.Label(
    chatbot_page,
    text="Chatbot Ready... Search Here",
    font=("Arial", 28, "bold"),
    bg="lightgreen"
).grid(row=0, column=0)

search_entry = tk.Entry(
    chatbot_page,
    font=("Arial", 16),
    width=40,
    justify="center"
)
search_entry.grid(row=1, column=0)

tk.Button(
    chatbot_page,
    text="Back",
    font=("Arial", 14),
    width=15,
    command=lambda: sp(welcome_page)
).grid(row=2, column=0)

# Show welcome page first
sp(welcome_page)

main.mainloop()
