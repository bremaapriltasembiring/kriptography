import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung hasil berdasarkan operator
def hitung():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        op = operator_var.get()

        if op == '+':
            hasil = a + b
        elif op == '-':
            hasil = a - b
        elif op == '*':
            hasil = a * b
        elif op == '/':
            if b == 0:
                messagebox.showerror("Error", "Pembagian dengan nol tidak diperbolehkan.")
                return
            hasil = a / b
        else:
            messagebox.showerror("Error", "Operator tidak valid.")
            return

        label_hasil.config(text=f"Hasil: {hasil:.2f}")
    except ValueError:
        messagebox.showerror("Input Salah", "Masukkan angka yang valid untuk nilai a dan b.")

# Fungsi untuk menghapus semua input
def reset():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    operator_var.set('+')
    label_hasil.config(text="Hasil: -")

# Fungsi untuk keluar dari aplikasi
def keluar():
    root.destroy()

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("400x320")
root.config(bg="#2C3E50")  # Warna biru gelap elegan
root.minsize(350, 300)      # Ukuran minimum
root.resizable(True, True)  # Sekarang bisa diperbesar/diperkecil

# Judul
judul = tk.Label(root, text="Kalkulator Aritmatika", font=("Segoe UI", 16, "bold"),
                 bg="#2C3E50", fg="white")
judul.pack(pady=15)

# Frame utama
frame = tk.Frame(root, bg="#34495E", padx=20, pady=20)
frame.pack(fill="both", expand=True, padx=20, pady=10)

# Input nilai a
tk.Label(frame, text="Nilai A:", font=("Segoe UI", 11), bg="#34495E", fg="white").grid(row=0, column=0, sticky="w", pady=5)
entry_a = tk.Entry(frame, font=("Segoe UI", 11), justify="center")
entry_a.grid(row=0, column=1, pady=5, sticky="ew")

# Input nilai b
tk.Label(frame, text="Nilai B:", font=("Segoe UI", 11), bg="#34495E", fg="white").grid(row=1, column=0, sticky="w", pady=5)
entry_b = tk.Entry(frame, font=("Segoe UI", 11), justify="center")
entry_b.grid(row=1, column=1, pady=5, sticky="ew")

# Pilihan operator (hanya +, -, *, /)
tk.Label(frame, text="Operator:", font=("Segoe UI", 11), bg="#34495E", fg="white").grid(row=2, column=0, sticky="w", pady=5)
operator_var = tk.StringVar(value='+')
operator_menu = tk.OptionMenu(frame, operator_var, '+', '-', '*', '/')
operator_menu.config(font=("Segoe UI", 11), bg="#1ABC9C", fg="white", width=5, relief="flat")
operator_menu.grid(row=2, column=1, pady=5, sticky="ew")

# Mengatur grid agar responsif
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=2)

# Tombol-tombol
tombol_frame = tk.Frame(root, bg="#2C3E50")
tombol_frame.pack(fill="x", padx=20, pady=10)

btn_hitung = tk.Button(tombol_frame, text="Hitung", font=("Segoe UI", 11, "bold"),
                       bg="#1ABC9C", fg="white", width=10, relief="flat", command=hitung)
btn_hitung.pack(side="left", expand=True, padx=5, fill="x")

btn_reset = tk.Button(tombol_frame, text="Reset", font=("Segoe UI", 11, "bold"),
                      bg="#E67E22", fg="white", width=10, relief="flat", command=reset)
btn_reset.pack(side="left", expand=True, padx=5, fill="x")

btn_keluar = tk.Button(tombol_frame, text="Keluar", font=("Segoe UI", 11, "bold"),
                       bg="#E74C3C", fg="white", width=10, relief="flat", command=keluar)
btn_keluar.pack(side="left", expand=True, padx=5, fill="x")

# Label hasil
label_hasil = tk.Label(root, text="Hasil: -", font=("Segoe UI", 13, "bold"),
                       bg="#2C3E50", fg="#ECF0F1")
label_hasil.pack(pady=10)

# Membuat elemen ikut menyesuaikan ukuran jendela
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Jalankan aplikasi
root.mainloop()
