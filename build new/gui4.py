
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\indoor\New folder (3)\build\assets\frame4")


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
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
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
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
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
window.resizable(False, False)
window.mainloop()