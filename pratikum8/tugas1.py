# ================= SBOX (HEX) =================
SBOX = [
0x63,0x7C,0x77,0x7B,0xF2,0x6B,0x6F,0xC5,0x30,0x01,0x67,0x2B,0xFE,0xD7,0xAB,0x76,
0xCA,0x82,0xC9,0x7D,0xFA,0x59,0x47,0xF0,0xAD,0xD4,0xA2,0xAF,0x9C,0xA4,0x72,0xC0,
0xB7,0xFD,0x93,0x26,0x36,0x3F,0xF7,0xCC,0x34,0xA5,0xE5,0xF1,0x71,0xD8,0x31,0x15,
0x04,0xC7,0x23,0xC3,0x18,0x96,0x05,0x9A,0x07,0x12,0x80,0xE2,0xEB,0x27,0xB2,0x75,
0x09,0x83,0x2C,0x1A,0x1B,0x6E,0x5A,0xA0,0x52,0x3B,0xD6,0xB3,0x29,0xE3,0x2F,0x84,
0x53,0xD1,0x00,0xED,0x20,0xFC,0xB1,0x5B,0x6A,0xCB,0xBE,0x39,0x4A,0x4C,0x58,0xCF,
0xD0,0xEF,0xAA,0xFB,0x43,0x4D,0x33,0x85,0x45,0xF9,0x02,0x7F,0x50,0x3C,0x9F,0xA8,
0x51,0xA3,0x40,0x8F,0x92,0x9D,0x38,0xF5,0xBC,0xB6,0xDA,0x21,0x10,0xFF,0xF3,0xD2,
0xCD,0x0C,0x13,0xEC,0x5F,0x97,0x44,0x17,0xC4,0xA7,0x7E,0x3D,0x64,0x5D,0x19,0x73,
0x60,0x81,0x4F,0xDC,0x22,0x2A,0x90,0x88,0x46,0xEE,0xB8,0x14,0xDE,0x5E,0x0B,0xDB,
0xE0,0x32,0x3A,0x0A,0x49,0x06,0x24,0x5C,0xC2,0xD3,0xAC,0x62,0x91,0x95,0xE4,0x79,
0xE7,0xC8,0x37,0x6D,0x8D,0xD5,0x4E,0xA9,0x6C,0x56,0xF4,0xEA,0x65,0x7A,0xAE,0x08,
0xBA,0x78,0x25,0x2E,0x1C,0xA6,0xB4,0xC6,0xE8,0xDD,0x74,0x1F,0x4B,0xBD,0x8B,0x8A,
0x70,0x3E,0xB5,0x66,0x48,0x03,0xF6,0x0E,0x61,0x35,0x57,0xB9,0x86,0xC1,0x1D,0x9E,
0xE1,0xF8,0x98,0x11,0x69,0xD9,0x8E,0x94,0x9B,0x1E,0x87,0xE9,0xCE,0x55,0x28,0xDF,
0x8C,0xA1,0x89,0x0D,0xBF,0xE6,0x42,0x68,0x41,0x99,0x2D,0x0F,0xB0,0x54,0xBB,0x16
]

# ================= INV SBOX (masih decimal) =================
INV_SBOX = [
82,9,106,213,48,54,165,56,191,64,163,158,129,243,215,251,
124,227,57,130,155,47,255,135,52,142,67,68,196,222,233,203,
84,123,148,50,166,194,35,61,238,76,149,11,66,250,195,78,
8,46,161,102,40,217,36,178,118,91,162,73,109,139,209,37,
114,248,246,100,134,104,152,22,212,164,92,204,93,101,182,146,
108,112,72,80,253,237,185,218,94,21,70,87,167,141,157,132,
144,216,171,0,140,188,211,10,247,228,88,5,184,179,69,6,
208,44,30,143,202,63,15,2,193,175,189,3,1,19,138,107,
58,145,17,65,79,103,220,234,151,242,207,206,240,180,230,115,
150,172,116,34,231,173,53,133,226,249,55,232,28,117,223,110,
71,241,26,113,29,41,197,137,111,183,98,14,170,24,190,27,
252,86,62,75,198,210,121,32,154,219,192,254,120,205,90,244,
31,221,168,51,136,7,199,49,177,18,16,89,39,128,236,95,
96,81,127,169,25,181,74,13,45,229,122,159,147,201,156,239,
160,224,59,77,174,42,245,176,200,235,187,60,131,83,153,97,
23,43,4,126,186,119,214,38,225,105,20,99,85,33,12,125
]

# ================= RCON =================
RCON = [1,2,4,8,16,32,64,128,27,54]

def pad_pkcs7(text):
    data = [ord(c) for c in text]
    pad_len = 16 - (len(data) % 16)
    return data + [pad_len] * pad_len

def unpad_pkcs7(data):
    return data[:-data[-1]]

def bytes_to_matrix(b):
    return [b[i:i+4] for i in range(0, 16, 4)]

def matrix_to_bytes(m):
    return [b for r in m for b in r]

def add_round_key(s, k):
    return [[a ^ b for a,b in zip(x,y)] for x,y in zip(s, k)]

def sub_bytes(s):
    return [[SBOX[b] for b in row] for row in s]

def inv_sub_bytes(s):
    return [[INV_SBOX[b] for b in row] for row in s]

def shift_rows(s):
    return [
        s[0],
        s[1][1:] + s[1][:1],
        s[2][2:] + s[2][:2],
        s[3][3:] + s[3][:3],
    ]

def inv_shift_rows(s):
    return [
        s[0],
        s[1][-1:] + s[1][:-1],
        s[2][-2:] + s[2][:-2],
        s[3][-3:] + s[3][:-3],
    ]

def xtime(a):
    return ((a << 1) ^ 0x1B) & 0xFF if a & 0x80 else (a << 1)

def mix_single_column(c):
    a = c
    b = [xtime(x) for x in a]
    return [
        b[0]^a[3]^a[2]^b[1]^a[1],
        b[1]^a[0]^a[3]^b[2]^a[2],
        b[2]^a[1]^a[0]^b[3]^a[3],
        b[3]^a[2]^a[1]^b[0]^a[0],
    ]

def mix_columns(s):
    cols = list(zip(*s))
    mixed = [mix_single_column(list(c)) for c in cols]
    return [list(col) for col in zip(*mixed)]

def mul(a, b):
    r = 0
    for _ in range(8):
        if b & 1: r ^= a
        h = a & 0x80
        a = (a << 1) & 0xFF
        if h: a ^= 0x1B
        b >>= 1
    return r

def inv_mix_single_column(c):
    return [
        mul(c[0],14)^mul(c[1],11)^mul(c[2],13)^mul(c[3],9),
        mul(c[0],9)^mul(c[1],14)^mul(c[2],11)^mul(c[3],13),
        mul(c[0],13)^mul(c[1],9)^mul(c[2],14)^mul(c[3],11),
        mul(c[0],11)^mul(c[1],13)^mul(c[2],9)^mul(c[3],14),
    ]

def inv_mix_columns(s):
    cols = list(zip(*s))
    mixed = [inv_mix_single_column(list(c)) for c in cols]
    return [list(c) for c in zip(*mixed)]

def key_expansion(key):
    w=[key[i:i+4] for i in range(0,16,4)]
    for i in range(4,44):
        t=w[i-1]
        if i%4==0:
            t=t[1:]+t[:1]
            t=[SBOX[x] for x in t]
            t[0]^=RCON[(i//4)-1]
        w.append([t[j]^w[i-4][j] for j in range(4)])
    return [w[i:i+4] for i in range(0,44,4)]

def aes_encrypt_block(b,rk):
    s=bytes_to_matrix(b)
    s=add_round_key(s,rk[0])
    for r in range(1,10):
        s=sub_bytes(s)
        s=shift_rows(s)
        s=mix_columns(s)
        s=add_round_key(s,rk[r])
    s=sub_bytes(s)
    s=shift_rows(s)
    s=add_round_key(s,rk[10])
    return matrix_to_bytes(s)

def aes_decrypt_block(b,rk):
    s=bytes_to_matrix(b)
    s=add_round_key(s,rk[10])
    for r in range(9,0,-1):
        s=inv_shift_rows(s)
        s=inv_sub_bytes(s)
        s=add_round_key(s,rk[r])
        s=inv_mix_columns(s)
    s=inv_shift_rows(s)
    s=inv_sub_bytes(s)
    s=add_round_key(s,rk[0])
    return matrix_to_bytes(s)

# ============================================================
# PROGRAM DINAMIS (INPUT)
# ============================================================

plaintext = input("Masukkan plaintext: ")
key = input("Masukkan key (maks 16 karakter): ")

pb = pad_pkcs7(plaintext)

kb = [ord(c) for c in key]
kb = (kb + [0]*16)[:16]

rk = key_expansion(kb)

cipher = []
for i in range(0, len(pb), 16):
    cipher += aes_encrypt_block(pb[i:i+16], rk)

dec = []
for i in range(0, len(cipher), 16):
    dec += aes_decrypt_block(cipher[i:i+16], rk)

dec_text = ''.join(chr(x) for x in unpad_pkcs7(dec))

print("\n=== HASIL ===")
print("Ciphertext (bytes):", cipher)

# HEX dengan spasi
hex_with_space = ' '.join(f"{x:02X}" for x in cipher)
print("Ciphertext (hex):", hex_with_space)

print("Decrypted:", dec_text)

