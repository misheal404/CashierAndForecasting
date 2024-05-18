import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class PaymentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Metode Pembayaran")

        self.back_image = None  # Variable to hold the image to avoid garbage collection
        self.setup_payment_page()

    def setup_payment_page(self):
        # Bersihkan root dari widget yang ada sebelumnya
        for widget in self.root.winfo_children():
            widget.destroy()

        # Label Debit di tengah halaman
        self.label_debit = tk.Label(self.root, text="Debit", font=("Helvetica", 24))
        self.label_debit.grid(row=0, column=1, columnspan=2, pady=20)

        # Label dan Entry untuk Total Pembelian
        self.label_total = tk.Label(self.root, text="Total Pembelian")
        self.label_total.grid(row=1, column=0, sticky="w", padx=10)
        self.entry_total = tk.Entry(self.root)
        self.entry_total.grid(row=1, column=1, padx=10)

        # Label dan OptionMenu untuk Nama Bank
        self.label_bank = tk.Label(self.root, text="Nama Bank")
        self.label_bank.grid(row=2, column=0, sticky="w", padx=10)
        self.bank_var = tk.StringVar(self.root)
        self.bank_var.set("Pilih Bank")
        self.bank_options = ["BCA"]
        self.bank_menu = tk.OptionMenu(self.root, self.bank_var, *self.bank_options)
        self.bank_menu.grid(row=2, column=1, padx=10)

        # Tombol Selesai dengan warna
        self.finish_button = tk.Button(self.root, text="Selesai", command=self.finish_payment, bg="blue", fg="black")
        self.finish_button.grid(row=3, column=0, columnspan=2, pady=20)

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

        # Label Pembayaran Berhasil di tengah halaman
        self.label_success = tk.Label(self.root, text="Pembayaran Berhasil", font=("Helvetica", 24))
        self.label_success.pack(pady=20)

        # Informasi pembayaran
        self.label_info = tk.Label(self.root, text=f"Total Pembelian: {total_pembelian}\nBank: {nama_bank}", font=("Arial", 14))
        self.label_info.pack(pady=10)

        # Tombol Cetak Nota
        self.print_button = tk.Button(self.root, text="Cetak Nota", command=self.print_receipt, bg="green", fg="black")
        self.print_button.pack(pady=5)

        # Tombol Keluar
        self.exit_button = tk.Button(self.root, text="Keluar", command=self.root.quit, bg="red", fg="black")
        self.exit_button.pack(pady=5)

    def print_receipt(self):
        # Fungsi cetak nota
        messagebox.showinfo("Cetak Nota", "Nota berhasil dicetak.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentApp(root)
    root.mainloop()
