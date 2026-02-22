import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Login Page")
root.geometry("500x300")
root.configure(bg="#b4aacb")  # Light purple background

# Center frame
frame = tk.Frame(root, bg="#b4aacb")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title = tk.Label(frame, text="login page",
                 font=("Arial", 12),
                 bg="#b4aacb")
title.grid(row=0, column=0, columnspan=2, pady=10)

# Name Label
name_label = tk.Label(frame, text="Name",
                      font=("Arial", 10),
                      bg="#b4aacb")
name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Name Entry
name_entry = tk.Entry(frame,
                      width=20,
                      bd=2,
                      relief="solid")
name_entry.grid(row=1, column=1, padx=10, pady=10)

# Password Label
password_label = tk.Label(frame, text="password",
                          font=("Arial", 10),
                          bg="#b4aacb")
password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Password Entry
password_entry = tk.Entry(frame,
                          width=20,
                          bd=2,
                          relief="solid",
                          show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Submit Button
submit_button = tk.Button(frame,
                          text="submit",
                          width=10,
                          bd=2,
                          relief="raised")
submit_button.grid(row=3, column=0, columnspan=2, pady=15)

root.mainloop()
