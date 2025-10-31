def substitusi_cipher(plaintext, aturan):
    """
    Melakukan substitusi cipher berdasarkan aturan yang diberikan.
    Memastikan plaintext diubah ke huruf kapital agar sesuai dengan aturan.
    """
    ciphertext = ''
    # Iterasi melalui plaintext setelah diubah ke huruf kapital
    for char in plaintext.upper():
        if char in aturan:
            # Jika karakter ada di aturan, substitusikan
            ciphertext += aturan[char]
        else:
            # Jika tidak ada (misalnya spasi, tanda baca, atau karakter non-aturan), biarkan saja
            ciphertext += char
    return ciphertext

def input_aturan_substitusi():
    """
    Meminta pengguna untuk memasukkan aturan substitusi dan mengembalikannya dalam bentuk kamus.
    """
    aturan = {}
    print("\nMasukkan aturan substitusi (misal: A=Z, B=Y, dll.).")
    print("Ketik 'SELESAI' untuk mengakhiri input aturan.")
    
    while True:
        input_pair = input("Masukkan pasangan substitusi (Contoh: U=K) atau 'SELESAI': ").strip().upper()
        
        if input_pair == 'SELESAI':
            break
        
        # Memastikan format input benar (Contoh: A=B)
        if '=' in input_pair and len(input_pair.split('=')) == 2:
            try:
                original, replacement = input_pair.split('=')
                # Hapus spasi jika ada dan pastikan hanya satu karakter
                original = original.strip()
                replacement = replacement.strip()
                
                if len(original) == 1 and len(replacement) == 1 and original.isalpha() and replacement.isalpha():
                    aturan[original] = replacement
                    print(f"✅ Aturan '{original}' -> '{replacement}' ditambahkan.")
                else:
                    print("⚠️ Masukkan satu huruf saja untuk karakter asli dan pengganti.")
            except ValueError:
                print("❌ Format input salah. Gunakan format KODE_ASLI=KODE_PENGGANTI (Contoh: U=K).")
        else:
            print("❌ Format input salah. Gunakan format KODE_ASLI=KODE_PENGGANTI (Contoh: U=K).")
            
    return aturan

# --- Program Utama ---

# 1. Input Aturan Substitusi dari Pengguna
aturan_substitusi = input_aturan_substitusi()

# 2. Input Plaintext dari Pengguna
plaintext = input("\nMasukkan Plaintext yang ingin dienkripsi: ").strip()

# 3. Proses Enkripsi
if aturan_substitusi:
    ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

    # 4. Tampilkan Hasil
    print("\n--- Hasil Cipher Substitusi ---")
    print(f'Plaintext Asli: **{plaintext}**')
    print(f'Plaintext (Kapital): **{plaintext.upper()}**')
    print(f'Ciphertext: **{ciphertext}**')
    print("-------------------------------")
else:
    print("\nTidak ada aturan substitusi yang dimasukkan. Proses dibatalkan.")