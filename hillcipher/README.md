# Hill Cipher Encryption & Decryption

A Python implementation of the **Hill Cipher**, a polygraphic substitution cipher based on linear algebra and modular arithmetic.

---

## Features
- Encrypts plaintext using an **n × n** key matrix  
- Decrypts ciphertext using the modular inverse of the key matrix  
- Supports dynamic matrix sizes  
- Pads plaintext if necessary for proper encryption  

---

## Requirements
- Python 3.x
- NumPy

Install NumPy using:
```sh
pip install numpy
```

---

## Usage
### 1. Running the Script
```sh
python hill_cipher.py
```
Sample interaction:
```
Enter the size of the key matrix (n x n): 2
Enter the key matrix (2x2) elements row-wise:
Row 1: 6 24
Row 2: 1 13
Enter the plain text: HELLO
Encrypted: ZEBBW
Decrypted: HELLOX
```

### 2. Using as a Module
```python
from hill_cipher import hill_cipher_encrypt, hill_cipher_decrypt

key_matrix = [[6, 24], [1, 13]]
plaintext = "HELLO"

encrypted = hill_cipher_encrypt(plaintext, key_matrix)
decrypted = hill_cipher_decrypt(encrypted, key_matrix)
```

---

## How It Works
### Encryption (`hill_cipher_encrypt()`)
1. Converts plaintext to uppercase and removes spaces
2. Converts text to numeric vector (A=0, B=1, ..., Z=25)
3. Multiplies the key matrix with plaintext blocks
4. Takes modulo 26 for final encrypted values
5. Converts numbers back to characters

### Decryption (`hill_cipher_decrypt()`)
1. Computes the modular inverse of the key matrix
2. Applies the inverse matrix to ciphertext blocks
3. Converts numeric values back to characters

### Key Matrix Generation
1. User provides an **n × n** key matrix
2. Must be invertible under mod 26
3. Determinant must have a modular inverse in mod 26

---

## Example
**Input:**
```
Enter the size of the key matrix (n x n): 2
Enter the key matrix (2x2) elements row-wise:
Row 1: 5 8
Row 2: 17 3
Enter the plain text: MATH
```
**Generated Key Matrix:**
```
5 8
17 3
```
**Output:**
```
Ciphertext: YRDK
Decrypted: MATH
```

---

## Notes
- Key matrix must be invertible in mod 26
- Plaintext is case-insensitive (converted to uppercase)
- Non-alphabetic characters are ignored
- Supports padding for uneven text length

---

## Limitations
- Only handles English alphabet (A-Z)
- No support for special characters or numbers
- Requires a valid, invertible key matrix

---

## Live Demo
https://colab.research.google.com/drive/1ggChPjfgLNRMG3t_574T-FTsiZSAuGAG#scrollTo=0SEzQOelqeFs&line=60&uniqifier=1

---


