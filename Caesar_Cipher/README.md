# Caesar Cipher Implementation

A Python implementation of the Caesar cipher, an ancient encryption technique that shifts letters by a specified number of positions in the alphabet.

## Features
- Encrypts uppercase and lowercase letters
- Preserves non-alphabetic characters (spaces, symbols, numbers)
- Handles arbitrary shift values (including large shifts via modulo 26)

## Requirements
- Python 3.x

## Usage

### 1. Running the Script
1. Navigate to the `caesar_cipher` folder
2. Run the script:
   ```bash
   python caesar_cipher.py
   ```
3. Follow the prompts:
   ```
   Enter Text : Hello World!
   Shift : 3
   Ciphertext : Khoor Zruog!
   ```

### 2. Using as a Module
Import the cipher function in other Python scripts:
```python
from caesar_cipher import caesar_cipher

encrypted = caesar_cipher("Secret Message", 5)
decrypted = caesar_cipher(encrypted, -5)
```

## Example
**Input:**
```
Enter Text : Attack at Dawn!
Shift : 5
```

**Output:**
```
Ciphertext : Fyyfhp fy Ifbs!
```

## How It Works
The cipher uses modular arithmetic to shift characters:
- For uppercase letters: `(ord(char) + shift - 65) % 26 + 65`
- For lowercase letters: `(ord(char) + shift - 97) % 26 + 97`

Non-alphabetic characters are preserved without modification.

## Live Demo
https://colab.research.google.com/drive/1ggChPjfgLNRMG3t_574T-FTsiZSAuGAG#scrollTo=0SEzQOelqeFs&line=10&uniqifier=1

## Caesar Cipher Basics
**Encryption Formula:**  
`E(x) = (x + shift) mod 26`  

**Decryption Formula:**  
`D(x) = (x - shift) mod 26`

Where `x` is the character's alphabetical position (A=0, B=1, ..., Z=25).

## Notes
- Shift values are automatically wrapped using modulo 26
- Negative shifts will decrypt messages
- For historical accuracy, use shift = 3 (as used by Julius Caesar)
