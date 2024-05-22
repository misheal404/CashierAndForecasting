import pandas as pd
import customtkinter as ctk

# Initialize empty lists to store menu data
order_menu = []
price_o = []
quanti = []

# Create an empty DataFrame
menu = pd.DataFrame({'nama menu': order_menu, 'harga': price_o, 'qty': quanti})

def add_in(m, p):
    price_o.append(p)
    order_menu.append(m)
    # Update DataFrame
    global menu
    menu = pd.DataFrame({'nama menu': order_menu, 'harga': price_o, 'qty': quanti})

def add():
    qt = ctk.CTkEntry(frame, width=50, height=10, bg_color='#D9D9D9')
    qt.place(x=50, y=5)
    quanti.append(qt)

menus = ['ayam', 'kaki', 'lai']
menud = [80, 90, 10]

# Create the main window
frame = ctk.CTk()
frame.geometry("500x500")

# Adding quantity entry field
add_button = ctk.CTkButton(frame, width=9, height=8, text='add', command=add)
add_button.place(x=100, y=5)

# Adding menu button
menu_1_button = ctk.CTkButton(frame, width=9, height=8, text=menus[0], command=lambda: add_in(menus[0], menud[0]))
menu_1_button.place(x=0, y=5)

# Start the main loop
frame.mainloop()

# Print the updated DataFrame after closing the window
print(menu)
