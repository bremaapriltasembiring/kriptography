# Kalkulator Hybrid - Tugas Praktikum 2

def kalkulator_hybrid():
    print("=== KALKULATOR HYBRID ===")
    print("Masukkan ekspresi matematika (contoh: 4+4-3 atau 5 - 3 * 4)")
    ekspresi = input("Input Ekspresi: ")

    try:
        # Menghapus spasi berlebih dan mengevaluasi ekspresi
        hasil = eval(ekspresi)
        print("Output >", hasil)
    except Exception as e:
        print("Terjadi kesalahan dalam perhitungan:", e)

# Program utama
if __name__ == "__main__":
    kalkulator_hybrid()
