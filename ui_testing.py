
import customtkinter as ctk
import tkinter as tk
from customtkinter import CTk, CTkLabel, FontManager, CTkCanvas, CTkButton
import PIL 
import tkinter
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
    fg_color="#627254",  # Background color of the button
    )
    rounded_button.place(x=200, y=500)
    win.mainloop()

new_window()