import numpy as np

def mod_inverse_matrix(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))  # Compute determinant
    det_inv = pow(det, -1, mod)  # Compute modular inverse of determinant

    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod  # Compute adjugate matrix
    return (det_inv * adjugate) % mod  # Multiply adjugate by modular inverse of determinant

def hill_cipher_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext = plaintext.upper().replace(" ", "")
    
    if len(plaintext) % n != 0:
        plaintext += "X" * (n - len(plaintext) % n)  # Padding

    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    ciphertext = ""

    for i in range(0, len(plaintext_vector), n):
        block = plaintext_vector[i:i + n]
        result = np.dot(key_matrix, block) % 26
        ciphertext += "".join(chr(num + ord('A')) for num in result)

    return ciphertext

def hill_cipher_decrypt(ciphertext, key_matrix):
    n = len(key_matrix)
    key_inverse = mod_inverse_matrix(key_matrix, 26)  # Compute inverse matrix mod 26

    ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]
    decrypted_text = ""

    for i in range(0, len(ciphertext_vector), n):
        block = ciphertext_vector[i:i + n]
        result = np.dot(key_inverse, block) % 26
        decrypted_text += "".join(chr(num + ord('A')) for num in result)

    return decrypted_text

def get_key_matrix(n):
    print(f"Enter the key matrix ({n}x{n}) elements row-wise:")
    key_matrix = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            raise ValueError(f"Row {i + 1} must have exactly {n} elements.")
        key_matrix.append(row)
    return np.array(key_matrix)

# Example usage
n = int(input("Enter the size of the key matrix (n x n): "))
key_matrix = get_key_matrix(n)

plaintext = input("Enter the plain text: ")
encrypted_text = hill_cipher_encrypt(plaintext, key_matrix)
print("Encrypted:", encrypted_text)

decrypted_text = hill_cipher_decrypt(encrypted_text, key_matrix)
print("Decrypted:", decrypted_text)