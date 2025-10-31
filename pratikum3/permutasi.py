# ==============================================
# TUGAS 2 - PERMUTASI
# Praktikum III: Matematika dalam Kriptografi
# ==============================================

import itertools

def permutasi_menyeluruh():
    data = input("Masukkan elemen dipisahkan dengan spasi: ").split()
    hasil = list(itertools.permutations(data))
    print("\nPermutasi menyeluruh:")
    for p in hasil:
        print(p)


def permutasi_sebagian():
    data = input("Masukkan elemen dipisahkan dengan spasi: ").split()
    k = int(input("Masukkan jumlah elemen yang diambil (k): "))
    hasil = list(itertools.permutations(data, k))
    print(f"\nPermutasi {k}-sebagian:")
    for p in hasil:
        print(p)


def permutasi_keliling():
    data = input("Masukkan elemen dipisahkan dengan spasi: ").split()
    pertama = data[0]
    hasil = [[pertama] + list(perm) for perm in itertools.permutations(data[1:])]
    print("\nPermutasi keliling:")
    for p in hasil:
        print(p)


def permutasi_berkelompok():
    jumlah_grup = int(input("Masukkan jumlah kelompok: "))
    grup = []
    for i in range(jumlah_grup):
        anggota = input(f"Masukkan elemen grup {i+1} (pisahkan dengan spasi): ").split()
        grup.append(anggota)

    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru

    print("\nPermutasi berkelompok:")
    for p in hasil:
        print(p)


def atur_buku():
    n = int(input("Masukkan jumlah buku (n): "))
    r = int(input("Masukkan jumlah bagian rak (r): "))
    total_cara = r ** n
    print(f"\nJumlah cara mengatur {n} buku di {r} bagian rak adalah: {total_cara}")


def main():
    print("=== PERMUTASI ===")
    print("1. Permutasi Menyeluruh")
    print("2. Permutasi Sebagian")
    print("3. Permutasi Keliling")
    print("4. Permutasi Berkelompok")
    print("5. Mengatur Buku di Rak")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        permutasi_menyeluruh()
    elif pilihan == "2":
        permutasi_sebagian()
    elif pilihan == "3":
        permutasi_keliling()
    elif pilihan == "4":
        permutasi_berkelompok()
    elif pilihan == "5":
        atur_buku()
    else:
        print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
