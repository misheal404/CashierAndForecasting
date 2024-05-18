import customtkinter as ctk 
import pandas as pd
import tkinter as tk
from customtkinter import CTk, CTkLabel, FontManager, CTkCanvas, CTkButton
import PIL 
from PIL import Image, ImageTk
import tkinter

total = [0,0,0]
data = {
    'Menu': ['Kopi Gula Aren', 'Kopi Susu'],
    'Price': [5.99, 4.99], 'Quantity' : [total]
}
df = pd.DataFrame(data)
order_quantities = {item: 0 for item in df['Menu']}
def add_to_total(menu_item, price):
    total.append((menu_item, price))
    order_quantities[menu_item] += 1
   
def remove_from_total(menu_item, price):
    if order_quantities[menu_item] > 0:
        total.remove((menu_item, price))
        order_quantities[menu_item] -= 1
def update_label():
    quantity_label.configure(text=f"Quantity: {order_quantities['menu_item1']}")

# Step 3: Function to handle button click
def add_to_total(menu_item, price):
    order_quantities[menu_item] += 1
    update_label()


def mine(tab, menu_item, price, y_position):
    menu = ctk.CTk(fg_color='#A9B388')
    menu.geometry(f"{500}x{500}")
    menu.title("Menu")
 
    #tabview
    drink = ctk.CTkTabview(master=menu, width=800, height=500, fg_color='#EEEEEE')
    drink.place(x=310, y=100)
    
    drink.add('tabview 1')
    drink.add('2')
    drink.set('tabview 1')
    #label
    Frame1 = ctk.CTkFrame(drink.tab('tabview 1') , width=650, height=50, corner_radius=30, bg_color='transparent', fg_color='#627254')
    Frame1.place(x=60, y=50)
    text1 = ctk.CTkLabel(Frame1, text=menu_item, 
                          width=90, height=10,
                        font=("Helvetica", 20, 'bold'),
                        fg_color='#627254', bg_color='transparent',
                        text_color='#EEEEEE' )
    text1.place(x=30, y=13)
    button1 = ctk.CTkButton(Frame1,
                            font=('Helvetica', -18, 'bold'),
                            text="+",
                            width=15,
                            height=25,
                            corner_radius=30,  # This creates the rounded effect
                            border_width=0, 
                            border_color="#EEEEEE",
                            text_color="#627254", fg_color='#EEEEEE',
                            command=lambda: add_to_total(menu_item, price))
    button2 = ctk.CTkButton(Frame1,
                            font=('Helvetica', -18, 'bold'),
                            text="-",
                            width=15,
                            height=25,
                            corner_radius=30,  # This creates the rounded effect
                            border_width=0, 
                            border_color="#EEEEEE",
                            text_color="#627254", fg_color='#EEEEEE',
                            command=lambda: remove_from_total(menu_item, price))
    button2.place(x=550, y=13)

    quantity_label = ctk.CTkLabel(Frame1, text=f"Quantity: {order_quantities['menu_item1']}")
    quantity_label.pack(pady=20)
   
    

    menu.mainloop()
mine()