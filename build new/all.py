from tkinter import Toplevel
import customtkinter as ctk
from pathlib import Path
import pandas as pd
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

#L O G I C  F U N C T I O N
def open_window_2(w1, w2):
    w1.destroy()
    w2()
def csv_all(dataframe, file_name):
    file_path = os.path.join("C:\\Users\\USER\\git rep\\CashierAndForecasting\\build new\\database", f"{file_name}.csv")
    # Check if the file already exists
    if os.path.exists(file_path):
        dataframe.to_csv(file_path, mode='a', header=False,  index=False)
    else:
        dataframe.to_csv(file_path, index=False)
def on_button_click(usn_entry, pw_entry, window1, next_func):
    # Add your button click logic here
    usn = []
    pw = []
    usn.append(usn_entry.get())
    pw.append(pw_entry.get())
    dfU = pd.DataFrame({
    'Username' : usn,
    "Password": pw,
    })
    csv_all(dfU, 'login data')
    open_window_2(window1, next_func)
    print(dfU)
    pass

menu_s = []
harga = []
total = []
amm = []

dfZ = pd.DataFrame({
    'Menu': ['Americano', 'Espresso', 'Latte', 'Cappucino', 'Cold Brew', 'Matcha Latte', 'Hazelnut Latte', 'Mocha Latte'],
    'Harga': [25000, 28000, 33000, 33000, 33000, 40000, 40000, 40000]
})

menuC = ['Americano', 'Espresso', 'Latte', 'Cappucino', 'Cold Brew', 'Matcha Latte', 'Hazelnut Latte', 'Mocha Latte']

def add(menu_num, amm_entry):
    menu_pilihan = menuC[menu_num]
    jumlah = int(amm_entry.get())
    if menu_pilihan in dfZ['Menu'].values:
        harga_pilihan = dfZ[dfZ['Menu'] == menu_pilihan]['Harga'].values[0]
        total_harga = harga_pilihan * jumlah
        menu_s.append(menu_pilihan)
        harga.append(harga_pilihan)
        amm.append(jumlah)
        total.append(total_harga)

def done(w1):
    dfA = pd.DataFrame({
        'Menu': menu_s,
        'Harga': harga,
        'Satuan': amm,
        'Total': total
    })
    csv_all(dfA, 'menu_all')
    open_window_2(w1, summary)

# GUI 

def main():
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new\assets\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("1280x720")
    window.configure(bg = "#F5EFE6")


    canvas = Canvas(
        window,
        bg = "#F5EFE6",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        827.0,
        0.0,
        1369.0,
        832.0,
        fill="#1A4D2E",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(window, sign_in),
        relief="flat"
    )
    button_1.place(
        x=101.0,
        y=27.0,
        width=70.0,
        height=30.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(window, sign_in),
        relief="flat"
    )
    button_2.place(
        x=259.0,
        y=27.0,
        width=90.0,
        height=30.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(window, sign_in),
        relief="flat"
    )
    button_3.place(
        x=440.0,
        y=27.0,
        width=165.0,
        height=30.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(window, sign_in),
        relief="flat"
    )
    button_4.place(
        x=692.0,
        y=27.0,
        width=83.0,
        height=30.0
    )

    canvas.create_text(
        101.0,
        200.0,
        anchor="nw",
        text="THE CHRONICLE",
        fill="#000000",
        font=("InknutAntiqua Bold", 50 * -1)
    )

    canvas.create_text(
        101.0,
        329.0,
        anchor="nw",
        text="grow your beloved coffee shop with us",
        fill="#000000",
        font=("Inter", 30 * -1)
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda : open_window_2(window, sign_in),
        relief="flat"
    )
    button_5.place(
        x=110.0,
        y=437.0,
        width=180.0,
        height=60.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        944.0,
        437.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()

def sign_in():
   
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new\assets\frame2")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    windowA = Tk()

    windowA.geometry("1280x720")
    windowA.configure(bg = "#FFFFFF")


    canvas = Canvas(
        windowA,
        bg = "#FFFFFF",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        683.0,
        432.0,
        image=image_image_1
    )
    

    canvas.create_rectangle(
        224.0,
        56.0,
        1056.0,
        630.0,
        fill="#EADBC8",
        outline="")

    canvas.create_text(
        557.0,
        86.0,
        anchor="nw",
        text="SIGN IN",
        fill="#1A4D2E",
        font=("Inter Bold", 60 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_rectangle(
        668.0,
        278.0, 381, 246,
        fill='#EADBC8', outline=''
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=381.0,
        y=246.0,
        width=574.0,
        height=62.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_rectangle(
        668.0,
        408.0, 381, 376, 
        fill='#EADBC8', outline=''
    )

    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=381.0,
        y=376.0,
        width=574.0,
        height=62.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0, fg='black',bg='#EADBC8',
        highlightthickness=0,
        command=lambda: on_button_click(entry_1, entry_2, windowA, home) ,
        relief="flat"
    )
    button_1.place(
        x=527.0,
        y=521.0,
        width=281.0,
        height=69.0
    )
    windowA.resizable(False, False)
    windowA.mainloop()

def home():

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\indoor\New folder (3)\build\assets\frame1")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    windowB = Tk()

    windowB.geometry("1280x720")
    windowB.configure(bg = "#F5EFE6")


    canvas = Canvas(
        windowB,
        bg = "#F5EFE6",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        827.0,
        0.0,
        1369.0,
        832.0,
        fill="#1A4D2E",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(windowB, home),
        relief="flat"
    )
    button_1.place(
        x=101.0,
        y=27.0,
        width=70.0,
        height=30.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(windowB, menu),
        relief="flat"
    )
    button_2.place(
        x=259.0,
        y=27.0,
        width=90.0,
        height=30.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(windowB, sell_home),
        relief="flat"
    )
    button_3.place(
        x=440.0,
        y=27.0,
        width=165.0,
        height=30.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(windowB, main),
        relief="flat"
    )
    button_4.place(
        x=692.0,
        y=27.0,
        width=75.0,
        height=30.0
    )

    canvas.create_text(
        97.0,
        223.0,
        anchor="nw",
        text="COFFEE CHRONICLE",
        fill="#000000",
        font=("Inter", 50 * -1)
    )

    canvas.create_text(
        101.0,
        329.0,
        anchor="nw",
        text="grow your beloved coffee shop with us",
        fill="#000000",
        font=("Inter", 30 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        944.0,
        437.0,
        image=image_image_1
    )
    windowB.resizable(False, False)
    windowB.mainloop()

def menu():


    from pathlib import Path

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new\assets\frame11")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    windowW = Tk()

    windowW.geometry("1280x720")
    windowW.configure(bg = "#E8DFCA")


    canvas = Canvas(
        windowW,
        bg = "#E8DFCA",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        5.0,
        1280.0,
        98.0,
        fill="#4F6F52",
        outline="")

    canvas.create_text(
        512.0,
        17.0,
        anchor="nw",
        text="M E N U",
        fill="#FFFFFF",
        font=("IstokWeb Bold", 40 * -1)
    )

    canvas.create_rectangle(
        51.0,
        125.0,
        235.0,
        347.0,
        fill="#F5EFE6",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        109.0,
        327.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=79.0,
        y=317.0,
        width=60.0,
        height=18.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(0, entry_1),
        relief="flat"
    )
    button_1.place(
        x=173.666748046875,
        y=315.8039245605469,
        width=36.372093200683594,
        height=20.3137264251709
    )

    canvas.create_text(
        80.0,
        286.0,
        anchor="nw",
        text="Americano",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        144.0,
        208.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        301.0,
        125.0,
        488.0,
        347.0,
        fill="#F5EFE6",
        outline="")

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        359.5,
        327.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=329.0,
        y=317.0,
        width=61.0,
        height=18.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(1, entry_2),
        relief="flat"
    )
    button_2.place(
        x=425.6666259765625,
        y=315.8039245605469,
        width=36.96511459350586,
        height=20.313724517822266
    )

    canvas.create_text(
        350.0,
        286.0,
        anchor="nw",
        text="Espresso",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        395.0,
        214.0,
        image=image_image_2
    )

    canvas.create_rectangle(
        547.0,
        128.0,
        733.0,
        347.0,
        fill="#F5EFE6",
        outline="")

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        605.5,
        327.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=575.0,
        y=317.0,
        width=61.0,
        height=18.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(2, entry_3),
        relief="flat"
    )
    button_3.place(
        x=671.0,
        y=316.2254943847656,
        width=36.76744079589844,
        height=20.039215087890625
    )

    canvas.create_text(
        610.0,
        287.0,
        anchor="nw",
        text="Latte",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        641.0,
        215.0,
        image=image_image_3
    )

    canvas.create_rectangle(
        792.0,
        128.0,
        981.0,
        347.0,
        fill="#F5EFE6",
        outline="")

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        851.5,
        327.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=820.0,
        y=317.0,
        width=63.0,
        height=18.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(3, entry_4),
        relief="flat"
    )
    button_4.place(
        x=918.6666259765625,
        y=316.2254943847656,
        width=37.558135986328125,
        height=20.039216995239258
    )

    canvas.create_text(
        830.0,
        287.0,
        anchor="nw",
        text="Cappuccino",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        887.0,
        216.0,
        image=image_image_4
    )

    canvas.create_rectangle(
        1040.0,
        125.0,
        1222.0,
        347.0,
        fill="#F5EFE6",
        outline="")

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        1132.0,
        208.0,
        image=image_image_5
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        1097.0,
        327.5,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=1067.0,
        y=317.0,
        width=60.0,
        height=19.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(4, entry_5),
        relief="flat"
    )
    button_5.place(
        x=1161.33349609375,
        y=315.8039245605469,
        width=35.97674560546875,
        height=20.3137264251709
    )

    canvas.create_text(
        1080.0,
        286.0,
        anchor="nw",
        text="Cold Brew",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    canvas.create_rectangle(
        1038.0,
        411.0,
        1220.0,
        641.0,
        fill="#F5EFE6",
        outline="")

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        1095.0,
        619.5,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=1065.0,
        y=609.0,
        width=60.0,
        height=19.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(9, entry_6),
        relief="flat"
    )
    button_6.place(
        x=1159.33349609375,
        y=608.6797485351562,
        width=35.97674560546875,
        height=21.045751571655273
    )

    canvas.create_text(
        1080.0,
        578.0,
        anchor="nw",
        text="Mocha Latte",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        1130.0,
        497.0,
        image=image_image_6
    )

    canvas.create_rectangle(
        792.0,
        411.0,
        989.0,
        641.0,
        fill="#F5EFE6",
        outline="")

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        853.5,
        619.5,
        image=entry_image_7
    )
    entry_7 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_7.place(
        x=821.0,
        y=609.0,
        width=65.0,
        height=19.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(8, entry_7),
        relief="flat"
    )
    button_7.place(
        x=923.333251953125,
        y=608.6797485351562,
        width=38.94186019897461,
        height=21.045751571655273
    )

    canvas.create_text(
        840.0,
        578.0,
        anchor="nw",
        text="Vanilla Latte",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        891.0,
        497.0,
        image=image_image_7
    )

    canvas.create_rectangle(
        547.0,
        413.0,
        733.0,
        641.0,
        fill="#F5EFE6",
        outline="")

    entry_image_8 = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(
        605.5,
        620.0,
        image=entry_image_8
    )
    entry_8 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_8.place(
        x=575.0,
        y=610.0,
        width=61.0,
        height=18.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(7, entry_8),
        relief="flat"
    )
    button_8.place(
        x=671.0001220703125,
        y=608.9607543945312,
        width=36.7674446105957,
        height=20.86274528503418
    )

    canvas.create_text(
        580.0,
        578.0,
        anchor="nw",
        text="Hazelnut Latte",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        645.0,
        504.0,
        image=image_image_8
    )

    canvas.create_rectangle(
        297.0,
        411.0,
        494.0,
        641.0,
        fill="#F5EFE6",
        outline="")

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        396.0,
        503.0,
        image=image_image_9
    )

    entry_image_9 = PhotoImage(
        file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(
        359.0,
        619.5,
        image=entry_image_9
    )
    entry_9 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_9.place(
        x=327.0,
        y=609.0,
        width=64.0,
        height=19.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(6, entry_9),
        relief="flat"
    )
    button_9.place(
        x=428.3333740234375,
        y=608.6797485351562,
        width=38.94186019897461,
        height=21.045751571655273
    )

    canvas.create_text(
        360.0,
        578.0,
        anchor="nw",
        text="Thai Tea",
        fill="#000000",
        font=("Helvetica", 18 * -1)
    )

    canvas.create_rectangle(
        45.0,
        411.0,
        235.0,
        641.0,
        fill="#F5EFE6",
        outline="")

    entry_image_10 = PhotoImage(
        file=relative_to_assets("entry_10.png"))
    entry_bg_10 = canvas.create_image(
        105.0,
        619.5,
        image=entry_image_10
    )
    entry_10 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_10.place(
        x=74.0,
        y=609.0,
        width=62.0,
        height=19.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add(5, entry_10),
        relief="flat"
    )
    button_10.place(
        x=171.6666259765625,
        y=608.6797485351562,
        width=37.55813980102539,
        height=21.045751571655273
    )

    canvas.create_text(
        80.0,
        578.0,
        anchor="nw",
        text="Matcha Latte",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        141.0,
        503.0,
        image=image_image_10
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0, bg='#4F6F52',
        command=lambda: done(windowW),
        relief="flat"
    )
    button_11.place(
        x=1106.0,
        y=20.0,
        width=148.0,
        height=41.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_12 = Button(
        image=button_image_12, bg='#4F6F52',
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_12 clicked"),
        relief="flat"
    )
    button_12.place(
        x=29.0,
        y=20.0,
        width=63.0,
        height=41.0
    )
    windowW.resizable(False, False)
    windowW.mainloop()

def summary():

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new\assets\frame4")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    WindowD = Tk()

    WindowD.geometry("1280x720")
    WindowD.configure(bg = "#F5EFE6")


    canvas = Canvas(
        WindowD,
        bg = "#F5EFE6",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        112.0,
        fill="#D1D1D1",
        outline="")

    canvas.create_text(
        514.0,
        31.0,
        anchor="nw",
        text="SUMMARY",
        fill="#000000",
        font=("InriaSans Bold", 40 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1, bg='#D1D1D1',
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(WindowD, choose_payment),
        relief="flat"
    )
    button_1.place(
        x=1011.0,
        y=31.0,
        width=285.0,
        height=56.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2, bg='#D1D1D1',
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(WindowD, menu),
        relief="flat"
    )
    button_2.place(
        x=24.0,
        y=14.0,
        width=99.0,
        height=56.0
    )

    canvas.create_rectangle(
        505.0,
        604.0,
        1173.0,
        606.0,
        fill="#000000",
        outline="")

    canvas.create_text(
        482.0,
        193.0,
        anchor="nw",
        text="Menu",
        fill="#000000",
        font=("Inder Regular", 35 * -1)
    )

    canvas.create_text(
        799.0,
        193.0,
        anchor="nw",
        text="Qty",
        fill="#000000",
        font=("Inder Regular", 35 * -1)
    )

    canvas.create_text(
        1046.0,
        193.0,
        anchor="nw",
        text="Price",
        fill="#000000",
        font=("Inder Regular", 35 * -1)
    )

    canvas.create_text(
        780.0,
        618.0,
        anchor="nw",
        text="Total :",
        fill="#000000",
        font=("Inder Regular", 35 * -1)
    )

    canvas.create_rectangle(
        88.0,
        241.0,
        382.0616455078125,
        243.0,
        fill="#000000",
        outline="")

    canvas.create_text(
        74.0,
        204.0,
        anchor="nw",
        text="name",
        fill="#000000",
        font=("InriaSans Bold", 25 * -1)
    )

    canvas.create_rectangle(
        88.0,
        356.0,
        382.0616455078125,
        358.0,
        fill="#000000",
        outline="")

    canvas.create_text(
        59.0,
        314.0,
        anchor="nw",
        text="date",
        fill="#000000",
        font=("InriaSans Bold", 25 * -1)
    )
    WindowD.resizable(False, False)
    WindowD.mainloop()

def choose_payment():

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new\assets\frame5")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    WindowE = Tk()

    WindowE.geometry("1280x720")
    WindowE.configure(bg = "#F5EFE6")


    canvas = Canvas(
        WindowE,
        bg = "#F5EFE6",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        112.0,
        fill="#D1D1D1",
        outline="")

    canvas.create_text(
        514.0,
        31.0,
        anchor="nw",
        text="PAYMENT",
        fill="#000000",
        font=("InriaSans Bold", 40 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1, bg='#D1D1D1',
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(WindowE, summary),
        relief="flat"
    )
    button_1.place(
        x=24.0,
        y=14.0,
        width=99.0,
        height=56.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(WindowE, emoney),
        relief="flat"
    )
    button_2.place(
        x=766.0,
        y=231.0,
        width=306.0,
        height=129.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(WindowE, cash),
        relief="flat"
    )
    button_3.place(
        x=147.0,
        y=214.0,
        width=317.0,
        height=146.0
    )
    WindowE.resizable(False, False)
    WindowE.mainloop()

def emoney():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new\assets\frame7")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    WindowF = Tk()

    WindowF.geometry("1280x720")
    WindowF.configure(bg = "#F5EFE6")


    canvas = Canvas(
        WindowF,
        bg = "#F5EFE6",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        112.0,
        fill="#D1D1D1",
        outline="")

    canvas.create_text(
        514.0,
        31.0,
        anchor="nw",
        text="E-MONEY",
        fill="#000000",
        font=("InriaSans Bold", 40 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1, bg='#D1D1D1',
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(WindowF, choose_payment),
        relief="flat"
    )
    button_1.place(
        x=24.0,
        y=14.0,
        width=99.0,
        height=56.0
    )

    canvas.create_text(
        92.0,
        149.0,
        anchor="nw",
        text="Name",
        fill="#000000",
        font=("InriaSerif Bold", 30 * -1)
    )

    canvas.create_text(
        95.0,
        281.0,
        anchor="nw",
        text="Date",
        fill="#000000",
        font=("InriaSerif Bold", 30 * -1)
    )

    canvas.create_text(
        752.0,
        149.0,
        anchor="nw",
        text="E-money",
        fill="#000000",
        font=("InriaSerif Bold", 30 * -1)
    )

    canvas.create_text(
        752.0,
        285.0,
        anchor="nw",
        text="Sub Total",
        fill="#000000",
        font=("InriaSerif Bold", 30 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        266.5,
        240.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=95.0,
        y=240.0,
        width=343.0,
        height=-2.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        266.5,
        370.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=95.0,
        y=370.0,
        width=343.0,
        height=-2.0
    )

    canvas.create_rectangle(
        751.0,
        237.0,
        1095.0,
        238.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        751.0,
        373.0,
        1095.0,
        374.0,
        fill="#000000",
        outline="")

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=123.0,
        y=611.0,
        width=1028.0,
        height=75.0
    )
    WindowF.resizable(False, False)
    WindowF.mainloop()

def cash():
        
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new\assets\frame6")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    WindowG = Tk()

    WindowG.geometry("1280x720")
    WindowG.configure(bg = "#F5EFE6")


    canvas = Canvas(
        WindowG,
        bg = "#F5EFE6",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    #coba

    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        112.0,
        fill="#D1D1D1",
        outline="")

    canvas.create_text(
        514.0,
        31.0,
        anchor="nw",
        text="CASH",
        fill="#000000",
        font=("InriaSans Bold", 40 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=24.0,
        y=14.0,
        width=99.0,
        height=56.0
    )

    canvas.create_text(
        92.0,
        149.0,
        anchor="nw",
        text="Name",
        fill="#000000",
        font=("InriaSerif Bold", 30 * -1)
    )

    canvas.create_text(
        95.0,
        281.0,
        anchor="nw",
        text="Date",
        fill="#000000",
        font=("InriaSerif Bold", 30 * -1)
    )

    canvas.create_text(
        752.0,
        149.0,
        anchor="nw",
        text="Sub Total",
        fill="#000000",
        font=("InriaSerif Bold", 30 * -1)
    )

    canvas.create_text(
        752.0,
        285.0,
        anchor="nw",
        text="Cash",
        fill="#000000",
        font=("InriaSerif Bold", 30 * -1)
    )

    canvas.create_text(
        752.0,
        436.0,
        anchor="nw",
        text="Return",
        fill="#000000",
        font=("InriaSerif Bold", 30 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        266.5,
        240.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=95.0,
        y=240.0,
        width=343.0,
        height=-2.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        266.5,
        370.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=95.0,
        y=370.0,
        width=343.0,
        height=-2.0
    )

    canvas.create_rectangle(
        751.0,
        237.0,
        1095.0,
        238.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        751.0,
        373.0,
        1095.0,
        374.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        751.0,
        524.0,
        1095.0,
        525.0,
        fill="#000000",
        outline="")

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=123.0,
        y=612.0,
        width=1028.0,
        height=75.0
    )
    WindowG.resizable(False, False)
    WindowG.mainloop()

def success():
        
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new\assets\frame8")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    WindowH = Tk()

    WindowH.geometry("1280x720")
    WindowH.configure(bg = "#FFFFFF")


    canvas = Canvas(
        WindowH,
        bg = "#FFFFFF",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        410.0,
        370.0,
        image=image_image_1
    )

    canvas.create_text(
        732.0,
        125.0,
        anchor="nw",
        text="PAYMENT SUCCESSFULLY !",
        fill="#093FFF",
        font=("Inika Bold", 40 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=758.0,
        y=360.0,
        width=358.85205078125,
        height=75.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=758.0,
        y=496.0,
        width=358.85205078125,
        height=75.0
    )
    WindowH.resizable(False, False)
    WindowH.mainloop()

def sell_home():
       
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new\assets\frame9")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    windowX = Tk()

    windowX.geometry("1280x720")
    windowX.configure(bg = "#FFFFFF")


    canvas = Canvas(
        windowX,
        bg = "#FFFFFF",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        382.0,
        362.0,
        image=image_image_1
    )

    canvas.create_text(
        790.0,
        116.0,
        anchor="nw",
        text="SELLING REPORT",
        fill="#000000",
        font=("InriaSans Bold", 45 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=841.0,
        y=362.0,
        width=331.21142578125,
        height=71.58737182617188
    )
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_3, bg='#D1D1D1',
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(windowX, home),
        relief="flat"
    )
    button_2.place(
        x=24.0,
        y=14.0,
        width=99.0,
        height=56.0
    )
    windowX.resizable(False, False)
    windowX.mainloop()

#menu()
menu()