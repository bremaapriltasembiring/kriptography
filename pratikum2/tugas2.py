a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
operator = input("Masukkan operator (+, -, *, /, %): ")

if operator == '+':
    hasil = a + b
elif operator == '-':
    hasil = a - b
elif operator == '*':
    hasil = a * b
elif operator == '/':
    if b != 0:
        hasil = a / b
    else:
        hasil = "Error! Pembagian dengan nol tidak diperbolehkan."
elif operator == '%':
    hasil = a % b
else:
    hasil = "Operator tidak valid."

print(f"Hasil dari {a} {operator} {b} = {hasil}")
