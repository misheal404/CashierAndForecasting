

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\indoor\New folder (3)\build\assets\frame7")


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
