# ==============================================
# TUGAS 3 - KOMBINASI
# Praktikum III: Matematika dalam Kriptografi
# ==============================================

import itertools

def faktorial(x):
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil


def kombinasi(n, r):
    if r > n:
        return 0
    return faktorial(n) // (faktorial(r) * faktorial(n - r))


def kombinasi_dengan_huruf():
    n = int(input("Masukkan jumlah total objek (n): "))
    r = int(input("Masukkan jumlah objek yang dipilih (r): "))

    hasil = kombinasi(n, r)
    print(f"\nJumlah kombinasi C({n}, {r}) = {hasil}")

    huruf = [chr(65 + i) for i in range(n)]  # A, B, C, ...
    print(f"Objek: {huruf}")

    print("\nKombinasi:")
    for c in itertools.combinations(huruf, r):
        print(c)


def main():
    print("=== KOMBINASI ===")
    kombinasi_dengan_huruf()


if __name__ == "__main__":
    main()
