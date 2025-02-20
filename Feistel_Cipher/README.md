# Feistel Cipher Encryption & Decryption

A Python implementation of the **Feistel Cipher**, a symmetric structure used in block ciphers, which splits data into halves and processes them iteratively.

---

## Features
- Encrypts plaintext using a **Feistel network** structure  
- Decrypts ciphertext back to the original message  
- Uses binary bitwise operations for processing  
- Supports dynamic-length plaintext  

---

## Requirements
- Python 3.x

---

## Usage
### 1. Running the Script
```sh
python feistel_cipher.py
```
Sample interaction:
```
Enter a string : hello
Result : 0110100001100101011011000110110001101111
Enter a key : key
Cipher: 1010111101010100110001010100010110011010
Decrypted: hello
```

### 2. Using as a Module
```python
from feistel_cipher import feistel_encrypt, feistel_decrypt

plaintext = "hello"
key = "key"

encrypted = feistel_encrypt(plaintext, key)
decrypted = feistel_decrypt(encrypted, key)
```

---

## How It Works
### Encryption (`feistel_encrypt()`)
1. Converts plaintext to binary.
2. Splits the binary string into left and right halves.
3. Applies bitwise operations with a given key.
4. Swaps halves after each round.
5. Produces a cipher binary string.

### Decryption (`feistel_decrypt()`)
1. Follows the encryption process in reverse order.
2. Applies the same bitwise operations with the key.
3. Swaps halves to reconstruct the original plaintext.

### Key-Based Processing
1. Converts key to binary.
2. Uses bitwise addition and XOR operations.
3. Preserves data integrity through reversible transformations.

---

## Example
**Input:**
```
Enter a string : world
Enter a key : secret
```
**Output:**
```
Cipher: 10101011001110100101101101001011
Decrypted: world
```

---

## Notes
- The key is case-sensitive.
- Non-alphabetic characters remain unchanged.
- Supports only ASCII-based text encryption.

---

## Limitations
- Only supports binary-based encryption.
- Key size impacts encryption complexity.
- Limited to text input.

---

## Live Demo
Test with online Python interpreters:
1. [Replit](https://replit.com/)
2. [PythonTutor](https://pythontutor.com/render.html)

---

## License
[MIT](https://choosealicense.com/licenses/mit/) - Free for educational use.

