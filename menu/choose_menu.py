import customtkinter as ctk
import tkinter as tk
from customtkinter import CTk, CTkLabel, FontManager, CTkCanvas, CTkButton
import PIL
from PIL import Image, ImageTk
import tkinter
def new_window():
    # Define the new window
    win = ctk.CTk(fg_color='#DDDDDD')
    win.geometry(f"{500}x{500}")
    win.title("New Window")

    #text
    text = ctk.CTkLabel(win, 
                        text="Hello, welcome to  Cafe Chronicle", 
                        font=("Helvetica", 50),
                        text_color='#627254')
    text.place(x=30, y=50)

    text2 = ctk.CTkLabel(win, 
                        text="Please Choose the menu", 
                        font=("Helvetica", 30),
                        text_color='#000000')
    text2.place(x=40, y=150)
    rounded_button = ctk.CTkButton(
    master=win,
    font=('Helvetica', 30, 'bold'),
    text="Kasir",
    width=300,
    height=100,
    corner_radius=25,  # This creates the rounded effect
    border_width=1,
    border_color="#EEEEEE",
    fg_color="#627254",  # Background color of the button
    )
    rounded_button.place(x=750, y=200)

    rounded_button2 = ctk.CTkButton(
    master=win,
    font=('Helvetica', 30, 'bold'),
    text="Data Penjualan",
    width=300,
    height=100,
    corner_radius=25,  # This creates the rounded effect
    border_width=1,
    border_color="#EEEEEE",
    fg_color="#627254",  # Background color of the button
    )
    rounded_button2.place(x=750, y=380)

    image = Image.open("CashierAndForecasting/menu/gambarmenu.png")
    photo = ImageTk.PhotoImage(image)

    # Create a canvas to place the image
    canvas = CTkCanvas(win, width=image.width, height=image.height)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.place(x=200, y=400)
    win.mainloop()
new_window()