def vigenere_encrypt(pt, key):
    key = key.lower()
    cp = ""
    key_index = 0
    for char in pt.lower():
        if char.isalpha():
            shift = ord(key[key_index]) - ord('a')
            cp += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index = (key_index + 1) % len(key)
        else:
            cp += char
    return cp

def vigenere_decrypt(ct, key):
    key = key.lower()
    pt = ""
    key_index = 0
    for char in ct.lower():
        if char.isalpha():
            shift = ord(key[key_index]) - ord('a')
            pt += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_index = (key_index + 1) % len(key)
        else:
            pt += char
    return pt

# Input
pt = input("ENTER THE PLAIN TEXT\n")
key = input("ENTER THE KEY FOR CIPHER\n")

# Encryption
encrypted_text = vigenere_encrypt(pt, key)
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)