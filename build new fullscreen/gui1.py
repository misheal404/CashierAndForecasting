
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\PROKOM\CashierAndForecasting\build new\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.attributes("-fullscreen", True)

# Toggle fullscreen with F11
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen")))

# Exit fullscreen with Escape and set size to 1280x720 (kelipatan dari 1280x720)
window.bind("<Escape>", lambda event: (window.attributes("-fullscreen", False), window.geometry("1280x720")))

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
