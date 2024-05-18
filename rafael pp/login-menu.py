from tkinter import *
import tkinter as tk
import customtkinter as ctk 

def halaman_register():
    window.destroy()
    global window2
    window2 = tk.Tk()
    window2.title("Cafe Chronicle")
    window2.geometry("1250x756")
    window2.configure(bg="white")
    window2.resizable(True, True)    
    frame = Frame(window2, width=350, height=350, bg="gray")
    frame.place(x=600, y=200)
    heading = Label(frame, text="Sign Up", fg="#57a1f8", bg="gray", font=("Montserrat", 23, "bold"))
    heading.place(x=100, y=5)
    username = Entry(frame, width= 25, fg="black", border=2, bg="white", font=(11))
    username.place(x=60, y=75)
    password = Entry(frame, width= 25, fg="black", border=2, bg="white", font=(11))
    password.place(x=60, y=115)

    img = PhotoImage(file="Modern Initial E Logo.png")
    Label(window2, image=img, bg="white",).place(x=120, y=125)

    Button(frame, width=29, height=1, text="Confirm", fg="white", bg="#57a1f8").place(x=60, y=185)
    Button(frame, width=29, height=1, text="Back", fg="black", bg="white", command=back_login).place(x=60, y=155)
    window2.mainloop()

def back_login():
    window2.destroy()
    halaman_login()

def halaman_login():
    global window
    window = tk.Tk()
    #menambah ikon photo
    image = PhotoImage(file="C:\\Users\\rafae\\OneDrive\\Dokumen\\PROKOM TUBES COBA COBA\\CashierAndForecasting\\rafael pp\\images.png")
    window.iconphoto(False, image)

    window.title("Cafe Chronicle") #judul program sebelah ikon
    window.geometry("1366x768") #resolusi layar
    window.configure(bg="#DDDDDD")#bg
    window.resizable(True, True)    
    #frame = Frame(window, width=350, height=350, bg="gray")
    #frame.place(x=600, y=200)
    heading = Label(window, text="Cafe Chronicle", fg="#627254", bg="#DDDDDD", font=("HK Grotesk", 70))#judul di interface
    heading.place(x=40, y=130)

    subheading = Label(window, text="Welcome to the Cafe Chronicle Cashier app, your new", fg="#000000", bg="#DDDDDD", font=("Canva Sans", 22)) #subjudul
    subheading.place(x=50, y=230)

    subheading2 = Label(window, text="partner in crafting seamless customer experiences.", fg="#000000", bg="#DDDDDD", font=("Canva Sans", 22)) #subjudul
    subheading2.place(x=50, y=270)
    if ctk is not None:
        login_button = ctk.CTkButton(
            master=window,
            text=("Log In"),
            font=("Circular Std", 30),
            width=150,
            height=55,
            fg_color="#76885B",
            corner_radius=40,  # Adjust corner radius for desired roundness
            command=halaman_register  # Replace with your login function
        )
        login_button.place(x=70, y=350)  # Position the button (adjust as needed)
    
    img = PhotoImage(file="C:\\Users\\rafae\\OneDrive\\Dokumen\\PROKOM TUBES COBA COBA\\CashierAndForecasting\\rafael pp\\image.png")
    Label(window, image=img, bg="#DDDDDD",).place(x=760, y=100)

    window.mainloop()

halaman_login()
