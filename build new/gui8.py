

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


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
