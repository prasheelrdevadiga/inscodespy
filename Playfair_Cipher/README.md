# Playfair Cipher Implementation

A Python implementation of the Playfair cipher encryption algorithm with automatic key matrix generation and text processing.

## Features
- Key matrix generation from keyword (combines I/J)
- Plaintext processing with digraph formation
- Automatic padding with 'x' for repeating letters and odd-length text
- Implements standard Playfair encryption rules:
  - Same row: shift right
  - Same column: shift down
  - Rectangle: swap columns

## Requirements
- Python 3.x

## Usage

### 1. Running the Script
```bash
python playfair_cipher.py
```
Sample interaction:
```
Enter the plaintext: instruments
Enter the key: monarchy
Ciphertext: gatlmzlrqtx
```

### 2. Using as a Module
```python
from playfair_cipher import playfair_encrypt

encrypted = playfair_encrypt("hidethegold", "playfairexample")
print(encrypted)  # Output: "bmodzbxdna"
```

## Algorithm Steps

### 1. Key Matrix Generation
1. Convert key to lowercase, replace 'j' with 'i'
2. Remove duplicate letters while preserving order
3. Fill remaining matrix with remaining alphabet (excluding 'j')

Example for key "monarchy":
```
m o n a r
c h y b d
e f g i k
l p q s t
u v w x z
```

### 2. Text Preparation
1. Convert to lowercase, replace 'j' with 'i', remove spaces
2. Split into digraphs:
   - Add 'x' between duplicate letters
   - Add 'x' if odd number of characters

Example: "instruments" → ["in", "st", "ru", "me", "nt", "sx"]

### 3. Encryption Rules
| Case          | Transformation                     |
|---------------|------------------------------------|
| Same row      | Shift right (wrap around)          |
| Same column   | Shift down (wrap around)           |
| Rectangle     | Swap columns                       |

## Example Walkthrough
**Input:**
```
Plaintext: "attack"
Key: "monarchy"
```

**Processed Digraphs:** ["at", "ta", "ck"] → ["at", "tx", "ta", "ck"] (after padding)

**Encryption:**
1. at → m → r (same row)
2. tx → z → x (rectangle)
3. ta → h → m (same column)
4. ck → d → b (rectangle)

**Output:** "rrzxhmdb"

## Limitations
- No decryption implementation
- Skips non-alphabet characters
- Always uses lowercase for processing
- Limited error handling for invalid input

## References
- [Playfair Cipher Explanation](https://www.geeksforgeeks.org/playfair-cipher-with-examples/)
- [Historical Background](https://www.cryptomuseum.com/crypto/playfair/)

## Live Demo
Test the cipher online using:
1. [Replit Online Python Editor](https://replit.com/)
2. [OneCompiler Python](https://onecompiler.com/python)

## License
[MIT License](https://opensource.org/licenses/MIT)