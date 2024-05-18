import customtkinter as Ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class PaymentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Metode Pembayaran")

        # Mendapatkan ukuran layar
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Menentukan ukuran dan posisi jendela
        window_width = 400
        window_height = 300
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Mengatur ukuran dan posisi jendela
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.setup_payment_page()

    def setup_payment_page(self):
        # Bersihkan root dari widget yang ada sebelumnya
        for widget in self.root.winfo_children():
            widget.destroy()

        # Debit
        self.label_debit = tk.Label(self.root, text="Debit", font=("Helvetica", 36))
        self.label_debit.pack(pady=20)

        # Total Pembelian
        self.label_total = tk.Label(self.root, text="Total Pembelian", font=("Helvetica", 18))
        self.label_total.pack(anchor="w", padx=10)

        self.entry_total = tk.Entry(self.root, font=("Helvetica", 14))
        self.entry_total.pack(padx=10)

        # Nama Bank
        self.label_bank = tk.Label(self.root, text="Nama Bank", font=("Helvetica", 18))
        self.label_bank.pack(anchor="w", padx=10)

        self.bank_var = tk.StringVar(self.root)
        self.bank_var.set("Pilih Bank")
        self.bank_options = ["BCA"]
        self.bank_menu = tk.OptionMenu(self.root, self.bank_var, *self.bank_options)
        self.bank_menu.config(font=("Helvetica", 14))
        self.bank_menu.pack(padx=10)

        # Selesai
        self.finish_button = tk.Button(self.root, text="Selesai", command=self.finish_payment, bg="blue", fg="black", font=("Helvetica", 18))
        self.finish_button.pack(pady=20)

    def finish_payment(self):
        total_pembelian = self.entry_total.get()
        nama_bank = self.bank_var.get()

        if not total_pembelian:
            messagebox.showerror("Input Error", "Total pembelian tidak boleh kosong.")
            return

        if nama_bank == "Pilih Bank":
            messagebox.showerror("Input Error", "Silakan pilih nama bank.")
            return

        try:
            total_pembelian = float(total_pembelian)
            self.show_success_page(total_pembelian, nama_bank)
        except ValueError:
            messagebox.showerror("Input Error", "Total pembelian harus berupa angka.")

    def show_success_page(self, total_pembelian, nama_bank):
        # Bersihkan root dari widget yang ada sebelumnya
        for widget in self.root.winfo_children():
            widget.destroy()

        # Pembayaran Berhasil
        self.label_success = tk.Label(self.root, text="Pembayaran Berhasil", font=("Helvetica", 36))
        self.label_success.pack(pady=20)

        # Informasi pembayaran
        info_text = f"Total Pembelian: {total_pembelian}\nBank: {nama_bank}"
        self.label_info = tk.Label(self.root, text=info_text, font=("Arial", 24))
        self.label_info.pack(pady=10)

        # Cetak Nota
        self.print_button = tk.Button(self.root, text="Cetak Nota", command=self.print_receipt, bg="green", fg="black", font=("Helvetica", 18))
        self.print_button.pack(pady=5)

        # Keluar
        self.exit_button = tk.Button(self.root, text="Keluar", command=self.root.quit, bg="red", fg="black", font=("Helvetica", 18))
        self.exit_button.pack(pady=5)

    def print_receipt(self):
        # Fungsi cetak nota
        messagebox.showinfo("Cetak Nota", "Nota berhasil dicetak.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentApp(root)
    root.mainloop()
