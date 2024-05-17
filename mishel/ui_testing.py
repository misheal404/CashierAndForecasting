import customtkinter as ctk 
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
    # Create a CTkCanvas widget
    canvas = ctk.CTkCanvas(sign_in, width=800, height=600)
    canvas.pack(fill="both", expand=True)

    # Define the coordinates for the square
    x1, y1 = 100, 100  # Top-left corner
    x2, y2 = 200, 200  # Bottom-right corner

    # Add a square (rectangle with equal sides) to the canvas
    square = canvas.create_rectangle(x1, y1, x2, y2, fill="#627254", outline="#627254", width=1000)

    #text
    text = ctk.CTkLabel(sign_in,text="Sign in", 
                        font=("Helvetica", 40),
                        fg_color='#627254',
                        text_color='#EEEEEE')
    text.place(x=300, y=150)

    #input usn and pw
    usn = ctk.CTkEntry(sign_in, width=400, height=50, corner_radius=0, fg_color= '#DDDDDD', text_color='#627254', placeholder_text="Enter  username")
    usn.place(x=160, y=300)
    pw = ctk.CTkEntry(sign_in, width=400, height=50, corner_radius=0, fg_color= '#DDDDDD', text_color='#627254', placeholder_text="Enter  password")
    pw.place(x=160, y=400)

    #button login
    rounded_button = ctk.CTkButton(
    master=sign_in,
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

def menu():
    mena = ctk.CTk()
    mena.geometry(f"{500}x{500}")
    mena._fg_color('#EEEEEE')
    mena.title("Menu")

    # Load the image
    image = Image.open("CashierAndForecasting/mishel/s.png")
    photo = ImageTk.PhotoImage(image)

    header = ctk.CTkLabel(mena,text="Menu list", 
                          width=90, height=10,
                        font=("Helvetica", 20),
                        fg_color='#627254', bg_color='#EEEEEE',
                        text_color='#EEEEEE')
    header.place(x=300, y=150)
    mena.mainloop()

def mine():
    menu = ctk.CTk()
    menu.geometry(f"{500}x{500}")
    menu.title("Menu")
    # Load the image
    F1 = ctk.CTkFrame(menu, width=1000, height=50, bg_color='#627254')
    F1.place(x=20, y=20)
    menu_1 = ctk.CTkButton(master=F1,
    font=('Helvetica', -15, 'bold'),
    text="Log in",
    width=30,
    height=30,
    corner_radius=30,  # This creates the rounded effect
    border_width=0, 
    border_color="#EEEEEE",
    fg_color="#627254")
    menu_1.place(x=500, y=20)
    menu.mainloop()
mine()