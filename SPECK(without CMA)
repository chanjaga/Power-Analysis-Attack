#ARX暗号SPECK

def rotate_left(val, r_bits, max_bits=64):
    return ((val << r_bits) & (2 ** max_bits - 1)) | ((val & (2 ** max_bits - 1)) >> (max_bits - r_bits))

def rotate_right(val, r_bits, max_bits=64):
    return ((val & (2 ** max_bits - 1)) >> r_bits) | (val << (max_bits - r_bits) & (2 ** max_bits - 1))

# SPECKの暗号化
def speck_encrypt(X, Y, k, r):
    for i in range(r):
        X = (rotate_right(X, 8) + Y) ^ k[i]
        Y = rotate_left(Y, 3) ^ X
    return X, Y

# SPECKの復号
def speck_decrypt(X, Y, k, r):
    for i in range(r-1, -1, -1):
        Y = rotate_right(Y^X, 3)
        X = rotate_left((X^k[i]) - Y, 8)
    return X, Y

# 元の平文を設定
plaintext_1 = 0x0123456789abcdef
plaintext_2 = 0xfedcba9876543210

# 鍵を設定
key = [
    0x1918, 0x1110, 0x0908, 0x0100,
    0x1a19, 0x1211, 0x0a09, 0x0201,
    0x1b1a, 0x1312, 0x0b0a, 0x0302,
    0x1c1b, 0x1413, 0x0c0b, 0x0403,
    0x1d1c, 0x1514, 0x0d0c, 0x0504,
    0x1e1d, 0x1615, 0x0e0d, 0x0605,
    0x1f1e, 0x1716, 0x0f0e, 0x0706,
    0x0100, 0x1918, 0x1110, 0x0908
]

#暗号処理の繰り返し回数
round_times = 10

# 平文を暗号化
ciphertext_1, ciphertext_2 = speck_encrypt(plaintext_1, plaintext_2, key, round_times)

# 暗号文を復号
decrypted_1, decrypted_2 = speck_decrypt(ciphertext_1, ciphertext_2, key, round_times)

# 結果の表示
print("Original Plaintext: 0x{:016x} {:016x}".format(plaintext_1, plaintext_2))
print("Encrypted Ciphertext: 0x{:016x} {:016x}".format(ciphertext_1, ciphertext_2))
print("Decrypted Plaintext: 0x{:016x} {:016x}".format(decrypted_1, decrypted_2))
