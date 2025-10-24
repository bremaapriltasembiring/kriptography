# Program Konversi Bilangan Hexadesimal ke Desimal, Biner, dan Oktal

print("=== Konversi Bilangan Hexadesimal ===")
heksa = input("Masukkan bilangan hexadesimal: ")

try:
    # Konversi ke Desimal
    desimal = int(heksa, 16)
    # Konversi ke Biner
    biner = bin(desimal).replace("0b", "")
    # Konversi ke Oktal
    oktal = oct(desimal).replace("0o", "")
    
    print(f"Bilangan Hexadesimal: {heksa.upper()}")
    print(f"Konversi ke Desimal: {desimal}")
    print(f"Konversi ke Biner: {biner}")
    print(f"Konversi ke Oktal: {oktal}")
except ValueError:
    print("Input tidak valid! Pastikan hanya memasukkan angka 0-9 dan huruf A-F.")
