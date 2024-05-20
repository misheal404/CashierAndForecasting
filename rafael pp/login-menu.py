from tkinter import *
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv 

is_fullscreen = False

def save_user_data(username, password):
    with open('user_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def read_user_data():
    users = {}
    try:
        with open('user_data.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                users[row[0]] = row[1]
    except FileNotFoundError:
        pass
    return users

def toggle_fullscreen(window):
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    window.attributes("-fullscreen", is_fullscreen)

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2 - radius, y1,
        x2, y1, x2, y1 + radius,
        x2, y1 + radius, x2, y2 - radius,
        x2, y2 - radius, x2, y2,
        x2 - radius, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1 + radius, y2,
        x1, y2, x1, y2 - radius,
        x1, y2 - radius, x1, y1 + radius,
        x1, y1 + radius, x1, y1
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

def halaman_signin():
    global is_fullscreen, window, bg_photo
    try:
        if window:
            window.destroy()
    except NameError:
        pass
    window = tk.Tk()
    window.title("Cafe Chronicle")
    window.geometry("1366x768")
    window.configure(bg="#DDDDDD")
    window.resizable(True, True)
    window.attributes("-fullscreen", is_fullscreen)

    # Load the background image
    bg_image = Image.open("C:\\Users\\rafae\\OneDrive\\Dokumen\\PROKOM TUBES COBA COBA\\rafael pp\\OIP.jpg")  # Replace with your image path
    bg_image = bg_image.resize((1366, 768), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = Canvas(window, width=1366, height=768, bg="#DDDDDD", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Add the background image to the canvas
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Create a rounded rectangle on the canvas
    create_rounded_rectangle(canvas, -30, 0, 633, 720, radius=80, fill="#A9B388")

    heading = Label(window, text="Sign In", fg="#35522B", bg="#A9B388", font=("Montserrat", 50, "bold"))
    heading.place(x=200, y=120)

    username_label = Label(window, text="Username:", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    username_label.place(x=150, y=210)

    create_rounded_rectangle(canvas, 130, 245, 505, 295, radius=40, fill="#A9B388", outline="black", width=2)
    username_var = StringVar()

    def limit_username(*args):
        if len(username_var.get()) > 20:
            messagebox.showerror("Username Tidak Boleh Melebihi 20 Karakter!")
            username_var.set(username_var.get()[:20])

    username_var.trace("w", limit_username)
    username = Entry(window, textvariable=username_var, width=23, fg="black", border=0, bg="#A9B388", font=("Montserrat", 20))
    username.place(x=150, y=252)

    password_label = Label(window, text="Password:", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    password_label.place(x=150, y=310)

    create_rounded_rectangle(canvas, 130, 345, 505, 395, radius=40, fill="#A9B388", outline="black", width=2)
    password_var = StringVar()

    def limit_password(*args):
        if len(password_var.get()) > 20:
            messagebox.showerror("Input Error", "Password cannot exceed 20 characters.")
            password_var.set(password_var.get()[:20])

    password_var.trace("w", limit_password)
    password = Entry(window, textvariable=password_var, width=23, fg="black", border=0, bg="#A9B388", font=("Montserrat", 20), show='*')
    password.place(x=150, y=352)

    def toggle_password():
        if password.cget('show') == '*':
            password.config(show='')
        else:
            password.config(show='*')

    show_password = Checkbutton(window, text="Show Password", command=toggle_password, bg="#A9B388", fg="black", font=("Montserrat", 12))
    show_password.place(x=150, y=400)

    def sign_in():
        users = read_user_data()
        username = username_var.get()
        password = password_var.get()
        if username not in users:
            messagebox.showerror("Error", "Username tidak ditemukan")
        elif users[username] != password:
            messagebox.showerror("Error", "Password salah")
        else:
            messagebox.showinfo("Success", "Login berhasil")
            # Tambahkan logika untuk setelah berhasil login (misalnya membuka halaman baru)

    if ctk is not None:
        confirm_button = ctk.CTkButton(
            master=window,
            text=("Confirm"),
            font=("Circular Std", 20),
            text_color="#FFE7A9",
            width=120,
            height=40,
            fg_color="#35522B",
            bg_color="#A9B388",
            corner_radius=20,
            command=sign_in
        )
        confirm_button.place(x=135, y=440)
        
        fullscreen_button = ctk.CTkButton(
            master=window,
            text=("Toggle Fullscreen"),
            font=("Circular Std", 20),
            text_color="#FFE7A9",
            width=150,
            height=40,
            fg_color="#35522B",
            bg_color="#A9B388",
            corner_radius=20,
            command=lambda: toggle_fullscreen(window)
        )
        fullscreen_button.place(x=40, y=20)

    noacc_label = Label(window, text="Don't have account?", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    noacc_label.place(x=130, y=500)

    sign_up_label = Label(window, text="Sign Up", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold", "underline"), cursor="hand2")
    sign_up_label.place(x=300, y=498)
    sign_up_label.bind("<Button-1>", lambda e: halaman_signup())

    window.mainloop()

def back_signin():
    global window3
    if window3 and window3.winfo_exists():
        window3.destroy()
        window3 = None
    halaman_signin()

def halaman_signup():
    global is_fullscreen, window, window3, bg_photo
    if window and window.winfo_exists():
        window.destroy()
        window = None
    window3 = tk.Tk()
    window3.title("Cafe Chronicle - Sign Up")
    window3.geometry("1366x768")
    window3.configure(bg="#DDDDDD")
    window3.resizable(True, True)
    window3.attributes("-fullscreen", is_fullscreen)

    canvas = Canvas(window3, width=1366, height=768, bg="#DDDDDD", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Load the background image
    bg_image = Image.open("C:\\Users\\rafae\\OneDrive\\Dokumen\\PROKOM TUBES COBA COBA\\rafael pp\\OIP.jpg")  # Replace with your image path
    bg_image = bg_image.resize((1366, 768), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Add the background image to the canvas
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Implement the sign-up UI here
    heading = Label(window3, text="Sign Up", fg="#35522B", bg="#A9B388", font=("Montserrat", 30, "bold"))
    heading.place(x=550, y=110)

    # Create rounded frame
    create_rounded_rectangle(canvas, 390, 100, 860, 620, radius=50, fill="#A9B388", outline="#A9B388", width=2)

    username_label = Label(window3, text="Username:", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    username_label.place(x=440, y=170)

    # Create a rounded rectangle for username entry
    create_rounded_rectangle(canvas, 440, 205, 810, 235, radius=25, fill="#A9B388", outline="black", width=2)
    username_var = StringVar()

    # Limit the length of username
    def limit_username(*args):
        if len(username_var.get()) > 20:
            messagebox.showerror("Username Tidak Boleh Melebihi 20 Karakter!")
            username_var.set(username_var.get()[:20])

    username_var.trace("w", limit_username)
    username_entry = Entry(window3, textvariable=username_var, width=23, fg="black", border=0, bg="#A9B388", font=("Montserrat", 15))
    username_entry.place(x=445, y=207)

    password_label = Label(window3, text="Password:", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    password_label.place(x=440, y=260)

    # Create a rounded rectangle for password entry
    create_rounded_rectangle(canvas, 440, 295, 810, 325, radius=20, fill="#A9B388", outline="black", width=2)
    password_var = StringVar()

    # Limit the length of password
    def limit_password(*args):
        if len(password_var.get()) > 20:
            messagebox.showerror("Input Error", "Password cannot exceed 20 characters.")
            password_var.set(password_var.get()[:20])

    password_var.trace("w", limit_password)
    password_entry = Entry(window3, textvariable=password_var, width=23, fg="black", border=0, bg="#A9B388", font=("Montserrat", 15), show='*')
    password_entry.place(x=446, y=297)

    # Create a checkbox to show password
    def toggle_password():
        if password_entry.cget('show') == '*':
            password_entry.config(show='')
            confirm_password_entry.config(show='')
        else:
            password_entry.config(show='*')
            confirm_password_entry.config(show='*')

    show_password = Checkbutton(window3, text="Show Password", command=toggle_password, bg="#A9B388", fg="black", font=("Montserrat", 12))
    show_password.place(x=445, y=430)

    confirm_password_label = Label(window3, text="Confirm Password:", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    confirm_password_label.place(x=440, y=350)

    # Create a rounded rectangle for confirm password entry
    create_rounded_rectangle(canvas, 440, 385, 810, 415, radius=20, fill="#A9B388", outline="black", width=2)
    confirm_password_var = StringVar()

    confirm_password_entry = Entry(window3, textvariable=confirm_password_var, width=23, fg="black", border=0, bg="#A9B388", font=("Montserrat", 15), show='*')
    confirm_password_entry.place(x=445, y=387)

    def sign_up():
        username = username_var.get()
        password = password_var.get()
        confirm_password = confirm_password_var.get()

        # Validasi input
        if len(username) == 0 or len(password) == 0 or len(confirm_password) == 0:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # Simpan data pengguna
        save_user_data(username, password)
        if messagebox.askyesno("Sign Up Success", "Sign up berhasil! Kembali ke halaman sign in?"):
            window3.destroy()
            halaman_signin()

    if ctk is not None:
        signup_button = ctk.CTkButton(
            master=window3,
            text=("Sign Up"),
            font=("Circular Std", 20),
            text_color="#FFE7A9",
            width=120,
            height=40,
            fg_color="#35522B",
            bg_color="#A9B388",
            corner_radius=20,
            command=sign_up
        )
        signup_button.place(x=650, y=540)

        back_button = ctk.CTkButton(
            master=window3,
            text=("Back"),
            font=("Circular Std", 20),
            text_color="#FFE7A9",
            width=120,
            height=40,
            fg_color="#35522B",
            bg_color="#A9B388",
            corner_radius=20,
            command=back_signin
        )
        back_button.place(x=480, y=540)
    

    window3.mainloop()

halaman_signin()
