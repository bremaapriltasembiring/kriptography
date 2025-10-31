def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext:
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext

aturan_substitusi = {
    'U': 'Z',
    'N': 'G',
    'I': 'D',
    'K': 'P',
    'A': 'V'
}

plaintext = "UNIKA"
ciphertext = substitusi_cipher(plaintext, aturan_substitusi)
print(f'Plaintext: {plaintext}')
print(f'Ciphertext: {ciphertext}')