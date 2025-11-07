class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def _format_key(self, text):
        """Menyesuaikan panjang kunci agar sama dengan teks"""
        key_repeated = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                key_repeated += self.key[key_index % len(self.key)]
                key_index += 1
            else:
                key_repeated += char
        return key_repeated

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        key = self._format_key(plaintext)
        ciphertext = ""
        print("\n=== PROSES ENKRIPSI ===")
        for p, k in zip(plaintext, key):
            if p.isalpha():
                p_val = ord(p) - 65
                k_val = ord(k) - 65
                c_val = (p_val + k_val) % 26
                c = chr(c_val + 65)
                ciphertext += c
                print(f"{p}({p_val}) + {k}({k_val}) = {c}({c_val})")
            else:
                ciphertext += p
                print(f"{p} (bukan huruf, tidak diubah)")
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        key = self._format_key(ciphertext)
        plaintext = ""
        print("\n=== PROSES DEKRIPSI ===")
        for c, k in zip(ciphertext, key):
            if c.isalpha():
                c_val = ord(c) - 65
                k_val = ord(k) - 65
                p_val = (c_val - k_val) % 26
                p = chr(p_val + 65)
                plaintext += p
                print(f"{c}({c_val}) - {k}({k_val}) = {p}({p_val})")
            else:
                plaintext += c
                print(f"{c} (bukan huruf, tidak diubah)")
        return plaintext


# === Bagian utama program ===
def main():
    print("===== PROGRAM VIGENERE CIPHER =====")
    key = input("Masukkan kunci: ")
    vc = VigenereCipher(key)

    while True:
        print("\nMenu:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            text = input("Masukkan teks yang akan dienkripsi: ")
            hasil = vc.encrypt(text)
            print("\nHasil Enkripsi:", hasil)
        elif pilihan == "2":
            text = input("Masukkan teks yang akan didekripsi: ")
            hasil = vc.decrypt(text)
            print("\nHasil Dekripsi:", hasil)
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
