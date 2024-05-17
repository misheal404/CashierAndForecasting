import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

def choose_menu():
    # Define the new window
    win = ctk.CTk(fg_color='#DDDDDD')

    # Mendapatkan ukuran layar
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    width = int(screen_width * 0.9)
    height = int(screen_height * 0.9)
    win.geometry(f"{width}x{height}")
    win.title("Choose Menu")

    # Title text
    title_text = ctk.CTkLabel(
        win,
        text="Hello, Welcome to Cafe Chronicle",
        font=("Helvetica", 50),
        text_color='#627254'
    )
    title_text.place(relx=0.05, rely=0.1, anchor='nw')

    # Subtitle text
    subtitle_text = ctk.CTkLabel(
        win,
        text="Please Choose the Menu",
        font=("Helvetica", 30),
        text_color='#000000'
    )
    subtitle_text.place(relx=0.07, rely=0.2, anchor='nw')

    # Kasir button
    kasir_button = ctk.CTkButton(
        master=win,
        font=('Helvetica', 40, 'bold'),
        text="Kasir",
        width=360,
        height=80,
        corner_radius=25,
        border_width=1,
        border_color="#EEEEEE",
        fg_color="#627254"
    )
    kasir_button.place(relx=0.75, rely=0.30, anchor='n')

    # Data Penjualan button
    penjualan_button = ctk.CTkButton(
        master=win,
        font=('Helvetica', 40, 'bold'),
        text="Data Penjualan",
        width=360,
        height=80,
        corner_radius=25,
        border_width=1,
        border_color="#EEEEEE",
        fg_color="#627254"
    )
    penjualan_button.place(relx=0.75, rely=0.50, anchor='n')

    # Keluar button
    keluar_button = ctk.CTkButton(
        master=win,
        font=('Helvetica', 40, 'bold'),
        text="Keluar",
        width=360,
        height=80,
        corner_radius=25,
        border_width=1,
        border_color="#EEEEEE",
        fg_color="#ff3131"
    )
    keluar_button.place(relx=0.75, rely=0.70, anchor='n')

    # Load and display image
    image = Image.open("CashierAndForecasting/menu/gambarmenu.png")
    image = image.resize((int(image.width * 1.6), int(image.height * 1.6)), Image.Resampling.LANCZOS)  # Perbesar gambar
    photo = ImageTk.PhotoImage(image)

    # Create a canvas to place the image
    canvas = ctk.CTkCanvas(win, width=image.width, height=image.height, bd=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.place(relx=0.15, rely=0.3)  # Geser gambar ke tengah

    # Keep reference to the image to prevent it from being garbage collected
    canvas.image = photo

    win.mainloop()

choose_menu()
