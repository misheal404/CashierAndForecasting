import pandas as pd
import customtkinter as ctk
oerder_menu = []
price_o = []
quanti = []
menu = pd.DataFrame({'nama menu' : [oerder_menu], 'harga' : [price_o],'qty' : [quanti]})

def add_in(m, p):
    price_o.append(p)
    oerder_menu.append(m)


menus= ['ayam', 'kaki', 'lai']
menud = [80, 90, 10]

harga = [10, 20, 5]
frame = ctk.CTk()
frame.geometry(f"{500}x{500}")

menu1 = 'ayam'
harga1 = 900
def add():
    qt = ctk.CTkEntry(frame, width= 50, height=10, bg_color='#D9D9D9')
    qt.place(x=50, y=5)
    quanti.append(qt)
ad = ctk.CTkButton(frame, width=9, height=8, text='add', command=add() )
ad.place(x=100, y=5)
menu_1 = ctk.CTkButton(frame, width=9, height=8, text=menu1, command=add_in(menus[0], menud[0]))
menu_1.place(x=0, y=5)

frame.mainloop()
print(menu)