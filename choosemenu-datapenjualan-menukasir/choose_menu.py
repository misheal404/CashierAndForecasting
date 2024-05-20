import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

def choose_menu():
    def open_kasir():
        kasir = Kasir(win)
        kasir.show_menu_kasir()

    def open_data_penjualan():
        win.destroy()
        data_penjualan()

    def close_program():
        win.destroy()

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
        command=open_kasir  # Menambahkan perintah untuk membuka menu kasir
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
        command=open_data_penjualan  # Menambahkan perintah untuk membuka data penjualan
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
        command=close_program  # Menambahkan perintah untuk keluar program
    )
    keluar_button.place(relx=0.75, rely=0.70, anchor='n')

    # Load and display image
    image = Image.open("D:\PROKOM\CashierAndForecasting\choosemenu-datapenjualan-menukasir\gambarmenu.png")
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
    def go_back():
        win.destroy()
        choose_menu()

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
        command=go_back  # Menambahkan perintah untuk kembali ke menu utama
    )
    back_button.place(relx=0.05, rely=0.95, anchor='sw')

    win.mainloop()

class Kasir:
    def __init__(self, root):
        self.root = root

    def update_quantity(self, item, change):
        self.items[item]['quantity'] += change
        if self.items[item]['quantity'] < 0:
            self.items[item]['quantity'] = 0
        self.update_display()

    def update_display(self):
        for item, label in self.labels.items():
            label.configure(text=f"{self.items[item]['quantity']}")

    def show_menu_kasir(self):
        def go_back():
            self.root.destroy()
            choose_menu()

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
        title_text.place(relx=0.5, rely=0.05, anchor='n')

        self.items = {
            "Coffee Latte": {"quantity": 0, "price": 20000},
            "Caramel Latte": {"quantity": 0, "price": 25000},
            "Cappuccino": {"quantity": 0, "price": 22000},
            "Mocha Latte": {"quantity": 0, "price": 23000},
            "Americano": {"quantity": 0, "price": 18000},
            "Vanilla Latte": {"quantity": 0, "price": 24000}
        }

        self.labels = {}
        self.buttons = {}  # Dictionary to store plus and minus buttons

        for idx, (item, data) in enumerate(self.items.items()):
            # Frame for border
            item_frame = ctk.CTkFrame(
                master=self.root,
                width=1000,
                height=70,
                corner_radius=25,
                fg_color='#FFFFFF'  # Background color white
            )
            item_frame.place(relx=0.5, rely=0.25 + idx * 0.1, anchor='center')

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
                text=f"{self.items[item]['quantity']}",
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
            command=go_back  # Add command to go back to the main menu
        )
        back_button.place(relx=0.05, rely=0.95, anchor='sw')

    def process_order(self):
        # Close the current kasir window
        self.root.destroy()

        # Create a new window for the order summary
        order_window = ctk.CTk(fg_color='#dddddd')

        # Mendapatkan ukuran layar
        screen_width = order_window.winfo_screenwidth()
        screen_height = order_window.winfo_screenheight()
        width = int(screen_width * 0.9)
        height = int(screen_height * 0.9)
        order_window.geometry(f"{width}x{height}")
        order_window.title("Ringkasan Pembelian")

        title_text = ctk.CTkLabel(
            order_window,
            text="Ringkasan Pembelian",
            font=("Helvetica", 40),
            text_color='#35522b'
        )
        title_text.place(relx=0.5, rely=0.03, anchor='n')

        # Add headers for the columns
        qty_header_label = ctk.CTkLabel(
            order_window,
            text="Qty",
            font=("Helvetica", 25, "bold"),
            text_color='#35522b'
        )
        qty_header_label.place(relx=0.1, rely=0.13, anchor='center')

        menu_header_label = ctk.CTkLabel(
            order_window,
            text="Menu",
            font=("Helvetica", 25, "bold"),
            text_color='#35522b'
        )
        menu_header_label.place(relx=0.25, rely=0.13, anchor='center')

        price_header_label = ctk.CTkLabel(
            order_window,
            text="Price",
            font=("Helvetica", 25, "bold"),
            text_color='#35522b'
        )
        price_header_label.place(relx=0.5, rely=0.13, anchor='center')

        total_header_label = ctk.CTkLabel(
            order_window,
            text="Total Harga",
            font=("Helvetica", 25, "bold"),
            text_color='#35522b'
        )
        total_header_label.place(relx=0.8, rely=0.13, anchor='center')

        total_amount = 0
        row_height = 0.2
        for idx, (item, data) in enumerate(self.items.items()):
            if (quantity := data["quantity"]) > 0:
                item_total = quantity * data["price"]
                total_amount += item_total

                # Display order details
                qty_label = ctk.CTkLabel(
                    order_window,
                    text=f"{quantity}",
                    font=("Helvetica", 25),
                    text_color='#000000'
                )
                qty_label.place(relx=0.1, rely=row_height, anchor='center')

                menu_label = ctk.CTkLabel(
                    order_window,
                    text=item,
                    font=("Helvetica", 25),
                    text_color='#000000'
                )
                menu_label.place(relx=0.2, rely=row_height, anchor='w')

                price_label = ctk.CTkLabel(
                    order_window,
                    text=f"Rp{data['price']:,}",
                    font=("Helvetica", 25),
                    text_color='#000000'
                )
                price_label.place(relx=0.5, rely=row_height, anchor='center')

                total_price_label = ctk.CTkLabel(
                    order_window,
                    text=f"Rp{item_total:,}",
                    font=("Helvetica", 25),
                    text_color='#000000'
                )
                total_price_label.place(relx=0.8, rely=row_height, anchor='center')

                row_height += 0.1

        total_label = ctk.CTkLabel(
            order_window,
            text=f"Total Pembelian: Rp{total_amount:,}",
            font=("Helvetica", 25, "bold"),
            text_color='#35522b'
        )
        total_label.place(relx=0.5, rely=0.8, anchor='center')

        # Bayar button
        bayar_button = ctk.CTkButton(
            master=order_window,
            font=('Helvetica', 20, 'bold'),
            text="Bayar",
            width=300,
            height=50,
            corner_radius=20,
            border_width=1,
            text_color='#FFE7A9',
            border_color="#35522B",
            fg_color="#35522B"
        )
        bayar_button.place(relx=0.5, rely=0.9, anchor='center')

        order_window.mainloop()

choose_menu()
