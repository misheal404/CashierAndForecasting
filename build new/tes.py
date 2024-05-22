from tkinter import Tk, Canvas, PhotoImage, Entry, Button, Scrollbar, Frame
from pathlib import Path

def menu():

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\git rep\CashierAndForecasting\build new\assets\frame3")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    WindowC = Tk()
    WindowC.geometry("1280x800")  # Adjust the height to fit the window with scrollbar
    WindowC.configure(bg="#E8DFCA")

    frame = Frame(WindowC)
    frame.pack(fill="both", expand=True)

    canvas = Canvas(
        frame,
        bg="#E8DFCA",
        height=1455,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)

    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Rest of your canvas and widget creation code goes here
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

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(191.0, 669.0, image=image_image_1)

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(191.0, 1040.0, image=image_image_2)

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(442.11111068725586, 470.0, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_1.place(x=399.0, y=456.0, width=86.22222137451172, height=26.0)

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(442.11111068725586, 833.0, image=entry_image_2)
    entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_2.place(x=399.0, y=819.0, width=86.22222137451172, height=26.0)

    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(442.11111068725586, 1196.0, image=entry_image_3)
    entry_3 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_3.place(x=399.0, y=1182.0, width=86.22222137451172, height=26.0)

    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(142.11111068725586, 470.0, image=entry_image_4)
    entry_4 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_4.place(x=99.0, y=456.0, width=86.22222137451172, height=26.0)

    entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(142.11111068725586, 833.0, image=entry_image_5)
    entry_5 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_5.place(x=99.0, y=819.0, width=86.22222137451172, height=26.0)

    entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(142.11111068725586, 1196.0, image=entry_image_6)
    entry_6 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_6.place(x=99.0, y=1182.0, width=86.22222137451172, height=26.0)

    entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(742.1111106872559, 470.0, image=entry_image_7)
    entry_7 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_7.place(x=699.0, y=456.0, width=86.22222137451172, height=26.0)

    entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(742.1111106872559, 833.0, image=entry_image_8)
    entry_8 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_8.place(x=699.0, y=819.0, width=86.22222137451172, height=26.0)

    entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(742.1111106872559, 1196.0, image=entry_image_9)
    entry_9 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_9.place(x=699.0, y=1182.0, width=86.22222137451172, height=26.0)

    entry_image_10 = PhotoImage(file=relative_to_assets("entry_10.png"))
    entry_bg_10 = canvas.create_image(1042.1111106872559, 470.0, image=entry_image_10)
    entry_10 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_10.place(x=999.0, y=456.0, width=86.22222137451172, height=26.0)

    entry_image_11 = PhotoImage(file=relative_to_assets("entry_11.png"))
    entry_bg_11 = canvas.create_image(1042.1111106872559, 833.0, image=entry_image_11)
    entry_11 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_11.place(x=999.0, y=819.0, width=86.22222137451172, height=26.0)

    entry_image_12 = PhotoImage(file=relative_to_assets("entry_12.png"))
    entry_bg_12 = canvas.create_image(1042.1111106872559, 1196.0, image=entry_image_12)
    entry_12 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_12.place(x=999.0, y=1182.0, width=86.22222137451172, height=26.0)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
    button_1.place(x=176.0, y=1262.0, width=30.0, height=30.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat")
    button_2.place(x=476.0, y=1262.0, width=30.0, height=30.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"), relief="flat")
    button_3.place(x=776.0, y=1262.0, width=30.0, height=30.0)

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=lambda: print("button_4 clicked"), relief="flat")
    button_4.place(x=1076.0, y=1262.0, width=30.0, height=30.0)

    WindowC.mainloop()
menu()