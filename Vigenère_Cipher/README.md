# Vigenère Cipher Encryption & Decryption

A Python implementation of the **Vigenère Cipher**, a method of encrypting alphabetic text by using a series of Caesar ciphers based on a keyword.

---

## Features
- Encrypts plaintext using a keyword-based shifting technique  
- Decrypts ciphertext back to the original message  
- Handles both uppercase and lowercase letters  
- Preserves non-alphabetic characters in the output  

---

## Requirements
- Python 3.x

---

## Usage
### 1. Running the Script
```sh
python vigenere_cipher.py
```
Sample interaction:
```
ENTER THE PLAIN TEXT
hello world
ENTER THE KEY FOR CIPHER
key
Encrypted: riijm uytnd
Decrypted: hello world
```

### 2. Using as a Module
```python
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt

plaintext = "attack at dawn"
key = "lemon"

encrypted = vigenere_encrypt(plaintext, key)
decrypted = vigenere_decrypt(encrypted, key)
```

---

## How It Works
### Encryption (`vigenere_encrypt()`)
1. Converts plaintext to lowercase.
2. Loops through each character and applies a shift based on the keyword.
3. Computes the new shifted character using modular arithmetic.
4. Preserves spaces and non-alphabetic characters.

### Decryption (`vigenere_decrypt()`)
1. Loops through each character and applies an inverse shift using the keyword.
2. Converts characters back to their original form using modular arithmetic.

### Key-Based Shifting
1. Takes a keyword input.
2. Uses each letter’s position (`a=0, b=1, ..., z=25`) as a shift value.
3. Repeats the keyword cyclically across the plaintext.

---

## Example
**Input:**
```
ENTER THE PLAIN TEXT
security
ENTER THE KEY FOR CIPHER
cipher
```
**Output:**
```
Encrypted: ubqpobrf
Decrypted: security
```

---

## Notes
- The key is case-insensitive (converted to lowercase internally).
- Non-alphabetic characters remain unchanged in the output.
- The keyword is repeated cyclically to match the length of the plaintext.

---

## Limitations
- Only handles English alphabet (a-z)
- No support for uppercase preservation
- Does not encrypt numbers or special characters

---

## Live Demo
https://colab.research.google.com/drive/1ggChPjfgLNRMG3t_574T-FTsiZSAuGAG#scrollTo=0SEzQOelqeFs&line=37&uniqifier=1
