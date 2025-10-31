def transposisi_cipher(plaintext):
    # Baris ini memiliki komentar // 4, yang mengindikasikan niat
    # untuk membagi panjang teks, tetapi secara fungsional hanya mengambil len(plaintext)
    part_length = len(plaintext) // 4  # Menggunakan integer division

    # Membagi plaintext menjadi bagian-bagian (parts)
    parts = [plaintext[i:i + part_length] for i in range(0,
    len(plaintext), part_length)]
    
    ciphertext = ""
    # Mengambil karakter secara kolom (transposisi) untuk 4 kolom
    for col in range(4):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]
    return ciphertext

plaintext = input("Masukkan plaintext: ")
ciphertext = transposisi_cipher(plaintext)
print(ciphertext)