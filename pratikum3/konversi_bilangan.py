# ==============================================
# TUGAS 1 - KONVERSI BILANGAN
# Praktikum III: Matematika dalam Kriptografi
# ==============================================

def konversi_desimal():
    desimal = int(input("Masukkan bilangan desimal: "))
    print(f"\nBilangan desimal: {desimal}")
    print(f"Biner: {bin(desimal)[2:]}")
    print(f"Oktal: {oct(desimal)[2:]}")
    print(f"Heksadesimal: {hex(desimal)[2:].upper()}")


def konversi_biner():
    biner = input("Masukkan bilangan biner: ")
    desimal = int(biner, 2)
    print(f"\nBilangan biner: {biner}")
    print(f"Desimal: {desimal}")
    print(f"Heksadesimal: {hex(desimal)[2:].upper()}")


def konversi_oktal():
    oktal = input("Masukkan bilangan oktal: ")
    desimal = int(oktal, 8)
    print(f"\nBilangan oktal: {oktal}")
    print(f"Desimal: {desimal}")
    print(f"Biner: {bin(desimal)[2:]}")
    print(f"Heksadesimal: {hex(desimal)[2:].upper()}")


def konversi_heksa():
    heksa = input("Masukkan bilangan heksadesimal: ")
    desimal = int(heksa, 16)
    print(f"\nBilangan heksadesimal: {heksa.upper()}")
    print(f"Desimal: {desimal}")
    print(f"Biner: {bin(desimal)[2:]}")
    print(f"Oktal: {oct(desimal)[2:]}")


def main():
    print("=== KONVERSI BILANGAN ===")
    print("1. Desimal ke Biner/Oktal/Heksadesimal")
    print("2. Biner ke Desimal/Heksadesimal")
    print("3. Oktal ke Desimal/Biner/Heksadesimal")
    print("4. Heksadesimal ke Desimal/Biner/Oktal")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        konversi_desimal()
    elif pilihan == "2":
        konversi_biner()
    elif pilihan == "3":
        konversi_oktal()
    elif pilihan == "4":
        konversi_heksa()
    else:
        print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
