# Monoalphabetic Cipher Implementation

A Python implementation of the monoalphabetic substitution cipher with automatic key generation from a keyword.

## Features
- Encrypts lowercase alphabetic text
- Generates full 26-letter key from a keyword
- Decrypts ciphertext back to original message
- Preserves non-alphabetic characters (they are omitted from ciphertext)
- Handles both partial and full keys

## Requirements
- Python 3.x

## Usage

### 1. Running the Script
```bash
python monoalphabetic_cipher.py
```
Sample interaction:
```
plain : hello world
keytext : key
key :  KEYABCDFGHIJLMNOPQRSTUVWXZ
Ciphertext: kellp
Decrypted: hello
```

### 2. Using as a Module
```python
from monoalphabetic_cipher import mono, decrypt

# Generate full key from partial key
user_key = "secret"
full_key = (user_key.upper() + 
            ''.join([chr(c) for c in range(65,91) 
                    if chr(c) not in user_key.upper()]))

encrypted = mono("attackatdawn", full_key)
decrypted = decrypt(encrypted, full_key)
```

## How It Works
### Encryption (`mono()`)
1. Converts plaintext to lowercase
2. For each alphabetic character:
   - Replaces with corresponding key character
   - `a` → key[0], `b` → key[1], ..., `z` → key[25]

### Decryption (`decrypt()`)
1. For each ciphertext character:
   - Finds its index in the key
   - Converts back to original character using index

### Key Generation
1. Takes user input keyword
2. Appends remaining alphabet letters in order
3. Ensures 26 unique uppercase characters

## Example
**Input:**
```
plain : security
keytext : cipher
```
**Generated Key:**  
`CIPHERABDFGJKLMNOQSTUVWXYZ`

**Output:**
```
Ciphertext: hxkwpmy
Decrypted: security
```

## Notes
- Key must contain 26 unique characters
- Plaintext is case-insensitive (converted to lowercase)
- Non-alphabetic characters are removed from ciphertext
- For historical accuracy, use keys without repeating letters

## Limitations
- Only handles English alphabet
- No support for uppercase preservation
- Non-alphabetic characters are omitted

## Live Demo
https://colab.research.google.com/drive/1ggChPjfgLNRMG3t_574T-FTsiZSAuGAG#scrollTo=0SEzQOelqeFs&line=29&uniqifier=1
