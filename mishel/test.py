
def login():
    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new fullscreen copy\assets\frame0")


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
        command=lambda: print("button_1 clicked"),
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
        command=lambda: print("button_2 clicked"),
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
        command=lambda: print("button_3 clicked"),
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
        command=lambda: print("button_4 clicked"),
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
        command=sign_in(),
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
        
    # This file was generated by the Tkinter Designer by Parth Jadhav
    # https://github.com/ParthJadhav/Tkinter-Designer


    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\indoor\New folder (3)\build\assets\frame2")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("1280x720")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
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
    entry_bg_1 = canvas.create_image(
        668.0,
        278.0,
        image=entry_image_1
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
    entry_bg_2 = canvas.create_image(
        668.0,
        408.0,
        image=entry_image_2
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
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=527.0,
        y=521.0,
        width=281.0,
        height=69.0
    )
    window.resizable(False, False)
    window.mainloop()

def home():
        
    # This file was generated by the Tkinter Designer by Parth Jadhav
    # https://github.com/ParthJadhav/Tkinter-Designer


    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\indoor\New folder (3)\build\assets\frame1")


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
        command=lambda: print("button_1 clicked"),
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
        command=lambda: print("button_2 clicked"),
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
        command=lambda: print("button_3 clicked"),
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
        command=lambda: print("button_4 clicked"),
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
    window.resizable(False, False)
    window.mainloop()

def menu():
        
    # This file was generated by the Tkinter Designer by Parth Jadhav
    # https://github.com/ParthJadhav/Tkinter-Designer


    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\indoor\New folder (3)\build\assets\frame3")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("1280x1455")
    window.configure(bg = "#E8DFCA")


    canvas = Canvas(
        window,
        bg = "#E8DFCA",
        height = 1455,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        361.0,
        192.0,
        619.0,
        498.0,
        fill="#F5EFE6",
        outline="")

    canvas.create_rectangle(
        361.0,
        555.0,
        619.0,
        861.0,
        fill="#F5EFE6",
        outline="")

    canvas.create_rectangle(
        361.0,
        918.0,
        619.0,
        1224.0,
        fill="#F5EFE6",
        outline="")

    canvas.create_rectangle(
        61.0,
        192.0,
        319.0,
        498.0,
        fill="#F5EFE6",
        outline="")

    canvas.create_rectangle(
        61.0,
        555.0,
        319.0,
        861.0,
        fill="#F5EFE6",
        outline="")

    canvas.create_rectangle(
        61.0,
        918.0,
        319.0,
        1224.0,
        fill="#F5EFE6",
        outline="")

    canvas.create_rectangle(
        661.0,
        192.0,
        919.0,
        498.0,
        fill="#F5EFE6",
        outline="")

    canvas.create_rectangle(
        661.0,
        555.0,
        919.0,
        861.0,
        fill="#F5EFE6",
        outline="")

    canvas.create_rectangle(
        661.0,
        918.0,
        919.0,
        1224.0,
        fill="#F5EFE6",
        outline="")

    canvas.create_rectangle(
        961.0,
        192.0,
        1219.0,
        498.0,
        fill="#F5EFE6",
        outline="")

    canvas.create_rectangle(
        961.0,
        555.0,
        1219.0,
        861.0,
        fill="#F5EFE6",
        outline="")

    canvas.create_rectangle(
        961.0,
        918.0,
        1219.0,
        1224.0,
        fill="#F5EFE6",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        191.0,
        669.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        191.0,
        1040.0,
        image=image_image_2
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        442.11111068725586,
        470.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=399.0,
        y=456.0,
        width=86.22222137451172,
        height=26.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        442.11111068725586,
        833.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=399.0,
        y=819.0,
        width=86.22222137451172,
        height=26.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        442.11111068725586,
        1196.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=399.0,
        y=1182.0,
        width=86.22222137451172,
        height=26.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        142.11111068725586,
        470.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=99.0,
        y=456.0,
        width=86.22222137451172,
        height=26.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        142.11111068725586,
        833.0,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=99.0,
        y=819.0,
        width=86.22222137451172,
        height=26.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        142.11111068725586,
        1196.0,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=99.0,
        y=1182.0,
        width=86.22222137451172,
        height=26.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        742.1111106872559,
        470.0,
        image=entry_image_7
    )
    entry_7 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_7.place(
        x=699.0,
        y=456.0,
        width=86.22222137451172,
        height=26.0
    )

    entry_image_8 = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(
        742.1111106872559,
        833.0,
        image=entry_image_8
    )
    entry_8 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_8.place(
        x=699.0,
        y=819.0,
        width=86.22222137451172,
        height=26.0
    )

    entry_image_9 = PhotoImage(
        file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(
        742.1111106872559,
        1196.0,
        image=entry_image_9
    )
    entry_9 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_9.place(
        x=699.0,
        y=1182.0,
        width=86.22222137451172,
        height=26.0
    )

    entry_image_10 = PhotoImage(
        file=relative_to_assets("entry_10.png"))
    entry_bg_10 = canvas.create_image(
        1042.1111106872559,
        470.0,
        image=entry_image_10
    )
    entry_10 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_10.place(
        x=999.0,
        y=456.0,
        width=86.22222137451172,
        height=26.0
    )

    entry_image_11 = PhotoImage(
        file=relative_to_assets("entry_11.png"))
    entry_bg_11 = canvas.create_image(
        1042.1111106872559,
        833.0,
        image=entry_image_11
    )
    entry_11 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_11.place(
        x=999.0,
        y=819.0,
        width=86.22222137451172,
        height=26.0
    )

    entry_image_12 = PhotoImage(
        file=relative_to_assets("entry_12.png"))
    entry_bg_12 = canvas.create_image(
        1042.1111106872559,
        1197.0,
        image=entry_image_12
    )
    entry_12 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_12.place(
        x=999.0,
        y=1183.0,
        width=86.22222137451172,
        height=26.0
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
        x=533.0,
        y=455.0,
        width=51.0,
        height=28.0
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
        x=533.0,
        y=818.0,
        width=51.0,
        height=28.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=533.0,
        y=1181.0,
        width=51.0,
        height=28.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=233.0,
        y=455.0,
        width=51.0,
        height=28.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=233.0,
        y=818.0,
        width=51.0,
        height=28.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=233.0,
        y=1181.0,
        width=51.0,
        height=28.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=833.0,
        y=455.0,
        width=51.0,
        height=28.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=833.0,
        y=818.0,
        width=51.0,
        height=28.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    button_9.place(
        x=833.0,
        y=1181.0,
        width=51.0,
        height=28.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_10 clicked"),
        relief="flat"
    )
    button_10.place(
        x=1133.0,
        y=455.0,
        width=51.0,
        height=28.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_11 clicked"),
        relief="flat"
    )
    button_11.place(
        x=1133.0,
        y=818.0,
        width=51.0,
        height=28.0
    )

    canvas.create_text(
        361.0,
        414.0,
        anchor="nw",
        text="Espresso",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    canvas.create_text(
        361.0,
        777.0,
        anchor="nw",
        text="Mocha Latte",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    canvas.create_text(
        361.0,
        1140.0,
        anchor="nw",
        text="Mocha Latte",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    canvas.create_text(
        61.0,
        414.0,
        anchor="nw",
        text="Americano",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    canvas.create_text(
        61.0,
        777.0,
        anchor="nw",
        text="Cold Brew",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    canvas.create_text(
        61.0,
        1140.0,
        anchor="nw",
        text="Cold Brew",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    canvas.create_text(
        661.0,
        414.0,
        anchor="nw",
        text="Latte",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    canvas.create_text(
        661.0,
        777.0,
        anchor="nw",
        text="Vanilla Latte",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    canvas.create_text(
        661.0,
        1140.0,
        anchor="nw",
        text="Vanilla Latte",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    canvas.create_text(
        961.0,
        414.0,
        anchor="nw",
        text="Cappuccino",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    canvas.create_text(
        961.0,
        777.0,
        anchor="nw",
        text="Hazelnut Latte",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    canvas.create_text(
        961.0,
        1140.0,
        anchor="nw",
        text="Hazelnut Latte",
        fill="#000000",
        font=("IstokWeb Bold", 20 * -1)
    )

    canvas.create_rectangle(
        0.0,
        5.0,
        1280.0,
        98.0,
        fill="#4F6F52",
        outline="")

    canvas.create_text(
        512.0,
        26.0,
        anchor="nw",
        text="M E N U",
        fill="#FFFFFF",
        font=("IstokWeb Bold", 40 * -1)
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_12 clicked"),
        relief="flat"
    )
    button_12.place(
        x=142.0,
        y=1318.0,
        width=1028.0,
        height=75.0
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        191.0,
        306.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        791.0,
        314.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        1089.0,
        314.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        491.0,
        669.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        791.0,
        669.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        1096.0,
        677.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        491.0,
        314.0,
        image=image_image_9
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        491.0,
        1032.0,
        image=image_image_10
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(
        791.0,
        1040.0,
        image=image_image_11
    )

    image_image_12 = PhotoImage(
        file=relative_to_assets("image_12.png"))
    image_12 = canvas.create_image(
        1087.0,
        1040.0,
        image=image_image_12
    )
    window.resizable(False, False)
    window.mainloop()

login()