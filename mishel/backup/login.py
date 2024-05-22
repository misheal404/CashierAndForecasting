def sign_in():
    from tkinter import Toplevel
    import customtkinter as ctk
    from pathlib import Path

    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
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
        borderwidth=0, text='password', fg='black',
        highlightthickness=0,
        command=lambda: open_window_2(windowA, home),
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