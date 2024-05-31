import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os,sys
from datetime import datetime
import subprocess

# Load user data
users_df = pd.read_csv('chronicle/data/users.csv')  # Ensure this CSV has 'username' and 'password' columns


class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configure(fg_color='#f5efe6')

        self.title("Chronicle App")
        self.geometry("1280x720")

        self.current_page = None
        self.selected_items = {}
        self.customer_var = tk.StringVar()
        self.cash_var = tk.StringVar()
        self.emoney_var = tk.StringVar()

        self.show_home_page()

    def quit_program(self):
        sys.exit()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def load_image(self, img_path):
        try:
            image = Image.open(img_path)
            image = image.resize((80 * 3, 80 * 3), Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            return image
        except Exception as e:
            print(f"Error loading image from {img_path}: {e}")

    def show_home_page(self):
        self.clear_window()

        title = ctk.CTkLabel(self, text="THE CHRONICLE", font=("Times New Roman", 71, 'bold'), text_color="#000000")
        title.place(relx=0.05, rely=0.28, anchor='nw')

        subtitle = ctk.CTkLabel(self, text="Grow your beloved coffee shop with us", font=("Helvetica", 40), text_color="#000000")
        subtitle.place(relx=0.05, rely=0.45, anchor='nw')

        start_button = ctk.CTkButton(self, text="Start Now", corner_radius=20, fg_color='#1A4D2E', text_color='#f5efe6',
                                     width=220, height=63, font=("Helvetica", 35), command=self.show_login_page)
        start_button.place(relx=0.06, rely=0.65, anchor='nw')

        home_button = ctk.CTkButton(self, text="Home", fg_color='#f5efe6', text_color='#000000',
                                    width=150, height=50, font=("Helvetica", 25), command=self.show_login_page)
        home_button.place(relx=0.05, rely=0, anchor='nw')

        cashier_button = ctk.CTkButton(self, text="Cashier", fg_color='#f5efe6', text_color='#000000',
                                       width=150, height=50, font=("Helvetica", 25), command=self.show_login_page)
        cashier_button.place(relx=0.20, rely=0, anchor='nw')

        report_button = ctk.CTkButton(self, text="Selling Report", fg_color='#f5efe6', text_color='#000000',
                                      width=150, height=50, font=("Helvetica", 25), command=self.show_login_page)
        report_button.place(relx=0.35, rely=0, anchor='nw')

        exit_button = ctk.CTkButton(self, text="Exit", fg_color='#f5efe6', text_color='#000000',
                                    width=150, height=50, font=("Helvetica", 25), command=self.quit_program)
        exit_button.place(relx=0.52, rely=0, anchor='nw')

        green_box = ctk.CTkFrame(self, width=450, height=730, fg_color="#1A4D2E")
        green_box.place(relx=1.0, rely=0.0, anchor='ne')

        image = Image.open("chronicle/assets/kopi1.png")
        image = image.resize((351, 564), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(self, image=image,text='')
        image_label.place(relx=0.648, rely=0.25, anchor='nw')

        image = Image.open("chronicle/assets/kopi2.png")
        image = image.resize((115, 171), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(self, image=image,text='')
        image_label.place(relx=0.588, rely=0.25, anchor='nw')

    def show_login_page(self):
        self.clear_window()

        self.bg_image = Image.open("chronicle/assets/bg.png")
        self.bg_image = self.bg_image.resize((self.winfo_width(), self.winfo_height()), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_canvas = tk.Canvas(self, width=self.winfo_width(), height=self.winfo_height())
        self.bg_canvas.create_image(0, 0, image=self.bg_photo, anchor=tk.NW)
        self.bg_canvas.pack(fill="both", expand=True)

        self.frame = ctk.CTkFrame(self, fg_color="#EADBC8", corner_radius=0, width=832, height=574)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.6, relheight=0.6)

        label = ctk.CTkLabel(self.frame, text="SIGN IN", font=("Inter", 60, 'bold'), text_color="#1A4D2E")
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.username_var = tk.StringVar(value="Enter your username")
        self.password_var = tk.StringVar(value="Enter your password")

        username_entry = ctk.CTkEntry(self.frame, text_color='#E8DFCA', textvariable=self.username_var, fg_color='#4F6F52',
                                      width=598, height=64, font=('Times New Roman', 25, 'bold'))
        username_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        password_entry = ctk.CTkEntry(self.frame, text_color='#E8DFCA', textvariable=self.password_var, fg_color='#4F6F52',
                                      width=598, height=64, font=('Times New Roman', 25, 'bold'))
        password_entry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        login_button = ctk.CTkButton(self.frame, text="Login", command=self.check_login, font=('Inter', 40, 'bold'), fg_color='#B5C18E', text_color="#4f6f52", width=281, height=69, corner_radius=20)
        login_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        back_button = ctk.CTkButton(self.frame, text="<<", fg_color='#EADBC8', text_color="#4f6f52", font=('Inter', 40), command=self.show_home_page)
        back_button.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

        username_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Enter your username"))
        username_entry.bind("<FocusOut>", lambda event: self.set_placeholder(event, "Enter your username"))
        password_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Enter your password", is_password=True))
        password_entry.bind("<FocusOut>", lambda event: self.set_placeholder(event, "Enter your password", is_password=True))

    def clear_placeholder(self, event, placeholder, is_password=False):
        entry = event.widget
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            if is_password:
                entry.config(show="*")

    def set_placeholder(self, event, placeholder, is_password=False):
        entry = event.widget
        if entry.get() == "":
            entry.insert(0, placeholder)
            if is_password:
                entry.config(show="")

    def check_login(self):
        username = self.username_var.get()
        password = self.password_var.get()
        if any((users_df['username'] == username) & (users_df['password'] == password)):
            self.show_choose_menu_page()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")

    def show_choose_menu_page(self):
        self.clear_window()

        title = ctk.CTkLabel(self, text="THE CHRONICLE", font=("Times New Roman", 71, 'bold'), text_color="#000000")
        title.place(relx=0.05, rely=0.28, anchor='nw')

        subtitle = ctk.CTkLabel(self, text="Grow your beloved coffee shop with us", font=("Helvetica", 40), text_color="#000000")
        subtitle.place(relx=0.05, rely=0.45, anchor='nw')

        home_button = ctk.CTkButton(self, text="Home", fg_color='#f5efe6', text_color='#000000',
                                    width=150, height=50, font=("Helvetica", 25), command=self.show_choose_menu_page)
        home_button.place(relx=0.05, rely=0, anchor='nw')

        cashier_button = ctk.CTkButton(self, text="Cashier", fg_color='#f5efe6', text_color='#000000',
                                       width=150, height=50, font=("Helvetica", 25), command=self.show_list_menu_page)
        cashier_button.place(relx=0.20, rely=0, anchor='nw')

        report_button = ctk.CTkButton(self, text="Selling Report", fg_color='#f5efe6', text_color='#000000',
                                      width=150, height=50, font=("Helvetica", 25), command=self.show_report_page)
        report_button.place(relx=0.35, rely=0, anchor='nw')

        exit_button = ctk.CTkButton(self, text="Log out", fg_color='#f5efe6', text_color='#000000',
                                    width=150, height=50, font=("Helvetica", 25), command=self.show_login_page)
        exit_button.place(relx=0.52, rely=0, anchor='nw')

        green_box = ctk.CTkFrame(self, width=450, height=730, fg_color="#1A4D2E")
        green_box.place(relx=1.0, rely=0.0, anchor='ne')

        image = Image.open("chronicle/assets/kopi1.png")
        image = image.resize((351, 564), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(self, image=image,text='')
        image_label.place(relx=0.648, rely=0.25, anchor='nw')

        image = Image.open("chronicle/assets/kopi2.png")
        image = image.resize((115, 171), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(self, image=image,text='')
        image_label.place(relx=0.588, rely=0.25, anchor='nw')

    def show_list_menu_page(self):
        
        self.selected_items.clear()
        self.clear_window()

        self.frame = ctk.CTkFrame(self, fg_color="#4F6F52", corner_radius=0, width=1280, height=90)
        self.frame.place(relx=0, rely=0, anchor=tk.NW)

        title = ctk.CTkLabel(self.frame, text="LIST MENU", font=("Inter", 40, 'bold'), text_color="#E8DFCA")
        title.place(relx=0.5, rely=0.145, anchor=tk.N)

        back_button = ctk.CTkButton(self.frame, text="<<", fg_color="#4F6F52", text_color="#E8DFCA", font=('Inter', 40), command=self.show_choose_menu_page)
        back_button.place(relx=0, rely=0.14, anchor=tk.NW)

        done_button = ctk.CTkButton(self.frame, text="DONE", fg_color="#4F6F52", text_color="#E8DFCA", font=('Inter', 40), command=self.summary_page)
        done_button.place(relx=0.85, rely=0.14, anchor=tk.NW)

        self.tabs = ctk.CTkTabview(self, fg_color='#f5efe6', text_color='#e8dfca', width=1280, height=670,
                                   segmented_button_fg_color='#f5efe6', segmented_button_selected_color='#4F6F52',
                                   segmented_button_unselected_color='#B5C18E')
        self.tabs.place(relx=0.5, rely=0.09, anchor=tk.N)

        drinks_tab = self.tabs.add("Drinks")
        foods_tab = self.tabs.add("Foods")

        sample_menu = {
            "Drinks": [
                ("Americano", "chronicle/assets/image_11.png", 21000),
                ("Espresso", "chronicle/assets/image_12.png", 20000),
                ("Latte", "chronicle/assets/image_13.png", 21000),
                ("Cappuccino", "chronicle/assets/image_4.png", 24000),
                ("Cold Brew", "chronicle/assets/image_5.png", 22000),
                ("Matcha Latte", "chronicle/assets/image_10.png", 24000),
                ("Thai Tea", "chronicle/assets/image_9.png", 18000),
                ("Hazelnut Latte", "chronicle/assets/image_8.png", 22000),
                ("Vanilla Latte", "chronicle/assets/image_7.png", 22000),
                ("Mocha Latte", "chronicle/assets/image_6.png", 22000)
            ],
            "Foods": [
                ("Chicken Sandwich", "chronicle/assets/chick.png", 32000),
                ("Banana Cake", "chronicle/assets/cake.png", 30000),
                ("Tuna Sandwich", "chronicle/assets/Tuna.png", 35000),
                ("Vanilla Cake", "chronicle/assets/vanilla.png", 30000),
                ("Chocolate Muffin", "chronicle/assets/Chocolate.png", 28000),
                ("Blueberry Muffin", "chronicle/assets/Blueberry.png", 28000),
                ("Almond Croissant", "chronicle/assets/AlmondCr.png", 27000),
                ("Butter Croissant", "chronicle/assets/ButterCr.png", 24000),
                ("Cheese Danish", "chronicle/assets/Danish.png", 26000),
                ("Cromboloni", "chronicle/assets/crombo.png", 27000)
            ]
        }

        for tab, items in sample_menu.items():
            row_index = 0
            col_index = 0
            for item, img_path, price in items:
                if col_index >= 5:
                    col_index = 0
                    row_index += 1
                image = self.load_image(img_path)
                self.add_menu_item(tab, item, image, price, row_index, col_index)
                col_index += 1

    def add_menu_item(self, tab_name, item_name, image, price, row_index, col_index):
        tab = self.tabs.tab(tab_name)

        item_frame = ctk.CTkFrame(tab, fg_color='#ffffff', corner_radius=10, width=300 * 3, height=200 * 3)
        item_frame.grid(row=row_index, column=col_index, padx=40, pady=25)

        image_label = ctk.CTkLabel(item_frame, image=image, text='')
        image_label.image = image
        image_label.grid(row=0, column=0, padx=10, pady=5)

        item_label = ctk.CTkLabel(item_frame, text=item_name, font=("Helvetica", 22, 'bold'), text_color="#4F6F52")
        item_label.grid(row=1, column=0, pady=6)

        quantity_frame = ctk.CTkFrame(item_frame, fg_color='#EADBC8', width=14 * 3, height=14 * 3)
        quantity_frame.grid(row=3, column=0, pady=6)

        minus_button = ctk.CTkButton(quantity_frame, text="-", fg_color='#B5C18E', text_color="#4F6F52", width=10 * 3, height=10 * 3, font=("Helvetica", 14, 'bold'))
        minus_button.grid(row=0, column=0, padx=15)

        quantity_label = ctk.CTkLabel(quantity_frame, text="0", font=("Helvetica", 22, 'bold'), text_color="#4F6F52")
        quantity_label.grid(row=0, column=1, padx=15)

        plus_button = ctk.CTkButton(quantity_frame, text="+", fg_color='#B5C18E', text_color="#4F6F52", width=10 * 3, height=10 * 3, font=("Helvetica", 14, 'bold'))
        plus_button.grid(row=0, column=2, padx=15)

        plus_button.configure(command=lambda: self.update_quantity(item_name, price, quantity_label, 1))
        minus_button.configure(command=lambda: self.update_quantity(item_name, price, quantity_label, -1))

    def update_quantity(self, item_name, price, label, delta):
        current_qty = int(label.cget("text"))
        new_qty = current_qty + delta
        if new_qty < 0:
            new_qty = 0
        label.configure(text=str(new_qty))
        self.update_selected_items(item_name, price, new_qty)

    def update_selected_items(self, item_name, price, quantity):
        if quantity > 0:
            self.selected_items[item_name] = (item_name, price, quantity, price * quantity)
        else:
            if item_name in self.selected_items:
                del self.selected_items[item_name]

    def summary_page(self):
        self.clear_window()

        self.frame = ctk.CTkFrame(self, fg_color="#D1D1D1", corner_radius=0, width=1280, height=90)
        self.frame.place(relx=0, rely=0, anchor=tk.NW)

        title = ctk.CTkLabel(self.frame, text="SUMMARY", font=("Inter", 40, 'bold'), text_color="#4F6F52")
        title.place(relx=0.5, rely=0.145, anchor=tk.N)

        back_button = ctk.CTkButton(self.frame, text="<<", fg_color="#D1D1D1", text_color="#4F6F52", font=('Inter', 40), command=self.show_list_menu_page)
        back_button.place(relx=0, rely=0.14, anchor=tk.NW)

        total_price = 0

        header_font = ("Helvetica", 22, 'bold')
        header_color = "#4F6F52"
        headers = ["Qty", "Menu", "Price", "Subtotal"]
        header_positions = [0.1, 0.3, 0.6, 0.8]

        for idx, header in enumerate(headers):
            header_label = ctk.CTkLabel(self, text=header, font=header_font, text_color=header_color)
            header_label.place(relx=header_positions[idx], rely=0.2, anchor=tk.W)

        if self.selected_items:
            total_price = 0
            row_index = 0

            for item_name, (name, price, quantity, total) in self.selected_items.items():
                y_position = 0.25 + row_index * 0.04

                quantity_label = ctk.CTkLabel(self, text=f"{quantity}", font=("Helvetica", 20), text_color="#4F6F52")
                quantity_label.place(relx=0.1, rely=y_position, anchor=tk.W)

                name_label = ctk.CTkLabel(self, text=name, font=("Helvetica", 20), text_color="#4F6F52")
                name_label.place(relx=0.3, rely=y_position, anchor=tk.W)

                price_label = ctk.CTkLabel(self, text=f"Rp.{price:,}", font=("Helvetica", 20), text_color="#4F6F52")
                price_label.place(relx=0.6, rely=y_position, anchor=tk.W)

                total_label = ctk.CTkLabel(self, text=f"Rp.{total:,}", font=("Helvetica", 20), text_color="#4F6F52")
                total_label.place(relx=0.8, rely=y_position, anchor=tk.W)

                row_index += 1
                total_price += total

            total_price_label = ctk.CTkLabel(self, text=f"Total Price: Rp.{total_price:,}", font=("Inter", 30), text_color="#4F6F52")
            total_price_label.place(relx=0.5, rely=0.25 + row_index * 0.04 + 0.05, anchor=tk.N)

            proceed_button = ctk.CTkButton(self, text="PROCEED TO PAYMENT", fg_color="#4F6F52", text_color="#D1D1D1", font=('Inter', 30), command=self.payment_page)
            proceed_button.place(relx=0.5, rely=0.2 + row_index * 0.05 + 0.15, anchor=tk.N)
        else:
            no_items_label = ctk.CTkLabel(self, text="No items selected", font=("Inter", 30), text_color="#4F6F52")
            no_items_label.place(relx=0.5, rely=0.3, anchor=tk.N)

    def payment_page(self):
        
        self.clear_window()

        self.frame = ctk.CTkFrame(self, fg_color="#D1D1D1", corner_radius=0, width=1280, height=90)
        self.frame.place(relx=0, rely=0, anchor=tk.NW)

        title = ctk.CTkLabel(self.frame, text="PAYMENT", font=("Inter", 40, 'bold'), text_color="#4F6F52")
        title.place(relx=0.5, rely=0.145, anchor=tk.N)

        back_button = ctk.CTkButton(self.frame, text="<<", fg_color="#D1D1D1", text_color="#4F6F52", font=('Inter', 40), command=self.summary_page)
        back_button.place(relx=0, rely=0.14, anchor=tk.NW)

        cash_button = ctk.CTkButton(self, text="CASH", fg_color="#40A578", text_color="#D1D1D1", width=300, height=120,
                                    corner_radius=25, font=('Inter', 40), anchor='center', command=self.cash_page)
        cash_button.place(relx=0.35, rely=0.5, anchor=tk.CENTER)

        emoney_button = ctk.CTkButton(self, text="E-MONEY", fg_color="#40A578", text_color="#D1D1D1",
                                      corner_radius=25, font=('Inter', 40), width=300, height=120, anchor='center', command=self.emoney_page)
        emoney_button.place(relx=0.65, rely=0.5, anchor=tk.CENTER)

    def cash_page(self):
        self.clear_window()
        self.emoney_var.set("")

        self.frame = ctk.CTkFrame(self, fg_color="#D1D1D1", corner_radius=0, width=1280, height=90)
        self.frame.place(relx=0, rely=0, anchor=tk.NW)

        title = ctk.CTkLabel(self.frame, text="CASH PAYMENT", font=("Inter", 40, 'bold'), text_color="#4F6F52")
        title.place(relx=0.5, rely=0.145, anchor=tk.N)

        back_button = ctk.CTkButton(self.frame, text="<<", fg_color="#D1D1D1", text_color="#4F6F52", font=('Inter', 40), command=self.payment_page)
        back_button.place(relx=0, rely=0.14, anchor=tk.NW)

        cust_name = ctk.CTkLabel(self, text='Customer Name:', font=("Inter", 30, 'bold'), text_color="#4F6F52")
        cust_name.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        self.customer_var = tk.StringVar()
        customer = ctk.CTkEntry(self, textvariable=self.customer_var, font=("Inter", 30), width=300)
        customer.place(relx=0.5, rely=0.22, anchor=tk.CENTER)

        total_amount = sum(total for _, _, _, total in self.selected_items.values())
        total_label = ctk.CTkLabel(self, text=f"Total: Rp.{total_amount:,}", font=("Inter", 30, 'bold'), text_color="#4F6F52")
        total_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        cash_label = ctk.CTkLabel(self, text='Cash:', font=("Inter", 30, 'bold'), text_color="#4F6F52")
        cash_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.cash_var = tk.StringVar()
        cash_entry = ctk.CTkEntry(self, textvariable=self.cash_var, font=("Inter", 30), width=300)
        cash_entry.place(relx=0.5, rely=0.47, anchor=tk.CENTER)

        calculate_button = ctk.CTkButton(self, text="Calculate Change", fg_color="#40A578", text_color="#D1D1D1",
                                         font=('Inter', 30), command=self.calculate_change)
        calculate_button.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        self.change_label = ctk.CTkLabel(self, text="", font=("Inter", 30), text_color="#4F6F52")
        self.change_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        proceed = ctk.CTkButton(self, text="Done", fg_color="#40A578", text_color="#D1D1D1",
                                font=('Inter', 30), command=self.print_nota)
        proceed.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def calculate_change(self):
        try:
            total_amount = sum(total for _, _, _, total in self.selected_items.values())
            cash_amount = float(self.cash_var.get())
            change = int(cash_amount - total_amount)
            if change < 0:
                self.change_label.configure(text="Insufficient cash", text_color="red")
            else:
                self.change_label.configure(text=f"Change: Rp.{change:,}", text_color="#4F6F52")
        except ValueError:
            self.change_label.configure(text="Invalid cash amount", text_color="red")

    def emoney_page(self):
        self.clear_window()
        self.emoney_var.set("")

        self.frame = ctk.CTkFrame(self, fg_color="#D1D1D1", corner_radius=0, width=1280, height=90)
        self.frame.place(relx=0, rely=0, anchor=tk.NW)

        title = ctk.CTkLabel(self.frame, text="E-MONEY PAYMENT", font=("Inter", 40, 'bold'), text_color="#4F6F52")
        title.place(relx=0.5, rely=0.145, anchor=tk.N)

        self.customer_var = tk.StringVar()
        customer = ctk.CTkEntry(self, textvariable=self.customer_var, font=("Inter", 30), width=300)
        customer.place(relx=0.5, rely=0.22, anchor=tk.CENTER)

        cust_name = ctk.CTkLabel(self, text='Customer Name:', font=("Inter", 30, 'bold'), text_color="#4F6F52")
        cust_name.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        total_amount = sum(total for _, _, _, total in self.selected_items.values())
        total_label = ctk.CTkLabel(self, text=f"Total: Rp.{total_amount:,}", font=("Inter", 30, 'bold'), text_color="#4F6F52")
        total_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        emoney = ctk.CTkLabel(self, text='Choose E-Money:', font=("Inter", 30, 'bold'), text_color="#4F6F52")
        emoney.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.emoney_var = tk.StringVar()
        options = ["OVO", "GoPay", "Dana"]
        rely_value = 0.47
        for option in options:
            radio = ctk.CTkRadioButton(self, text=option, variable=self.emoney_var, value=option, text_color="#4F6F52", font=('Inter', 30))
            radio.place(relx=0.45, rely=rely_value, anchor=tk.NW)
            rely_value += 0.09

        back_button = ctk.CTkButton(self.frame, text="<<", fg_color="#D1D1D1", text_color="#4F6F52", font=('Inter', 40), command=self.payment_page)
        back_button.place(relx=0, rely=0.14, anchor=tk.NW)

        complete_payment_button = ctk.CTkButton(self, text="COMPLETE PAYMENT", fg_color="#4F6F52", text_color="#D1D1D1", font=('Inter', 30), command=self.print_nota)
        complete_payment_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def print_nota(self):
        self.clear_window()

        self.frame = ctk.CTkFrame(self, fg_color="#4F6F52", corner_radius=0, width=1280, height=90)
        self.frame.place(relx=0, rely=0, anchor=tk.NW)

        title = ctk.CTkLabel(self.frame, text="PAYMENT SUCCEESFULL", font=("Inter", 40, 'bold'), text_color="#E8DFCA")
        title.place(relx=0.5, rely=0.145, anchor=tk.N)

        print_button = ctk.CTkButton(self, text="PRINT NOTA", fg_color="#4F6F52", text_color="#D1D1D1", font=('Inter', 30), command=self.print_receipt)
        print_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        menu_button = ctk.CTkButton(self, text="MAIN MENU", fg_color="#4F6F52", text_color="#D1D1D1", font=('Inter', 30), command=self.show_choose_menu_page)
        menu_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        logout_button = ctk.CTkButton(self, text="LOG OUT", fg_color="#ff0000", text_color="#D1D1D1", font=('Inter', 30), command=self.show_login_page)
        logout_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        

    def print_receipt(self):
        folder_name = 'chronicle'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        receipts_folder = os.path.join(folder_name, 'receipts')
        if not os.path.exists(receipts_folder):
            os.makedirs(receipts_folder)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        receipt_filename = os.path.join(receipts_folder, f"receipt_{timestamp}.pdf")

        c = canvas.Canvas(receipt_filename, pagesize=letter)
        c.setFont("Helvetica", 12)

        # Tambahkan logo di sudut kiri atas
        logo_path = "chronicle/assets/logo.png"  # Ganti dengan path logo perusahaan Anda
        c.drawImage(logo_path, 50, 700, width=100, height=100)

        c.drawString(180, 750, "THE CHRONICLE")
        c.drawString(180, 735, "Gd.1 Lt.3 No.1304")
        c.drawString(180, 720, "Teknik Industri,Fakultas Teknik")
        c.drawString(180, 705, "="*40)
        now = datetime.now()
        c.drawString(180, 690, f"Datetime: {timestamp}")

        customer_name = self.customer_var.get()
        c.drawString(180, 675, f"Customer: {customer_name}")
        c.drawString(180, 660, "-"*70)

        row_height = 640
        for item_name, (name, price, quantity, total) in self.selected_items.items():
            c.drawString(180, row_height, f"{name} x{quantity}")
            c.drawString(400, row_height, f"Rp.{total:,.0f}")
            row_height -= 15

        c.drawString(180, row_height, "-"*70)

        total_amount = sum(total for _, _, _, total in self.selected_items.values())
        c.drawString(180, row_height - 20, f"Total: Rp.{total_amount:,.0f}")

        payment_method = "Cash" if self.emoney_var.get() == "" else "E-Money"
        

        if payment_method == "Cash":
            cash_amount = float(self.cash_var.get())
            change = cash_amount - total_amount
            c.drawString(180, row_height - 40, f"Change: Rp.{change:,.0f}")
            c.drawString(180, row_height - 60, f"Payment Method: {payment_method}")

        

        if payment_method.startswith("E-Money"):
            emoney_details = self.emoney_var.get()
            c.drawString(180, row_height - 65, f"E-Money Type: {emoney_details}")
            c.drawString(180, row_height - 40, f"Payment Method: {payment_method}")

        c.drawString(180, row_height-90, "Coffee cheers to brew-tiful souls like you!")

        c.save()
        subprocess.Popen(['start', receipt_filename], shell=True)
        messagebox.showinfo("Receipt Printed", f"Receipt has been printed successfully!\nFile saved as: {receipt_filename}")
        self.save_to_csv(customer_name, total_amount, payment_method)

    def save_to_csv(self, customer_name, total_amount, payment_method):
        folder_name = 'chronicle'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        data_folder = os.path.join(folder_name, 'data')
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

        data_filename = os.path.join(data_folder, 'sales_data.csv')

        rows = []
        for item_name, (name, price, quantity, total) in self.selected_items.items():
            rows.append({
                "Customer": customer_name,
                "Item": name,
                "Price": price,
                "Quantity": quantity,
                "Subtotal": total,
                "Payment Method": payment_method,
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

        df = pd.DataFrame(rows)
        if os.path.exists(data_filename):
            df.to_csv(data_filename, mode='a', header=False, index=False)
        else:
            df.to_csv(data_filename, mode='w', header=True, index=False)

        messagebox.showinfo("Data Saved", f"Sales data has been saved successfully!\nFile saved as: {data_filename}")

    


    def show_report_page(self):
        self.clear_window()

        self.frame = ctk.CTkFrame(self, fg_color="#4F6F52", corner_radius=0, width=1280, height=90)
        self.frame.place(relx=0, rely=0, anchor=tk.NW)

        title = ctk.CTkLabel(self.frame, text="SELLING REPORT", font=("Inter", 40, 'bold'), text_color="#E8DFCA")
        title.place(relx=0.5, rely=0.145, anchor=tk.N)

        back_button = ctk.CTkButton(self.frame, text="<<", fg_color="#4F6F52", text_color="#E8DFCA", font=('Inter', 40), command=self.show_choose_menu_page)
        back_button.place(relx=0, rely=0.14, anchor=tk.NW)

        daily_button = ctk.CTkButton(self, text="Daily Report", fg_color="#4F6F52", text_color="#D1D1D1", font=('Inter', 30), command=lambda: self.load_and_display_data(process_type='daily'))
        daily_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        daily_button = ctk.CTkButton(self, text="Monthly Report", fg_color="#4F6F52", text_color="#D1D1D1", font=('Inter', 30), command=lambda: self.load_and_display_data(process_type='monthly'))
        daily_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        

    def load_and_process_csv(self, filename, process_type='daily'):
        df = pd.read_csv(filename)
        df['Date'] = pd.to_datetime(df['Date'])

        if process_type == 'daily':
            today = datetime.today().date()
            df['Date'] = df['Date'].dt.date
            df = df[df['Date'] == today]  # Filter for today's date
            aggregated_data = df.groupby(['Item']).agg({'Quantity': 'sum', 'Subtotal': 'sum'}).reset_index()
        elif process_type == 'monthly':
            this_month = datetime.today().strftime('%Y-%m')
            df['Month'] = df['Date'].dt.strftime('%Y-%m')
            df = df[df['Month'] == this_month]  # Filter for the current month
            aggregated_data = df.groupby(['Month', 'Item']).agg({'Quantity': 'sum', 'Subtotal': 'sum'}).reset_index()
        else:
            raise ValueError("Invalid process type. Please specify 'daily' or 'monthly'.")

        return aggregated_data

    def load_and_display_data(self, process_type='daily'):
        self.clear_window()
        filename = 'chronicle/data/sales_data.csv'
        try:
            data = self.load_and_process_csv(filename, process_type)
        except (FileNotFoundError, ValueError, KeyError) as e:
            error_label = tk.Label(self, text=f"Error: {str(e)}", fg="red")
            error_label.pack()
            return

        if process_type == 'daily':
            table_title = "Daily Sales Data"
        elif process_type == 'monthly':
            table_title = "Monthly Sales Data"
        else:
            raise ValueError("Invalid process type. Please specify 'daily' or 'monthly'.")

        table_frame = ctk.CTkFrame(self)
        table_frame.pack(fill='both', expand=True, padx=20, pady=20)

        title_label = tk.Label(table_frame, text=table_title, font=("Helvetica", 16))
        title_label.pack()

        tree = ttk.Treeview(table_frame)
        tree["columns"] = ["Item", "Quantity", "Subtotal"]
        tree["show"] = "headings"

        tree.heading("Item", text="Item")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Subtotal", text="Subtotal")

        tree.column("Item", width=200)
        tree.column("Quantity", width=100)
        tree.column("Subtotal", width=100)

        total_quantity = 0
        total_subtotal = 0

        for _, row in data.iterrows():
            tree.insert("", "end", values=[row["Item"], row["Quantity"], row["Subtotal"]])
            total_quantity += row["Quantity"]
            total_subtotal += row["Subtotal"]

        # Insert the total row at the end
        tree.insert("", "end", values=["Total", total_quantity, total_subtotal], tags=('total',))

        tree.tag_configure('total', background='lightgrey', font=('Helvetica', 12, 'bold'))

        tree.pack(fill='both', expand=True)

        back_button = ctk.CTkButton(self, text="BACK", fg_color="#FF0000", text_color="#D1D1D1", font=('Inter', 30), command=self.show_report_page)
        back_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        graph_button = ctk.CTkButton(self, text="SHOW GRAPH", fg_color="#004FB9", text_color="#D1D1D1", font=('Inter', 30), command=lambda: self.display_data_graph(filename,process_type))
        graph_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        # Membuat frame untuk menampung Treeview
    def display_data_graph(self,filename, process_type='daily'):
        try:
            data = self.load_and_process_csv(filename, process_type)
        except FileNotFoundError:
            print("Error: File not found.")
            return
        except ValueError as e:
            print(f"Error: {e}")
            return

        if process_type == 'daily':
            title = "Daily Sales Data"
        elif process_type == 'monthly':
            title = "Monthly Sales Data"
        else:
            print("Error: Invalid process type. Please specify 'daily' or 'monthly'.")
            return

        plt.bar(data['Item'], data['Subtotal'])
        plt.xlabel('Item')
        plt.ylabel('Subtotal')
        plt.title(title)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    


if __name__ == "__main__":
    app = Application()
    app.mainloop()
