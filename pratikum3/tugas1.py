# Program Konversi Bilangan Biner ke Desimal dan Hexadesimal

print("=== Konversi Bilangan Biner ===")
biner = input("Masukkan bilangan biner: ")

try:
    # Konversi ke Desimal
    desimal = int(biner, 2)
    # Konversi ke Hexadesimal
    heksa = hex(desimal).upper().replace("0X", "")
    
    print(f"Bilangan Biner: {biner}")
    print(f"Konversi ke Desimal: {desimal}")
    print(f"Konversi ke Hexadesimal: {heksa}")
except ValueError:
    print("Input tidak valid! Pastikan hanya memasukkan angka 0 dan 1.")
