from tkinter import *
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

is_fullscreen = False

def toggle_fullscreen(window):
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    window.attributes("-fullscreen", is_fullscreen)

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

def halaman_signin():
    global is_fullscreen, window
    try:
        window.destroy()
    except NameError:
        pass
    global window2
    window2 = tk.Tk()
    window2.title("Cafe Chronicle")
    window2.geometry("1366x768")
    window2.configure(bg="#DDDDDD")
    window2.resizable(True, True)
    window2.attributes("-fullscreen", is_fullscreen)

    canvas = Canvas(window2, width=1366, height=768, bg="#DDDDDD", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    rounded_frame = create_rounded_rectangle(canvas, -30, 0, 633, 720, radius=80, fill="#A9B388")

    heading = Label(window2, text="Sign In", fg="#35522B", bg="#A9B388", font=("Montserrat", 50, "bold"))
    heading.place(x=200, y=120)

    username_label = Label(window2, text="Username:", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    username_label.place(x=150, y=210)

    create_rounded_rectangle(canvas, 130, 245, 505, 295, radius=40, fill="#A9B388", outline="black", width=2)
    username_var = StringVar()

    def limit_username(*args):
        if len(username_var.get()) > 15:
            messagebox.showerror("Username Tidak Boleh Melebihi 15 Karakter!")
            username_var.set(username_var.get()[:15])

    username_var.trace("w", limit_username)
    username = Entry(window2, textvariable=username_var, width=23, fg="black", border=0, bg="#A9B388", font=("Montserrat", 20))
    username.place(x=150, y=252)

    password_label = Label(window2, text="Password:", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    password_label.place(x=150, y=310)

    create_rounded_rectangle(canvas, 130, 345, 505, 395, radius=40, fill="#A9B388", outline="black", width=2)
    password_var = StringVar()

    def limit_password(*args):
        if len(password_var.get()) > 15:
            messagebox.showerror("Input Error", "Password cannot exceed 15 characters.")
            password_var.set(password_var.get()[:15])

    password_var.trace("w", limit_password)
    password = Entry(window2, textvariable=password_var, width=23, fg="black", border=0, bg="#A9B388", font=("Montserrat", 20), show='*')
    password.place(x=150, y=352)

    def toggle_password():
        if password.cget('show') == '*':
            password.config(show='')
        else:
            password.config(show='*')

    show_password = Checkbutton(window2, text="Show Password", command=toggle_password, bg="#A9B388", fg="black", font=("Montserrat", 12))
    show_password.place(x=150, y=400)

    if ctk is not None:
        back_button = ctk.CTkButton(
            master=window2,
            text=("Back"),
            font=("Circular Std", 20),
            text_color="#FFE7A9",
            width=120,
            height=40,
            fg_color="#35522B",
            bg_color="#A9B388",
            corner_radius=20,
            command=back_login
        )
        back_button.place(x=180, y=430)

        confirm_button = ctk.CTkButton(
            master=window2,
            text=("Confirm"),
            font=("Circular Std", 20),
            text_color="#FFE7A9",
            width=120,
            height=40,
            fg_color="#35522B",
            bg_color="#A9B388",
            corner_radius=20,
            command=lambda: print("Confirm Clicked")
        )
        confirm_button.place(x=330, y=430)
    
    noacc_label = Label(window2, text="Don't have account?", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold"))
    noacc_label.place(x=150, y=480)

    sign_up_label = Label(window2, text="Sign Up", fg="#FFE7A9", bg="#A9B388", font=("HK Grotesk", 13, "bold", "underline"), cursor="hand2")
    sign_up_label.place(x=330, y=480)
    sign_up_label.bind("<Button-1>", lambda e: halaman_signup())

    window2.mainloop()

def back_signin():
    global window3
    if window3 and window3.winfo_exists():  # Periksa apakah jendela masih ada
        window3.destroy()
        window3 = None
    halaman_signin()

def halaman_signup():
    global is_fullscreen, window2, window3
    if window2 and window2.winfo_exists():  # Periksa apakah jendela masih ada
        window2.destroy()
        window2 = None
    window3 = tk.Tk()
    window3.title("Cafe Chronicle - Sign Up")
    window3.geometry("1366x768")
    window3.configure(bg="#DDDDDD")
    window3.resizable(True, True)
    window3.attributes("-fullscreen", is_fullscreen)

    canvas = Canvas(window3, width=1366, height=768, bg="#DDDDDD", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Implement the sign-up UI here
    heading = Label(window3, text="Sign Up", fg="#35522B", bg="#DDDDDD", font=("Montserrat", 50, "bold"))
    heading.place(x=600, y=120)
    if ctk is not None:
        back_button = ctk.CTkButton(
            master=window3,
            text=("Back"),
            font=("Circular Std", 20),
            text_color="#FFE7A9",
            width=120,
            height=40,
            fg_color="#35522B",
            bg_color="#A9B388",
            corner_radius=20,
            command=back_signin
        )
        back_button.place(x=180, y=430)
        username_var = StringVar()
        def limit_username(*args):
            if len(username_var.get()) > 15:
                messagebox.showerror("Username Tidak Boleh Melebihi 15 Karakter!")
                username_var.set(username_var.get()[:15])
        username_var.trace("w", limit_username)
        username = Entry(window3, textvariable=username_var, width=23, fg="black", border=0, bg="#A9B388", font=("Montserrat", 20))
        username.place(x=150, y=252)
        # Add sign-up form elements here...

    window3.mainloop()


def back_login():
    global window2
    window2.destroy()
    halaman_login()

def halaman_login():
    global window
    try:
        window3.destroy()
    except NameError:
        pass
    window = tk.Tk()
    image = PhotoImage(file="C:\\Users\\rafae\\OneDrive\\Dokumen\\PROKOM TUBES COBA COBA\\CashierAndForecasting\\rafael pp\\images.png")
    window.iconphoto(False, image)

    window.title("Cafe Chronicle")
    window.geometry("1366x768")
    window.configure(bg="#DDDDDD")
    window.resizable(True, True)

    window.attributes("-fullscreen", is_fullscreen)

    heading = Label(window, text="Cafe Chronicle", fg="#627254", bg="#DDDDDD", font=("HK Grotesk", 70))
    heading.place(x=40, y=130)

    subheading = Label(window, text="Welcome to the Cafe Chronicle Cashier app, your new", fg="#000000", bg="#DDDDDD", font=("Canva Sans", 22))
    subheading.place(x=50, y=230)

    subheading2 = Label(window, text="partner in crafting seamless customer experiences.", fg="#000000", bg="#DDDDDD", font=("Canva Sans", 22))
    subheading2.place(x=50, y=270)
    if ctk is not None:
        login_button = ctk.CTkButton(
            master=window,
            text=("Log In"),
            font=("Circular Std", 30),
            width=150,
            height=55,
            fg_color="#76885B",
            corner_radius=40,
            command=halaman_signin
        )
        login_button.place(x=70, y=350)
    
    img = PhotoImage(file="C:\\Users\\rafae\\OneDrive\\Dokumen\\PROKOM TUBES COBA COBA\\CashierAndForecasting\\rafael pp\\image.png")
    Label(window, image=img, bg="#DDDDDD").place(x=760, y=100)

    fullscreen_button = ctk.CTkButton(
        master=window,
        text=("Toggle Fullscreen"),
        font=("Circular Std", 20),
        width=150,
        height=40,
        fg_color="#76885B",
        corner_radius=20,
        command=lambda: toggle_fullscreen(window)
    )
    fullscreen_button.place(x=70, y=450)
    window.mainloop()

halaman_login()
