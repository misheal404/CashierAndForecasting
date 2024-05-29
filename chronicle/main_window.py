import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load user data
users_df = pd.read_csv('chronicle/users.csv')  # Ensure this CSV has 'username' and 'password' columns

class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configure(fg_color='#f5efe6')

        self.title("Chronicle App")
        self.geometry("1280x720")

        self.current_page = None
        self.selected_items = {}

        self.show_home_page()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()
    def load_image(self, img_path):
        try:
            image = Image.open(img_path)
            image = image.resize((80*3, 80*3), Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            return image
        except Exception as e:
            print(f"Error loading image from {img_path}: {e}")

    def show_home_page(self):
        self.clear_window()

        title = ctk.CTkLabel(self, text="THE CHRONICLE", font=("Times New Roman", 71,'bold'),text_color="#000000")
        title.place(relx=0.05, rely=0.28, anchor='nw')

        subtitle = ctk.CTkLabel(self, text="grow your beloved coffe shop with us", font=("Helvetica", 40),text_color="#000000")
        subtitle.place(relx=0.05, rely=0.45, anchor='nw')
        
        start_button = ctk.CTkButton(self, text="start now",corner_radius=20,fg_color='#1A4D2E',text_color='#f5efe6',
                                     width=220,height=63,font=("Helvetica", 35), command=self.show_login_page)
        start_button.place(relx=0.06, rely=0.65, anchor='nw')
        home_button = ctk.CTkButton(self, text="Home",fg_color='#f5efe6',text_color='#000000',
                                     width=150,height=50,font=("Helvetica", 25), command=self.show_login_page)
        home_button.place(relx=0.05, rely=0, anchor='nw')
        cashier_button = ctk.CTkButton(self, text="Cashier",fg_color='#f5efe6',text_color='#000000',
                                     width=150,height=50,font=("Helvetica", 25), command=self.show_login_page)
        cashier_button.place(relx=0.20, rely=0, anchor='nw')
        report_button = ctk.CTkButton(self, text="Selling Report",fg_color='#f5efe6',text_color='#000000',
                                     width=150,height=50,font=("Helvetica", 25), command=self.show_login_page)
        report_button.place(relx=0.35, rely=0, anchor='nw')
        exit_button = ctk.CTkButton(self, text="Exit",fg_color='#f5efe6',text_color='#000000',
                                     width=150,height=50,font=("Helvetica", 25), command=self.show_login_page)
        exit_button.place(relx=0.52, rely=0, anchor='nw')

        green_box = ctk.CTkFrame(self, width=450, height=730, fg_color="#1A4D2E")
        green_box.place(relx=1.0, rely=0.0, anchor='ne')

        image = Image.open("D:\PROKOM\chronicle\image_3.png")
        image = image.resize((351, 564), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(self, image=image,text='')
        image_label.place(relx=0.648, rely=0.25, anchor='nw')

        image = Image.open("D:\PROKOM\chronicle\image_4.png")
        image = image.resize((115, 171), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(self, image=image,text='')
        image_label.place(relx=0.588, rely=0.25, anchor='nw')
        

    # Create a canvas to place the imag

    def show_login_page(self):
        self.clear_window()

        # Load the background image
        self.bg_image = Image.open("chronicle/image_1.png")
        self.bg_image = self.bg_image.resize((self.winfo_width(), self.winfo_height()), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a canvas and place the image
        self.bg_canvas = tk.Canvas(self, width=self.winfo_width(), height=self.winfo_height())
        self.bg_canvas.create_image(0, 0, image=self.bg_photo, anchor=tk.NW)
        self.bg_canvas.pack(fill="both", expand=True)

        # Create a frame with background color
        self.frame = ctk.CTkFrame(self, fg_color="#EADBC8",corner_radius=0,width=832,height=574)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.6, relheight=0.6)

        # Create labels and entries within the frame
        label = ctk.CTkLabel(self.frame, text="SIGN IN", font=("Inter", 60, 'bold'), text_color="#1A4D2E")
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.username_var = tk.StringVar(value="Enter your username")
        self.password_var = tk.StringVar(value="Enter your password")

        
        username_entry = ctk.CTkEntry(self.frame, text_color='#E8DFCA', textvariable=self.username_var, fg_color='#4F6F52',
                                      width=598,height=64,
                                      font=('Times New Roman', 25, 'bold'))
        username_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        
        password_entry = ctk.CTkEntry(self.frame, text_color='#E8DFCA', textvariable=self.password_var, fg_color='#4F6F52',
                                      width=598,height=64,
                                      font=('Times New Roman', 25, 'bold'))
        password_entry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        login_button = ctk.CTkButton(self.frame, text="login", command=self.check_login, font=('Inter', 40, 'bold'), fg_color='#B5C18E', text_color="#4f6f52",width=281,height=69,corner_radius=20)
        login_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        back_button = ctk.CTkButton(self.frame, text="<<", fg_color='#EADBC8', text_color="#4f6f52", font=('Inter', 40), command=self.show_home_page)
        back_button.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

        # Bind events to the entry widgets
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
            messagebox.showerror("Login Failed", "Username atau password salah")

    def show_choose_menu_page(self):
        self.clear_window()

        title = ctk.CTkLabel(self, text="THE CHRONICLE", font=("Times New Roman", 71,'bold'),text_color="#000000")
        title.place(relx=0.05, rely=0.28, anchor='nw')

        subtitle = ctk.CTkLabel(self, text="grow your beloved coffe shop with us", font=("Helvetica", 40),text_color="#000000")
        subtitle.place(relx=0.05, rely=0.45, anchor='nw')

        home_button = ctk.CTkButton(self, text="Home",fg_color='#f5efe6',text_color='#000000',
                                     width=150,height=50,font=("Helvetica", 25), command=self.show_home_page)
        home_button.place(relx=0.05, rely=0, anchor='nw')
        cashier_button = ctk.CTkButton(self, text="Cashier",fg_color='#f5efe6',text_color='#000000',
                                     width=150,height=50,font=("Helvetica", 25), command=self.show_list_menu_page)
        cashier_button.place(relx=0.20, rely=0, anchor='nw')
        report_button = ctk.CTkButton(self, text="Selling Report", fg_color='#f5efe6', text_color='#000000',
                                  width=150, height=50, font=("Helvetica", 25), command=self.show_data_penjualan_page)
        report_button.place(relx=0.35, rely=0, anchor='nw')
        exit_button = ctk.CTkButton(self, text="Log out", fg_color='#f5efe6', text_color='#000000',
                                    width=150, height=50, font=("Helvetica", 25), command=self.show_login_page)
        exit_button.place(relx=0.52, rely=0, anchor='nw')
        green_box = ctk.CTkFrame(self, width=450, height=730, fg_color="#1A4D2E")
        green_box.place(relx=1.0, rely=0.0, anchor='ne')

        image = Image.open("D:\PROKOM\chronicle\image_3.png")
        image = image.resize((351, 564), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(self, image=image,text='')
        image_label.place(relx=0.648, rely=0.25, anchor='nw')

        image = Image.open("D:\PROKOM\chronicle\image_4.png")
        image = image.resize((115, 171), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(self, image=image,text='')
        image_label.place(relx=0.588, rely=0.25, anchor='nw')

    def show_list_menu_page(self):
        self.clear_window()

        self.frame = ctk.CTkFrame(self, fg_color="#4F6F52", corner_radius=0, width=1280, height=90)
        self.frame.place(relx=0, rely=0, anchor=tk.NW)

        # Create the title label and place it at the top of the frame
        title = ctk.CTkLabel(self.frame, text="LIST MENU", font=("Inter", 40, 'bold'), text_color="#E8DFCA")
        title.place(relx=0.5, rely=0.145, anchor=tk.N)

        back_button = ctk.CTkButton(self.frame, text="<<", fg_color="#4F6F52", text_color="#E8DFCA", font=('Inter', 40), command=self.show_home_page)
        back_button.place(relx=0, rely=0.14, anchor=tk.NW)

        done_button = ctk.CTkButton(self.frame, text="DONE", fg_color="#4F6F52", text_color="#E8DFCA", font=('Inter', 40),command=self.summary_page)
        done_button.place(relx=0.85, rely=0.14, anchor=tk.NW)

        self.tabs = ctk.CTkTabview(self, fg_color='#f5efe6', text_color='#e8dfca', width=1280, height=670,
                                segmented_button_fg_color='#f5efe6', segmented_button_selected_color='#4F6F52',
                                segmented_button_unselected_color='#B5C18E')
        self.tabs.place(relx=0.5, rely=0.09, anchor=tk.N)

        # Adding tabs correctly
        drinks_tab = self.tabs.add("Drinks")
        foods_tab = self.tabs.add("Foods")

        # Add sample menu items
        sample_menu = {
            "Drinks": [
                ("Americano", "D:/PROKOM/chronicle/assets/image_11.png", 21000),
                ("Espresso", "D:/PROKOM/chronicle/assets/image_12.png", 20000),
                ("Latte", "D:/PROKOM/chronicle/assets/image_13.png", 21000),
                ("Cappuccino", "D:/PROKOM/chronicle/assets/image_4.png", 24000),
                ("Cold Brew", "D:/PROKOM/chronicle/assets/image_5.png", 22000),
                ("Matcha Latte", "D:/PROKOM/chronicle/assets/image_10.png", 24000),
                ("Thai Tea", "D:/PROKOM/chronicle/assets/image_9.png", 18000),
                ("Hazelnut Latte", "D:/PROKOM/chronicle/assets/image_8.png", 22000),
                ("Vanilla Latte", "D:/PROKOM/chronicle/assets/image_7.png", 22000),
                ("Mocha Latte", "D:/PROKOM/chronicle/assets/image_6.png", 22000)
            ],
            "Foods": [
                ("Chicken Sandwich", "D:\PROKOM\chronicle\image_5.png", 32000),
                ("Banana Cake", "D:\PROKOM\chronicle\image_5.png", 30000),
                ("Tuna Sandwich", "D:\PROKOM\chronicle\image_5.png", 35000),
                ("Vanilla Cake", "D:\PROKOM\chronicle\image_5.png", 30000),
                ("Chocolate Muffin", "D:\PROKOM\chronicle\image_5.png", 28000),
                ("Blueberry Muffin", "D:\PROKOM\chronicle\image_5.png", 28000),
                ("Almond Croissant", "D:\PROKOM\chronicle\image_5.png", 27000),
                ("Butter Croissant", "D:\PROKOM\chronicle\image_5.png", 24000),
                ("Cheese Danish", "D:\PROKOM\chronicle\image_5.png", 26000),
                ("Cromboloni", "D:\PROKOM\chronicle\image_5.png", 27000)
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

        item_frame = ctk.CTkFrame(tab, fg_color='#ffffff', corner_radius=10, width=300*3, height=200*3)
        item_frame.grid(row=row_index, column=col_index, padx=40, pady=25)

        image_label = ctk.CTkLabel(item_frame, image=image, text='')
        image_label.image = image
        image_label.grid(row=0, column=0, padx=10, pady=5)

        item_label = ctk.CTkLabel(item_frame, text=item_name, font=("Helvetica", 22, 'bold'), text_color="#4F6F52")
        item_label.grid(row=1, column=0, pady=6)

        quantity_frame = ctk.CTkFrame(item_frame, fg_color='#EADBC8', width=14*3, height=14*3)
        quantity_frame.grid(row=3, column=0, pady=6)

        minus_button = ctk.CTkButton(quantity_frame, text="-", fg_color='#B5C18E', text_color="#4F6F52", width=10*3, height=10*3, font=("Helvetica", 14, 'bold'))
        minus_button.grid(row=0, column=0, padx=15)

        quantity_label = ctk.CTkLabel(quantity_frame, text="0", font=("Helvetica", 22, 'bold'), text_color="#4F6F52")
        quantity_label.grid(row=0, column=1, padx=15)

        plus_button = ctk.CTkButton(quantity_frame, text="+", fg_color='#B5C18E', text_color="#4F6F52", width=10*3, height=10*3, font=("Helvetica", 14, 'bold'))
        plus_button.grid(row=0, column=2, padx=15)

        plus_button.configure(command=lambda: self.update_quantity(item_name, price, quantity_label, 1))
        minus_button.configure(command=lambda: self.update_quantity(item_name, price, quantity_label, -1))

    def update_quantity(self, item_name, price, label, delta):
        current_qty = int(label.cget("text"))
        new_qty = current_qty + delta
        if new_qty < 0:
            new_qty = 0
        label.configure(text=str(new_qty))

        # Update selected items when quantity changes
        self.update_selected_items(item_name, price, new_qty)

    def update_selected_items(self, item_name, price, quantity):
        if quantity > 0:
            self.selected_items[item_name] = (item_name, price, quantity, price * quantity)
        else:
            # Remove item if quantity becomes 0
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

        # Headers
        header_font = ("Helvetica", 22, 'bold')
        header_color = "#4F6F52"
        headers = ["Qty", "Menu", "Price", "Subtotal"]
        header_positions = [0.1, 0.3, 0.6, 0.8]

        for idx, header in enumerate(headers):
            header_label = ctk.CTkLabel(self, text=header, font=header_font, text_color=header_color)
            header_label.place(relx=header_positions[idx], rely=0.2, anchor=tk.W)

        # Check if there are selected items
        if self.selected_items:
            # Initialize total price
            total_price = 0

            # Create labels for displaying each order
            row_index = 0  # Start from row 0 since rel_y will be adjusted
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

            # Display the total price
            total_price_label = ctk.CTkLabel(self, text=f"Total Price: Rp.{total_price:,}", font=("Inter", 30), text_color="#4F6F52")
            total_price_label.place(relx=0.5, rely=0.25 + row_index * 0.04 + 0.05, anchor=tk.N)

            # Button to proceed to payment page
            proceed_button = ctk.CTkButton(self, text="PROCEED TO PAYMENT", fg_color="#4F6F52", text_color="#D1D1D1", font=('Inter', 30), command=self.payment_page)
            proceed_button.place(relx=0.5, rely=0.2 + row_index * 0.05 + 0.15, anchor=tk.N)
        else:
            # Display message if no items are selected
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

        cash_button = ctk.CTkButton(self, text="CASH  ", fg_color="#40A578", text_color="#D1D1D1",width=300,height=120,
                                    corner_radius=25,font=('Inter', 40),anchor='left', command=self.cash_page)
        cash_button.place(relx=0.35, rely=0.5, anchor=tk.CENTER)

        emoney_button = ctk.CTkButton(self, text="E-MONEY", fg_color="#40A578", text_color="#D1D1D1", 
                                    corner_radius=25,font=('Inter', 40),width=300,height=120,anchor='left',command=self.emoney_page)
        emoney_button.place(relx=0.65, rely=0.5, anchor=tk.CENTER)
        
        

    def cash_page(self):
        self.clear_window()

        self.frame = ctk.CTkFrame(self, fg_color="#D1D1D1", corner_radius=0, width=1280, height=90)
        self.frame.place(relx=0, rely=0, anchor=tk.NW)

        title = ctk.CTkLabel(self.frame, text="CASH PAYMENT", font=("Inter", 40, 'bold'), text_color="#4F6F52")
        title.place(relx=0.5, rely=0.145, anchor=tk.N)

        back_button = ctk.CTkButton(self.frame, text="<<", fg_color="#D1D1D1", text_color="#4F6F52", font=('Inter', 40), command=self.payment_page)
        back_button.place(relx=0, rely=0.14, anchor=tk.NW)

        total_amount = sum(total for _, _, _, total in self.selected_items.values())
        total_label = ctk.CTkLabel(self, text=f"Total: Rp.{total_amount:,}", font=("Inter", 40, 'bold'), text_color="#4F6F52")
        total_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # Entry for cash amount
        self.cash_var = tk.StringVar()
        cash_entry = ctk.CTkEntry(self, textvariable=self.cash_var, font=("Inter", 30), width=300)
        cash_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Button to calculate change
        calculate_button = ctk.CTkButton(self, text="Calculate Change", fg_color="#40A578", text_color="#D1D1D1",
                                         font=('Inter', 30), command=self.calculate_change)
        calculate_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        
        # Label to display the change
        self.change_label = ctk.CTkLabel(self, text="", font=("Inter", 30), text_color="#4F6F52")
        self.change_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

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

        self.frame = ctk.CTkFrame(self, fg_color="#D1D1D1", corner_radius=0, width=1280, height=90)
        self.frame.place(relx=0, rely=0, anchor=tk.NW)

        title = ctk.CTkLabel(self.frame, text="E-MONEY PAYMENT", font=("Inter", 40, 'bold'), text_color="#4F6F52")
        title.place(relx=0.5, rely=0.145, anchor=tk.N)

        back_button = ctk.CTkButton(self.frame, text="<<", fg_color="#D1D1D1", text_color="#4F6F52", font=('Inter', 40), command=self.payment_page)
        back_button.place(relx=0, rely=0.14, anchor=tk.NW)

        instruction_label = ctk.CTkLabel(self, text="Please scan the QR code to complete the payment.", font=("Inter", 30), text_color="#4F6F52")
        instruction_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # Simulated QR code image
        qr_image = self.load_image("D:/PROKOM/chronicle/assets/qr_code.png")
        qr_label = ctk.CTkLabel(self, image=qr_image, text='')
        qr_label.image = qr_image
        qr_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        def complete_emoney_payment():
            messagebox.showinfo("Payment Successful", "Payment completed successfully.")
            self.show_home_page()

        complete_payment_button = ctk.CTkButton(self, text="COMPLETE PAYMENT", fg_color="#4F6F52", text_color="#D1D1D1", font=('Inter', 30), command=complete_emoney_payment)
        complete_payment_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def print_receipt(self, change):
        receipt_filename = "receipt.pdf"
        c = canvas.Canvas(receipt_filename, pagesize=letter)
        width, height = letter

        c.setFont("Helvetica", 12)
        c.drawString(100, height - 40, "The Chronicle Receipt")
        c.line(50, height - 45, width - 50, height - 45)

        y = height - 60
        for item_name, (name, price, quantity, total) in self.selected_items.items():
            c.drawString(50, y, f"{name} (x{quantity}) - Rp.{total:,}")
            y -= 20

        c.drawString(50, y - 20, f"Total: Rp.{sum(item[3] for item in self.selected_items.values()):,}")
        c.drawString(50, y - 40, f"Change: Rp.{change:,}")
        c.save()

        messagebox.showinfo("Receipt Saved", f"Receipt has been saved as {receipt_filename}")


        


    

    
        
        

        




    def show_report_page(self):
        self.clear_window()

        label = ctk.CTkLabel(self, text="Laporan Penjualan", font=("Arial", 24))
        label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        data_penjualan_button = ctk.CTkButton(self, text="Data Penjualan", command=self.show_data_penjualan_page)
        data_penjualan_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        grafik_button = ctk.CTkButton(self, text="Grafik", command=self.show_grafik_page)
        grafik_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        back_button = ctk.CTkButton(self, text="Back", command=self.show_choose_menu_page)
        back_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_data_penjualan_page(self):
        self.clear_window()

        label = ctk.CTkLabel(self, text="Data Penjualan", font=("Arial", 24))
        label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Add your data display here

        back_button = ctk.CTkButton(self, text="Back", command=self.show_report_page)
        back_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    def show_grafik_page(self):
        self.clear_window()

        label = ctk.CTkLabel(self, text="Grafik Penjualan", font=("Arial", 24))
        label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Add your graph display here

        back_button = ctk.CTkButton(self, text="Back", command=self.show_report_page)
        back_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
