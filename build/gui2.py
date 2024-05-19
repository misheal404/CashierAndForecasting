from pathlib import Path
import customtkinter as ctk
from tkinter import Tk, Canvas, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\build\assets\frame2")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1280x832")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=832,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    683.0,
    432.0,
    image=image_image_1
)

canvas.create_rectangle(
    196.0,
    56.0,
    1084.0,
    745.0,
    fill="#EADBC8",
    outline=""
)

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
    312.0,
    image=entry_image_1
)
entry_1 = ctk.CTkEntry(
    master=canvas,
    width=550.0,
    height=62.0,
    corner_radius=20,bg_color="#EADBC8",
    fg_color="#FFFFFF",
    text_color="#000716"
)
entry_1.place(
    x=381.0,
    y=280.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    668.0,
    442.0,
    image=entry_image_2
)
entry_2 = ctk.CTkEntry(
    master=canvas,
    width=550.0, height=62.0,
    corner_radius=20, bg_color="#EADBC8",
    fg_color="#FFFFFF",
    text_color="#000716"
)
entry_2.place(
    x=381.0,
    y=410.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
rounded_button = ctk.CTkButton(
    master=canvas,
    font=('Helvetica', -15, 'bold'),
    text=" ",
    width=100,
    height=40,
    corner_radius=25,  # This creates the rounded effect
    border_width=1, image=button_image_1,
    border_color="#EEEEEE",
    command=lambda: print("button_1 clicked"), bg_color='#EADBC8',
    fg_color="#EADBC8"
    )
button_1 = ctk.CTkButton(master=canvas,width=281,
    height=69, bg_color='transparent',
    image=button_image_1,
    border_width=0,
    command=lambda: print("button_1 clicked"),
    text=''  # Ensure no text overlay on the image
)
rounded_button.place(
    x=528.0,
    y=595.0

)

window.resizable(False, False)
window.mainloop()
