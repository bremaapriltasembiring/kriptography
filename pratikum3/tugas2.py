# Program Konversi Bilangan Oktal ke Desimal, Biner, dan Hexadesimal

print("=== Konversi Bilangan Oktal ===")
oktal = input("Masukkan bilangan oktal: ")

try:
    # Konversi ke Desimal
    desimal = int(oktal, 8)
    # Konversi ke Biner
    biner = bin(desimal).replace("0b", "")
    # Konversi ke Hexadesimal
    heksa = hex(desimal).upper().replace("0X", "")
    
    print(f"Bilangan Oktal: {oktal}")
    print(f"Konversi ke Desimal: {desimal}")
    print(f"Konversi ke Biner: {biner}")
    print(f"Konversi ke Hexadesimal: {heksa}")
except ValueError:
    print("Input tidak valid! Pastikan hanya memasukkan angka 0-7.")
