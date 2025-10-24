while True:
    a = int(input("Masukkan nilai a: "))
    b = int(input("Masukkan nilai b: "))
    c = a + b
    print("Hasil dari Nilai C adalah:", c)
    
    ulang = input("Apakah Anda ingin menghitung lagi? (Y/T): ").lower()
    if ulang != 'y':
        print("Program selesai. Terima kasih!")
        break
