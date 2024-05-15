import tkinter as tk
from tkinter import messagebox

class PaymentSuccessPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Payment Success")

        # Label
        tk.Label(master, text="Payment Successful!", font=("Helvetica", 18, "bold")).pack(pady=20)

        # Button
        tk.Button(master, text="Close", command=self.close_window).pack(pady=10)

        def print_receipt(self): 
        # Add your code to print the receipt here
            messagebox.showinfo("Print Nota", "Nota Printed Successfully!")

        # Button
        tk.Button(master, text="print nota", command=self.close_window, bg="#76885B").pack(pady=10)

    def close_window(self):
        self.master.destroy()

def show_payment_success_page():
    root = tk.Tk()
    app = PaymentSuccessPage(root)
    root.mainloop()

if __name__ == "__main__":
    show_payment_success_page()
