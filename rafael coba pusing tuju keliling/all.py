from tkinter import Toplevel
from tkinter import messagebox
import customtkinter as ctk
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def open_window_2(w1, w2):
    w1.destroy()
    w2()
def main():
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new\assets\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()
    window.title("Cafe Chronicle-Startiing")
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

    button_imagehome = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame0\button_1.png"))
    button_home = Button(
        image=button_imagehome,
        borderwidth=0,
        highlightthickness=0,
        bg="#F5EFE6",
        command=lambda: open_window_2(window, sign_in),
        relief="flat"
    )
    button_home.place(
        x=101.0,
        y=27.0,
        width=70.0,
        height=30.0
    )

    button_imagecashier1 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame0\button_2.png"))
    button_cashier1 = Button(
        image=button_imagecashier1,
        borderwidth=0,
        highlightthickness=0,
        bg="#F5EFE6",
        command=lambda: open_window_2(window, sign_in),
        relief="flat"
    )
    button_cashier1.place(
        x=259.0,
        y=27.0,
        width=90.0,
        height=30.0
    )

    button_imagesellingreport = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame0\button_3.png"))
    button_sellingreport = Button(
        image=button_imagesellingreport,
        borderwidth=0,
        highlightthickness=0,
        bg="#F5EFE6",
        command=lambda: open_window_2(window, sign_in),
        relief="flat"
    )
    button_sellingreport.place(
        x=440.0,
        y=27.0,
        width=165.0,
        height=30.0
    )

    button_imagelogout = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame0\button_4.png"))
    button_logout = Button(
        image=button_imagelogout,
        borderwidth=0,
        highlightthickness=0,
        bg="#F5EFE6",
        command=lambda: open_window_2(window, sign_in),
        relief="flat"
    )
    button_logout.place(
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

    button_imagestartnow = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame0\button_5.png"))
    button_startnow = Button(
        image=button_imagestartnow,
        borderwidth=0,
        bg="#F5EFE6",
        highlightthickness=0,
        command=lambda : open_window_2(window, sign_in),
        relief="flat"
    )
    button_startnow.place(
        x=110.0,
        y=437.0,
        width=180.0,
        height=60.0
    )

    image_imagecoffee = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame0\image_1.png"))
    image_1 = canvas.create_image(
        944.0,
        437.0,
        image=image_imagecoffee
    )
    window.resizable(False, False)
    window.mainloop()

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, messagebox

def sign_in():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new\assets\frame2")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def create_rounded_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1 + radius, y1,
            x1 + radius, y1,
            x2 - radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1 + radius,
            x1, y1
        ]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    def validate_login():
        username = entry_usn.get()
        password = entry_password.get()
        if username != "kelompok 10":
            messagebox.showerror("Login Error", "Username salah")
        elif password != "POSIGACOR":
            messagebox.showerror("Login Error", "Password salah")
        else:
            messagebox.showinfo("Login Success", "Login successful!")
            open_home_page()

    def open_home_page():
        # Placeholder for actual function to open the home page
        # You should replace this with the actual function that opens your home page
        print("Open Home Page")
        open_window_2(windowA, home)

    windowA = Tk()
    windowA.title("Cafe Chronicle-Sign In")
    windowA.geometry("1280x720")
    windowA.configure(bg="#FFFFFF")

    canvas = Canvas(
        windowA,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_imagecafe = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame2\image_1.png"))
    image_1 = canvas.create_image(
        683.0,
        432.0,
        image=image_imagecafe
    )

    create_rounded_rectangle(
        224.0,
        56.0,
        1056.0,
        630.0,
        radius=50,
        fill="#EADBC8",
        outline=""
    )

    canvas.create_text(
        557.0,
        86.0,
        anchor="nw",
        text="SIGN IN",
        fill="#1A4D2E",
        font=("Inter Bold", 60 * -1, "bold")
    )

    entry_gambarusername = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame2\entry_1.png"))
    entry_bg_1 = canvas.create_image(
        668.0,
        278.0,
        image=entry_gambarusername
    )
    entry_usn = Entry(
        bd=0,
        bg="#4F6F52",
        fg="#000716",
        highlightthickness=0,
        font=("Arial Black", 20)
    )
    entry_usn.place(
        x=381.0,
        y=246.0,
        width=574.0,
        height=62.0
    )

    entry_gambarpasword = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame2\entry_2.png"))
    entry_bg_2 = canvas.create_image(
        668.0,
        408.0,
        image=entry_gambarpasword
    )

    entry_password = Entry(
        bd=0,
        bg="#4F6F52",
        fg="#000716",
        highlightthickness=0,
        font=("Arial Black", 20),
        show="*"
    )
    entry_password.place(
        x=381.0,
        y=376.0,
        width=574.0,
        height=62.0
    )

    button_imagelogin = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame2\button_1.png"))
    button_login = Button(
        image=button_imagelogin,
        borderwidth=0,
        highlightthickness=0,
        bg="#EADBC8",
        command=validate_login,
        relief="flat"
    )
    button_login.place(
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
    windowB.title("Cafe Chronicle-Home")
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

    button_imagehome = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame1\button_1.png"))
    button_home = Button(
        image=button_imagehome,
        bg="#F5EFE6",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(windowB, home),
        relief="flat"
    )
    button_home.place(
        x=101.0,
        y=27.0,
        width=70.0,
        height=30.0
    )

    button_imagecashier = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame1\button_2.png"))
    button_cashier = Button(
        image=button_imagecashier,
        borderwidth=0,
        bg="#F5EFE6",
        highlightthickness=0,
        command=lambda: open_window_2(windowB, menu),
        relief="flat"
    )
    button_cashier.place(
        x=259.0,
        y=27.0,
        width=90.0,
        height=30.0
    )

    button_image_sellingreport = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame1\button_3.png"))
    button_sellingreport = Button(
        image=button_image_sellingreport,
        borderwidth=0,
        bg="#F5EFE6",
        highlightthickness=0,
        command=lambda: open_window_2(windowB, sell_home),
        relief="flat"
    )
    button_sellingreport.place(
        x=440.0,
        y=27.0,
        width=165.0,
        height=30.0
    )

    button_image_logout = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame1\button_4.png"))
    button_logout = Button(
        image=button_image_logout,
        borderwidth=0,
        bg="#F5EFE6",
        highlightthickness=0,
        command=lambda: open_window_2(windowB, main),
        relief="flat"
    )
    button_logout.place(
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

    image_image_cafe = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame1\image_1.png"))
    image_cafe = canvas.create_image(
        944.0,
        437.0,
        image=image_image_cafe
    )
    windowB.resizable(False, False)
    windowB.mainloop()
    
harga_kopi = {
    "Americano": 15000,
    "Espresso": 15000,
    "Latte": 15000,
    "Cappuccino": 15000,
    "Cold Brew": 15000,
    "Matcha Latte": 20000,
    "Thai Tea": 20000,
    "Hazelnut Latte": 20000,
    "Vanilla Latte": 20000,
    "Mocha Latte": 20000
}
def menu():

    # This file was generated by the Tkinter Designer by Parth Jadhav
    # https://github.com/ParthJadhav/Tkinter-Designer


    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from datetime import datetime
    from pathlib import Path
    from tkinter import Tk, Canvas, Entry, Button, PhotoImage
    import csv
    import os
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new\assets\frame11")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    if not os.path.isfile('pembelian.csv'):
        with open('pembelian.csv', mode='w', newline=''):
            pass

    def add_to_csv(kopi, jumlah):
        with open('pembelian.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([kopi, jumlah, harga_kopi[kopi] * jumlah])
    
    def add_americano(entry):
        jumlah = int(entry.get())
        add_to_csv("Americano", jumlah)

    def add_espresso(entry):
        jumlah = int(entry.get())
        add_to_csv("Espresso", jumlah)

    def add_latte(entry):
        jumlah = int(entry.get())
        add_to_csv("Latte", jumlah)

    def add_cappuccino(entry):
        jumlah = int(entry.get())
        add_to_csv("Cappuccino", jumlah)

    def add_cold_brew(entry):
        jumlah = int(entry.get())
        add_to_csv("Cold Brew", jumlah)

    def add_matcha_latte(entry):
        jumlah = int(entry.get())
        add_to_csv("Matcha Latte", jumlah)

    def add_thai_tea(entry):
        jumlah = int(entry.get())
        add_to_csv("Thai Tea", jumlah)

    def add_hazelnut_latte(entry):
        jumlah = int(entry.get())
        add_to_csv("Hazelnut Latte", jumlah)

    def add_vanilla_latte(entry):
        jumlah = int(entry.get())
        add_to_csv("Vanilla Latte", jumlah)

    def add_mocha_latte(entry):
        jumlah = int(entry.get())
        add_to_csv("Mocha Latte", jumlah)

    def done_button_pressed():
        waktu_pembelian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add_americano(entry_americanocoffee1, waktu_pembelian)
        add_espresso(entry_espressocoffee2, waktu_pembelian)
        add_latte(entry_lattecoffee3, waktu_pembelian)
        add_cappuccino(entry_cappucinocoffee4, waktu_pembelian)
        add_cold_brew(entry_coldbrewcoffee5, waktu_pembelian)
        add_matcha_latte(entry_matchalattecoffee10, waktu_pembelian)
        add_thai_tea(entry_thaiteacoffee9, waktu_pembelian)
        add_hazelnut_latte(entry_hazelnutlattecoffee8, waktu_pembelian)
        add_vanilla_latte(entry_coffeevanillalatte7, waktu_pembelian)
        add_mocha_latte(entry_mochalattecoffee6, waktu_pembelian)

        open_window_2(windowW, summary)

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

    entry_americanoimage_coffee1 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\entry_1.png"))
    entry_americanobg_coffee1 = canvas.create_image(
        109.0,
        327.0,
        image=entry_americanoimage_coffee1
    )
    entry_americanocoffee1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_americanocoffee1.place(
        x=79.0,
        y=317.0,
        width=60.0,
        height=18.0
    )

    button_image_addamericano1 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\button_1.png"))
    button_addamericano1 = Button(
        image=button_image_addamericano1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_americano(entry_americanocoffee1),
        relief="flat"
    )
    button_addamericano1.place(
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

    image_americanoimage_coffee1 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\image_1.png"))
    image_americanocoffee1 = canvas.create_image(
        144.0,
        208.0,
        image=image_americanoimage_coffee1
    )

    canvas.create_rectangle(
        301.0,
        125.0,
        488.0,
        347.0,
        fill="#F5EFE6",
        outline="")

    entry_espressoimage_coffee2 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\entry_2.png"))
    entry_espressobg_coffee2 = canvas.create_image(
        359.5,
        327.0,
        image=entry_espressoimage_coffee2
    )
    entry_espressocoffee2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_espressocoffee2.place(
        x=329.0,
        y=317.0,
        width=61.0,
        height=18.0
    )

    button_image_addespresso2 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\button_2.png"))
    button_addespresso2 = Button(
        image=button_image_addespresso2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_espresso(entry_espressocoffee2),
        relief="flat"
    )
    button_addespresso2.place(
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

    image_espressoimage_coffee2 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\image_2.png"))
    image_coffeeespresso2 = canvas.create_image(
        395.0,
        214.0,
        image=image_espressoimage_coffee2
    )

    canvas.create_rectangle(
        547.0,
        128.0,
        733.0,
        347.0,
        fill="#F5EFE6",
        outline="")

    entry_latteimage_coffee3 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\entry_3.png"))
    entry_lattebg_coffee3 = canvas.create_image(
        605.5,
        327.0,
        image=entry_latteimage_coffee3
    )
    entry_lattecoffee3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_lattecoffee3.place(
        x=575.0,
        y=317.0,
        width=61.0,
        height=18.0
    )

    button_image_addlatte3 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\button_3.png"))
    button_addlatte3 = Button(
        image=button_image_addlatte3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_latte(entry_lattecoffee3),
        relief="flat"
    )
    button_addlatte3.place(
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

    image_lattecappucinoimage_coffee3 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\image_3.png"))
    image_coffeelattecappucino3 = canvas.create_image(
        641.0,
        215.0,
        image=image_lattecappucinoimage_coffee3
    )

    canvas.create_rectangle(
        792.0,
        128.0,
        981.0,
        347.0,
        fill="#F5EFE6",
        outline="")

    entry_cappucinoimage_coffee4 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\entry_4.png"))
    entry_cappucinobg_coffee4 = canvas.create_image(
        851.5,
        327.0,
        image=entry_cappucinoimage_coffee4
    )
    entry_cappucinocoffee4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_cappucinocoffee4.place(
        x=820.0,
        y=317.0,
        width=63.0,
        height=18.0
    )

    button_image_addcappucino4 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\button_4.png"))
    button_addcappucino4 = Button(
        image=button_image_addcappucino4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_cappuccino(entry_cappucinocoffee4),
        relief="flat"
    )
    button_addcappucino4.place(
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

    image_cappucinoimage_coffee4 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\image_4.png"))
    image_coffeecappucino4 = canvas.create_image(
        887.0,
        216.0,
        image=image_cappucinoimage_coffee4
    )

    canvas.create_rectangle(
        1040.0,
        125.0,
        1222.0,
        347.0,
        fill="#F5EFE6",
        outline="")

    image_coldbrewimage_coffee5 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\image_5.png"))
    image_coffeecoldbrew5 = canvas.create_image(
        1132.0,
        208.0,
        image=image_coldbrewimage_coffee5
    )

    entry_coldbrewimage_coffee5 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\entry_5.png"))
    entry_coldbrewbg_coffee5 = canvas.create_image(
        1097.0,
        327.5,
        image=entry_coldbrewimage_coffee5
    )
    entry_coldbrewcoffee5 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_coldbrewcoffee5.place(
        x=1067.0,
        y=317.0,
        width=60.0,
        height=19.0
    )

    button_image_addcoldbrew5 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\button_5.png"))
    button_addcoldbrew5 = Button(
        image=button_image_addcoldbrew5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_cold_brew(entry_cappucinocoffee4),
        relief="flat"
    )
    button_addcoldbrew5.place(
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

    entry_mochalatteimage_coffee6 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\entry_6.png"))
    entry_mochalattebg_coffee6 = canvas.create_image(
        1095.0,
        619.5,
        image=entry_mochalatteimage_coffee6
    )
    entry_mochalattecoffee6 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_mochalattecoffee6.place(
        x=1065.0,
        y=609.0,
        width=60.0,
        height=19.0
    )

    button_image_addmochalatte6 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\button_6.png"))
    button_addmochalatte6 = Button(
        image=button_image_addmochalatte6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_mocha_latte(entry_mochalattecoffee6),
        relief="flat"
    )
    button_addmochalatte6.place(
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

    image_mochalatteimage_coffee6 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\image_6.png"))
    image_mochalattecoffee6 = canvas.create_image(
        1130.0,
        497.0,
        image=image_mochalatteimage_coffee6
    )

    canvas.create_rectangle(
        792.0,
        411.0,
        989.0,
        641.0,
        fill="#F5EFE6",
        outline="")

    entry_vanillalatteimage_coffee7 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\entry_7.png"))
    entry_vanillalattebg_coffee7 = canvas.create_image(
        853.5,
        619.5,
        image=entry_vanillalatteimage_coffee7
    )
    entry_coffeevanillalatte7 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_coffeevanillalatte7.place(
        x=821.0,
        y=609.0,
        width=65.0,
        height=19.0
    )

    button_image_addvanillalatte7 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\button_7.png"))
    button_addvanillalatte7 = Button(
        image=button_image_addvanillalatte7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_vanilla_latte(entry_coffeevanillalatte7),
        relief="flat"
    )
    button_addvanillalatte7.place(
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

    image_vanillalatteimage_coffee7 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\image_7.png"))
    image_coffeevanillalatte7 = canvas.create_image(
        891.0,
        497.0,
        image=image_vanillalatteimage_coffee7
    )

    canvas.create_rectangle(
        547.0,
        413.0,
        733.0,
        641.0,
        fill="#F5EFE6",
        outline="")

    entry_hazelnutlatteimage_coffee8 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\entry_8.png"))
    entry_hazelnutlattebg_coffee8 = canvas.create_image(
        605.5,
        620.0,
        image=entry_hazelnutlatteimage_coffee8
    )
    entry_hazelnutlattecoffee8 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_hazelnutlattecoffee8.place(
        x=575.0,
        y=610.0,
        width=61.0,
        height=18.0
    )

    button_image_addhazelnutlatte8 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\button_8.png"))
    button_addhazelnutlatte8 = Button(
        image=button_image_addhazelnutlatte8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_hazelnut_latte(entry_hazelnutlattecoffee8),
        relief="flat"
    )
    button_addhazelnutlatte8.place(
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

    image_hazelnutlatteimage_coffee8 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\image_8.png"))
    image_hazelnutlattecoffee8 = canvas.create_image(
        645.0,
        504.0,
        image=image_hazelnutlatteimage_coffee8
    )

    canvas.create_rectangle(
        297.0,
        411.0,
        494.0,
        641.0,
        fill="#F5EFE6",
        outline="")

    image_thaiteaimage_coffee9 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\image_9.png"))
    image_thaiteacoffee9 = canvas.create_image(
        396.0,
        503.0,
        image=image_thaiteaimage_coffee9
    )

    entry_thaiteaimage_coffee9 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\entry_9.png"))
    entry_thaiteabg_coffee9 = canvas.create_image(
        359.0,
        619.5,
        image=entry_thaiteaimage_coffee9
    )
    entry_thaiteacoffee9 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_thaiteacoffee9.place(
        x=327.0,
        y=609.0,
        width=64.0,
        height=19.0
    )

    button_image_addthaitea9 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\button_9.png"))
    button_addthaitea9 = Button(
        image=button_image_addthaitea9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_thai_tea(entry_thaiteacoffee9),
        relief="flat"
    )
    button_addthaitea9.place(
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

    entry_matchalatteimage_coffee10 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\entry_10.png"))
    entry_mochalattebg_coffee10 = canvas.create_image(
        105.0,
        619.5,
        image=entry_matchalatteimage_coffee10
    )
    entry_matchalattecoffee10 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_matchalattecoffee10.place(
        x=74.0,
        y=609.0,
        width=62.0,
        height=19.0
    )

    button_image_addmatchalatte10 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\button_10.png"))
    button_addmatchalatte10 = Button(
        image=button_image_addmatchalatte10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_matcha_latte(entry_matchalattecoffee10),
        relief="flat"
    )
    button_addmatchalatte10.place(
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

    image_matchalatteimage_coffee10 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\image_10.png"))
    image_matchalattecoffee10 = canvas.create_image(
        141.0,
        503.0,
        image=image_matchalatteimage_coffee10
    )

    button_image_done11 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\button_11.png"))
    button_done11 = Button(
        image=button_image_done11,
        borderwidth=0,
        highlightthickness=0, bg='#4F6F52',
        command=lambda: open_window_2(windowW, summary),
        relief="flat"
    )
    button_done11.place(
        x=1106.0,
        y=20.0,
        width=148.0,
        height=41.0
    )

    button_image_back12 = PhotoImage(
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame11\button_12.png"))
    button_back12 = Button(
        image=button_image_back12, bg='#4F6F52',
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(windowW, home),
        relief="flat"
    )
    button_back12.place(
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame4\button_1.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame4\button_2.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame5\button_1.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame5\button_2.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame5\button_3.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame7\button_1.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame7\entry_1.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame7\entry_2.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame7\button_2.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame6\button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_window_2(WindowG, choose_payment),
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame6\entry_1.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame6\entry_2.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame6\button_2.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame8\image_1.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame8\button_1.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame8\button_2.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame9\image_1.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame9\button_1.png"))
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
        file=relative_to_assets(r"C:\Users\rafae\OneDrive\Dokumen\build\CashierAndForecasting\build new\assets\frame9\button_2.png"))
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
main()