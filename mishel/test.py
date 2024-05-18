import customtkinter as ctk 
import pandas as pd
import tkinter as tk
from customtkinter import CTk, CTkLabel, FontManager, CTkCanvas, CTkButton
import PIL 
from PIL import Image, ImageTk
import tkinter
ctk.set_appearance_mode("light")

def increase_count():
    current_value = int(count_label["text"])
    count_label.configure(text=str(current_value + 1))

# Function to decrease the count
def decrease_count():
    current_value = int(count_label["text"])
    count_label.configure(text=str(current_value - 1))

def mine():
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
    text1 = ctk.CTkLabel(Frame1, text="Kopi gula aren", 
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
                            text_color="#627254", fg_color='#EEEEEE', command=increase_count)
    button1.place(x=590, y=13)
    button2 = ctk.CTkButton(Frame1,
                            font=('Helvetica', -18, 'bold'),
                            text="-",
                            width=15,
                            height=25,
                            corner_radius=30,  # This creates the rounded effect
                            border_width=0, 
                            border_color="#EEEEEE",
                            text_color="#627254", fg_color='#EEEEEE', command=decrease_count)
    button2.place(x=560, y=13)


    count_label = ctk.CTkLabel(
    Frame1,
    font=('Helvetica', -18, 'bold'),
    text="0",
    width=50,
    height=25,
    corner_radius=30,
    fg_color="#EEEEEE"
)
    count_label.place(x=580, y=13)
    text1 = ctk.CTkLabel(Frame1, text="Kopi gula aren", 
                          width=90, height=10,
                        font=("Helvetica", 20, 'bold'),
                        fg_color='#627254', bg_color='transparent',
                        text_color='#EEEEEE' )

    text1.place(x=30, y=15)

    menu.mainloop()
mine()