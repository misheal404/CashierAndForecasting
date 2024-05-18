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
        fg_color="#627254",
        command=lambda: Kasir(win).show_menu_kasir()  # Menggunakan jendela win sebagai root
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
        fg_color="#627254",
        command=data_penjualan
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
        fg_color="#ff3131",
        command=win.destroy
    )
    keluar_button.place(relx=0.75, rely=0.70, anchor='n')

    # Load and display image
    image = Image.open("D:\PROKOM\CashierAndForecasting\menu&data_penjualan&menukasir\gambarmenu.png")
    image = image.resize((int(image.width * 1.6), int(image.height * 1.6)), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Create a canvas to place the image
    canvas = ctk.CTkCanvas(win, width=image.width, height=image.height, bd=0, highlightthickness=0)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.place(relx=0.15, rely=0.3)

    # Keep reference to the image to prevent it from being garbage collected
    canvas.image = photo

    win.mainloop()

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
    title_text.place(relx=0.5, rely=0.1, anchor='n')

    back_button = ctk.CTkButton(
        master=win,
        font=('Helvetica', 20, 'bold'),
        text="Kembali",
        width=100,
        height=50,
        corner_radius=10,
        border_width=1,
        border_color="#35522B",
        text_color='#FFE7A9',
        fg_color="#35522B",
        command=choose_menu
    )
    back_button.place(relx=0.05, rely=0.95, anchor='sw')

    win.mainloop()

class Kasir:
    def __init__(self, root):
        self.root = root

    def update_quantity(self, item, change):
        self.items[item] += change
        if self.items[item] < 0:
            self.items[item] = 0
        self.update_display()

    def update_display(self):
        for item, label in self.labels.items():
            label.configure(text=f"{self.items[item]}")

    def show_menu_kasir(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Change background color
        self.root.configure(fg_color='#a9b388')

        title_text = ctk.CTkLabel(
            self.root,
            text="List Menu",
            font=("Helvetica", 50),
            text_color='#35522b'
        )
        title_text.place(relx=0.5, rely=0.1, anchor='n')

        self.items = {
            "Coffe Latte": 0,
            "Caramel Latte": 0,
            "Cappuccino": 0,
            "Mocha Latte": 0,
            "Americano": 0,
            "Vanilla Latte": 0
        }

        self.labels = {}
        self.buttons = {}  # Dictionary to store plus and minus buttons

        for idx, (item, qty) in enumerate(self.items.items()):
            # Frame for border
            item_frame = ctk.CTkFrame(
                master=self.root,
                width=1000,
                height=70,
                corner_radius=25,
                fg_color='#FFFFFF'  # Background color white
            )
            item_frame.place(relx=0.5, rely=0.3 + idx * 0.1, anchor='center')

            # Item name
            item_name_label = ctk.CTkLabel(
                item_frame,
                text=item,
                font=("Helvetica", 30),
                text_color='#35522b'
            )
            item_name_label.place(relx=0.05, rely=0.5, anchor='w')

            # Minus button
            subtract_button = ctk.CTkButton(
                master=item_frame,
                font=('Helvetica', 20, 'bold'),
                text="-",
                width=50,
                height=50,
                corner_radius=25,
                border_width=1,
                border_color="#ff3131",
                text_color='#35522b',
                fg_color="#ff3131",
                command=lambda item=item: self.update_quantity(item, -1)
            )
            subtract_button.place(relx=0.75, rely=0.5, anchor='center')
            self.buttons[f"subtract_{item}"] = subtract_button

            # Quantity
            item_label = ctk.CTkLabel(
                item_frame,
                text=f"{self.items[item]}",
                font=("Helvetica", 30),
                text_color='#35522b'
            )
            item_label.place(relx=0.85, rely=0.5, anchor='center')
            self.labels[item] = item_label

            # Plus button
            add_button = ctk.CTkButton(
                master=item_frame,
                font=('Helvetica', 20, 'bold'),
                text="+",
                width=50,
                height=50,
                corner_radius=25,
                border_width=1,
                text_color='#35522b',
                border_color="#ffe7a9",
                fg_color="#ffe7a9",
                command=lambda item=item: self.update_quantity(item, 1)
            )
            add_button.place(relx=0.95, rely=0.5, anchor='center')
            self.buttons[f"add_{item}"] = add_button

        # Done button
        done_button = ctk.CTkButton(
            master=self.root,
            font=('Helvetica', 20, 'bold'),
            text="Done",
            width=150,
            height=50,
            corner_radius=10,
            border_width=1,
            text_color='#FFE7A9',
            border_color="#35522B",
            fg_color="#35522B",
            command=self.process_order  # Add function to process order
        )
        done_button.place(relx=0.95, rely=0.95, anchor='se')

        # Back button
        back_button = ctk.CTkButton(
            master=self.root,
            font=('Helvetica', 20, 'bold'),
            text="Kembali",
            width=100,
            height=50,
            corner_radius=10,
            border_width=1,
            border_color="#35522B",
            text_color='#FFE7A9',
            fg_color="#35522B",
            command=choose_menu
        )
        back_button.place(relx=0.05, rely=0.95, anchor='sw')


    def process_order(self):
        # Fungsi untuk memproses pesanan (implementasikan sesuai kebutuhan Anda)
        pass

choose_menu()
