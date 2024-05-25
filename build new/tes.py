import tkinter as tk
import customtkinter as ctk
def add_entry(entry_list, entry_var):
    # Retrieve text from the entry widget
    entry_text = entry_var.get()
    
    # Append the text to the list
    entry_list.append(entry_text)

#
list = []
win = ctk.CTk(fg_color='#DDDDDD')
win.geometry(f"{500}x{500}")
win.title("New Window")

button = ctk.CTkEntry(win, height=300, width=100)
button.place(x=100, y=100)
add_button = ctk.CTkButton(win, text="Add Entry", command=lambda : add_entry(list, button))
add_button.pack(pady=20)

print(list)
win.mainloop()


    