import tkinter as tk
from tkinter import messagebox, Canvas, StringVar, Entry, Checkbutton, Label
from PIL import Image, ImageTk
import customtkinter as ctk
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
    frame_signup.pack_forget()
    frame_signin.pack(fill='both', expand=True)

def halaman_signup():
    frame_signin.pack_forget()
    frame_signup.pack(fill='both', expand=True)

def main():
    global root, frame_signin, frame_signup, bg_photo

    root = tk.Tk()
    root.title("Cafe Chronicle")
    root.geometry("1366x768")
    root.configure(bg="#DDDDDD")
    root.resizable(True, True)
    root.attributes("-fullscreen", is_fullscreen)

    # Load the background image
    bg_image = Image.open("C:\\Users\\rafae\\OneDrive\\Dokumen\\PROKOM TUBES COBA COBA\\rafael pp\\OIP.jpg")  # Replace with your image path
    bg_image = bg_image.resize((1366, 768), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    frame_signin = tk.Frame(root, bg="#DDDDDD")
    frame_signup = tk.Frame(root, bg="#DDDDDD")

    create_signin_ui(frame_signin)
    create_signup_ui(frame_signup)

    frame_signin.pack(fill='both', expand=True)

    root.mainloop()

def create_signin_ui(frame):
    canvas = Canvas(frame, width=1366, height=768, bg="#DDDDDD", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Add the background image to the canvas
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Create a rounded rectangle on the canvas
    create_rounded_rectangle(canvas, -30, 0, 633, 720, radius=80, fill="#A9B388")

    heading = Label(frame, text="Sign In", fg="#35522B", bg="#A9B388", font=("Montserrat", 50, "bold"))
    heading.place(x=200, y=120)

    username_label = Label(frame, text="Username:", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    username_label.place(x=150, y=210)

    create_rounded_rectangle(canvas, 130, 245, 505, 295, radius=40, fill="#A9B388", outline="black", width=2)
    username_var = StringVar()

    def limit_username(*args):
        if len(username_var.get()) > 20:
            messagebox.showerror("Input Error", "Username cannot exceed 20 characters.")
            username_var.set(username_var.get()[:20])

    username_var.trace("w", limit_username)
    username = Entry(frame, textvariable=username_var, width=23, fg="black", border=0, bg="#A9B388", font=("Montserrat", 20))
    username.place(x=150, y=252)

    password_label = Label(frame, text="Password:", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    password_label.place(x=150, y=310)

    create_rounded_rectangle(canvas, 130, 345, 505, 395, radius=40, fill="#A9B388", outline="black", width=2)
    password_var = StringVar()

    def limit_password(*args):
        if len(password_var.get()) > 20:
            messagebox.showerror("Input Error", "Password cannot exceed 20 characters.")
            password_var.set(password_var.get()[:20])

    password_var.trace("w", limit_password)
    password = Entry(frame, textvariable=password_var, width=23, fg="black", border=0, bg="#A9B388", font=("Montserrat", 20), show='*')
    password.place(x=150, y=352)

    def toggle_password():
        if password.cget('show') == '*':
            password.config(show='')
        else:
            password.config(show='*')

    show_password = Checkbutton(frame, text="Show Password", command=toggle_password, bg="#A9B388", fg="black", font=("Montserrat", 12))
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
            open_main_window()

    def open_main_window():
        new_window = tk.Toplevel(root)
        new_window.title("Main Window")
        new_window.geometry("800x600")
        Label(new_window, text="Welcome to the Main Window", font=("Montserrat", 20)).pack(pady=20)

    if ctk is not None:
        confirm_button = ctk.CTkButton(
            master=frame,
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
            master=frame,
            text=("Toggle Fullscreen"),
            font=("Circular Std", 20),
            text_color="#FFE7A9",
            width=150,
            height=40,
            fg_color="#35522B",
            bg_color="#A9B388",
            corner_radius=20,
            command=lambda: toggle_fullscreen(root)
        )
        fullscreen_button.place(x=40, y=20)

    noacc_label = Label(frame, text="Don't have account?", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    noacc_label.place(x=130, y=500)

    sign_up_label = Label(frame, text="Sign Up", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold", "underline"), cursor="hand2")
    sign_up_label.place(x=300, y=498)
    sign_up_label.bind("<Button-1>", lambda e: halaman_signup())

def create_signup_ui(frame):
    canvas = Canvas(frame, width=1366, height=768, bg="#DDDDDD", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Add the background image to the canvas
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Create a rounded rectangle on the canvas
    create_rounded_rectangle(canvas, 390, 100, 860, 620, radius=50, fill="#A9B388")

    heading = Label(frame, text="Sign Up", fg="#35522B", bg="#A9B388", font=("Montserrat", 30, "bold"))
    heading.place(x=550, y=110)

    username_label = Label(frame, text="Username:", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    username_label.place(x=440, y=170)

    create_rounded_rectangle(canvas, 440, 205, 810, 235, radius=25, fill="#A9B388", outline="black", width=2)
    username_var = StringVar()

    def limit_username(*args):
        if len(username_var.get()) > 20:
            messagebox.showerror("Input Error", "Username cannot exceed 20 characters.")
            username_var.set(username_var.get()[:20])

    username_var.trace("w", limit_username)
    username_entry = Entry(frame, textvariable=username_var, width=23, fg="black", border=0, bg="#A9B388", font=("Montserrat", 15))
    username_entry.place(x=445, y=207)

    password_label = Label(frame, text="Password:", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    password_label.place(x=440, y=260)

    create_rounded_rectangle(canvas, 440, 295, 810, 325, radius=20, fill="#A9B388", outline="black", width=2)
    password_var = StringVar()

    def limit_password(*args):
        if len(password_var.get()) > 20:
            messagebox.showerror("Input Error", "Password cannot exceed 20 characters.")
            password_var.set(password_var.get()[:20])

    password_var.trace("w", limit_password)
    password_entry = Entry(frame, textvariable=password_var, width=23, fg="black", border=0, bg="#A9B388", font=("Montserrat", 15), show='*')
    password_entry.place(x=446, y=297)

    def toggle_password():
        if password_entry.cget('show') == '*':
            password_entry.config(show='')
            confirm_password_entry.config(show='')
        else:
            password_entry.config(show='*')
            confirm_password_entry.config(show='*')

    show_password = Checkbutton(frame, text="Show Password", command=toggle_password, bg="#A9B388", fg="black", font=("Montserrat", 12))
    show_password.place(x=445, y=430)

    confirm_password_label = Label(frame, text="Confirm Password:", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    confirm_password_label.place(x=440, y=350)

    create_rounded_rectangle(canvas, 440, 385, 810, 415, radius=20, fill="#A9B388", outline="black", width=2)
    confirm_password_var = StringVar()

    confirm_password_entry = Entry(frame, textvariable=confirm_password_var, width=23, fg="black", border=0, bg="#A9B388", font=("Montserrat", 15), show='*')
    confirm_password_entry.place(x=445, y=387)

    def sign_up():
        username = username_var.get()
        password = password_var.get()
        confirm_password = confirm_password_var.get()

        if len(username) == 0 or len(password) == 0 or len(confirm_password) == 0:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        save_user_data(username, password)
        messagebox.showinfo("Success", "Sign up berhasil! Kembali ke halaman sign in?")
        halaman_signin()

    if ctk is not None:
        signup_button = ctk.CTkButton(
            master=frame,
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
            master=frame,
            text=("Back"),
            font=("Circular Std", 20),
            text_color="#FFE7A9",
            width=120,
            height=40,
            fg_color="#35522B",
            bg_color="#A9B388",
            corner_radius=20,
            command=halaman_signin
        )
        back_button.place(x=480, y=540)

main()

