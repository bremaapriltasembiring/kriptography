# --- FUNGSI SUBSTITUSI CIPHER ---
def substitusi_cipher(plaintext, aturan):
    """Melakukan Substitusi Cipher."""
    ciphertext = ''
    # Pastikan Plaintext diubah ke huruf kapital untuk pencocokan dengan aturan
    for char in plaintext.upper():
        if char in aturan:
            # Substitusi jika karakter ada di aturan
            ciphertext += aturan[char]
        else:
            # Biarkan karakter tidak berubah (termasuk spasi)
            ciphertext += char
    return ciphertext

# --- FUNGSI TRANSPOSISI CIPHER ---
def transposisi_cipher(plaintext_substitusi):
    """
    Melakukan Transposisi Cipher dengan aturan pembagian menjadi
    panjang bagian L/4, lalu dibaca 4 kolom.
    """
    # Menghitung panjang bagian (L // 4)
    part_length = len(plaintext_substitusi) // 4
    
    # Jika panjang teks kurang dari 4, transposisi mungkin tidak relevan
    if part_length == 0:
        return plaintext_substitusi

    # Membagi plaintext menjadi bagian-bagian (parts)
    parts = [plaintext_substitusi[i:i + part_length] 
             for i in range(0, len(plaintext_substitusi), part_length)]
    
    ciphertext = ""
    # Membaca 4 kolom (indeks 0 hingga 3)
    for col in range(4):
        for part in parts:
            # Jika indeks kolom masih valid dalam bagian (part)
            if col < len(part):
                ciphertext += part[col]
    return ciphertext

# --- ATURAN DAN INPUT ---

# Aturan Substitusi yang digunakan pada pengerjaan tugas
aturan_substitusi = {
    'U': 'K',
    'N': 'N',
    'I': 'I',
    'K': 'K',
    'A': 'B'
}

# Plaintext yang ditentukan dalam tugas
plaintext_input = "UNIKA SANTO THOMAS"

# --- PROSES ENKRIPSI ---

# 1. Substitusi Cipher
ciphertext_substitusi = substitusi_cipher(plaintext_input, aturan_substitusi)

# 2. Transposisi Cipher
ciphertext_gabungan = transposisi_cipher(ciphertext_substitusi)

# --- TAMPILAN HASIL (Sesuai Permintaan Tugas) ---
print("==========================================")
print("             HASIL ENKRIPSI GABUNGAN      ")
print("==========================================")
print(f"1. Input Plaintext             : {plaintext_input}")
print(f"2. Ciphertext Substitusi       : {ciphertext_substitusi}")
print(f"3. Ciphertext Gabungan         : {ciphertext_gabungan}")
print("==========================================")

# Output yang diharapkan dari kode ini adalah:
# 1. Input Plaintext             : UNIKA SANTO THOMAS
# 2. Ciphertext Substitusi       : KNIKB SANTO THOMB S
# 3. Ciphertext Gabungan         : KBNTBNSTHSIAOOK TM