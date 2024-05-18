import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

def data_penjualan():
    # Define the new window
    win = ctk.CTk(fg_color='#76885B')

    # Mendapatkan ukuran layar
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    width = int(screen_width * 0.9)
    height = int(screen_height * 0.9)
    win.geometry(f"{width}x{height}")
    win.title("Menu Data Penjualan")

    title_text = ctk.CTkLabel(
        win,
        text="Data Penjualan Harian",
        font=("Helvetica", 50),
        text_color='#dddddd'
    )
    # Pindahkan teks ke tengah atas
    title_text.place(relx=0.5, rely=0.1, anchor='n')

    # Tambahkan tombol Back
    back_button = ctk.CTkButton(
        master=win,
        font=('Helvetica', 20, 'bold'),
        text="Back",
        width=100,
        height=50,
        corner_radius=10,
        border_width=1,
        border_color="#35522B",
        text_color='#FFE7A9',
        fg_color="#35522B", 
    )
    back_button.place(relx=0.05, rely=0.95, anchor='sw')

    win.mainloop()

data_penjualan()
