import customtkinter as ctk

# Inisialisasi aplikasi
app = ctk.CTk()
app.title("Pembayaran Debit")
app.geometry("400x300")

# Variabel global untuk menyimpan total pembelian
total_pembelian = 0

# Pembayaran berhasil
def pembayaran_berhasil():
    global total_pembelian
    
    # Hapus semua widget yang ada di frame utama
    for widget in frame_main.winfo_children():
        widget.destroy()

    # Pembayaran berhasil
    label_sukses = ctk.CTkLabel(master=frame_main, text="Pembayaran Berhasil", font=("Arial", 16))
    label_sukses.pack(pady=10)

    # Total pembelian
    label_total = ctk.CTkLabel(master=frame_main, text=f"Total Pembelian: Rp {total_pembelian}", font=("Arial", 14))
    label_total.pack(pady=5)

    # Cetak nota
    button_print = ctk.CTkButton(master=frame_main, text="Print Nota", command=print_nota, fg_color="#4CAF50")
    button_print.pack(pady=10)

    # Keluar
    button_keluar = ctk.CTkButton(master=frame_main, text="Keluar", command=app.quit, fg_color="#f44336")
    button_keluar.pack(pady=10)

# Fungsi untuk mencetak nota (dummy function)
def print_nota():
    print("Nota dicetak")

# Total Pembelian
def selesai_tapped():
    global total_pembelian
    total_pembelian = int(entry_total_pembelian.get())
    pembayaran_berhasil()

# Frame utama untuk menampung semua widget
frame_main = ctk.CTkFrame(master=app)
frame_main.pack(pady=20, padx=20, fill="both", expand=True)

# Judul halaman
label_title = ctk.CTkLabel(master=frame_main, text="Debit", font=("Arial", 18))
label_title.pack(pady=10)

# Label untuk total pembelian
label_total_pembelian = ctk.CTkLabel(master=frame_main, text="Total Pembelian:", font=("Arial", 14))
label_total_pembelian.pack(pady=5)

# Entry untuk total pembelian
entry_total_pembelian = ctk.CTkEntry(master=frame_main)
entry_total_pembelian.pack(pady=5)

# Label untuk metode pembayaran
label_metode = ctk.CTkLabel(master=frame_main, text="Metode Pembayaran:", font=("Arial", 14))
label_metode.pack(pady=5)

# Dropdown menu untuk metode pembayaran
metode_var = ctk.StringVar(value="Pilih Metode")
dropdown_metode = ctk.CTkOptionMenu(master=frame_main, variable=metode_var, values=["Debit Card"])
dropdown_metode.pack(pady=5)

# Label untuk pilih bank
label_bank = ctk.CTkLabel(master=frame_main, text="Pilih Bank:", font=("Arial", 14))
label_bank.pack(pady=5)

# Dropdown menu untuk pilih bank
bank_var = ctk.StringVar(value="Pilih Bank")
dropdown_bank = ctk.CTkOptionMenu(master=frame_main, variable=bank_var, values=["BCA"])
dropdown_bank.pack(pady=5)

# Tombol selesai
button_selesai = ctk.CTkButton(master=frame_main, text="Selesai", command=selesai_tapped, fg_color="#4CAF50")
button_selesai.pack(pady=20)

# Menjalankan aplikasi
app.mainloop()
