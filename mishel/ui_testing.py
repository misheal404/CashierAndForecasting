import customtkinter as ctk 
import pandas as pd
import tkinter as tk
from customtkinter import CTk, CTkLabel, FontManager, CTkCanvas, CTkButton
import PIL 
from PIL import Image, ImageTk
import tkinter
ctk.set_appearance_mode("light")
def new_window():
    # Define the new window
    win = ctk.CTk(fg_color='#DDDDDD')
    win.geometry(f"{500}x{500}")
    win.title("New Window")

    #text
    text = ctk.CTkLabel(win, 
                        text="Cafe Chronicle", 
                        font=("Helvetica", 80),
                        text_color='#627254')
    text.place(x=200, y=200)
    #button
    rounded_button = ctk.CTkButton(
    master=win,
    font=('Helvetica', -15, 'bold'),
    text="Log in",
    width=150,
    height=50,
    corner_radius=25,  # This creates the rounded effect
    border_width=1, 
    border_color="#EEEEEE",
    fg_color="#627254", command=log_in  # Background color of the button
    )
    rounded_button.place(x=200, y=500)
    win.mainloop()

def log_in():
    
    sign_in = ctk.CTk()
    sign_in.geometry(f"{500}x{500}")
    sign_in.title("Sign in")

    #text
    kotak = ctk.CTkTabview(master=sign_in, width=700, height=1200, fg_color='#627254')
    kotak.place(x=0, y=0)
    
   
    # Create a CTkCanvas widget

    #text
    text = ctk.CTkLabel(kotak,text="Sign in", 
                        font=("Helvetica", 40),
                        fg_color='#627254',
                        text_color='#EEEEEE')
    text.place(x=300, y=150)

    #input usn and pw
    usn = ctk.CTkEntry(kotak, width=400, height=50, corner_radius=0, fg_color= '#DDDDDD', text_color='#627254', placeholder_text="Enter  username")
    usn.place(x=160, y=300)
    pw = ctk.CTkEntry(kotak, width=400, height=50, corner_radius=0, fg_color= '#DDDDDD', text_color='#627254', placeholder_text="Enter  password")
    pw.place(x=160, y=400)

    #button login
    rounded_button = ctk.CTkButton(
    master=kotak,
    font=('Helvetica', -15, 'bold'),
    text="Log in",
    width=150,
    height=50,
    corner_radius=25,  # This creates the rounded effect
    border_width=1,
    border_color="#EEEEEE",
    fg_color="#627254",  # Background color of the button
    )
    rounded_button.place(x=160, y=500)

    sign_in.mainloop()
log_in()


def menu():
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

    text1 = ctk.CTkLabel(Frame1, text="Kopi gula aren", 
                          width=90, height=10,
                        font=("Helvetica", 20, 'bold'),
                        fg_color='#627254', bg_color='transparent',
                        text_color='#EEEEEE' )
  
    button1 = ctk.CTkButton(Frame1,
                            font=('Helvetica', -18, 'bold'),
                            text="+",
                            width=15,
                            height=25,
                            corner_radius=30,  # This creates the rounded effect
                            border_width=0, 
                            border_color="#EEEEEE",
                            text_color="#627254", fg_color='#EEEEEE')
    button2 = ctk.CTkButton(Frame1,
                            font=('Helvetica', -18, 'bold'),
                            text="-",
                            width=15,
                            height=25,
                            corner_radius=30,  # This creates the rounded effect
                            border_width=0, 
                            border_color="#EEEEEE",
                            text_color="#627254", fg_color='#EEEEEE')
    Frame1.place(x=60, y=50)
    text1.place(x=30, y=13)
    button2.place(x=560, y=13)
    button1.place(x=590, y=13)

    Frame2 = ctk.CTkFrame(drink.tab('tabview 1') , width=650, height=50, corner_radius=30, bg_color='transparent', fg_color='#627254')
    Frame2.place(x=60, y=130)
    text2 = ctk.CTkLabel(Frame2, text="Kopi susu aren", 
                          width=90, height=10,
                        font=("Helvetica", 20, 'bold'),
                        fg_color='#627254', bg_color='transparent',
                        text_color='#EEEEEE' )
    Frame1.place(x=60, y=50)
    Frame2.place(x=60, y=130)
    text2.place(x=30, y=15)
    text1.place(x=30, y=13)
    button2.place(x=520, y=13)
    button1.place(x=590, y=13)


    #button

    menu.mainloop()