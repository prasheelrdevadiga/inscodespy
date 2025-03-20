# RSA Encryption & Decryption

This repository contains a simple Python implementation of the RSA encryption and decryption algorithm. The script generates public and private keys and demonstrates encryption and decryption with basic mathematical operations.

## How It Works

1. **Key Generation:**
   - Choose two prime numbers `p` and `q`.
   - Compute `n = p * q` and Euler's totient function `phi = (p-1) * (q-1)`.
   - Select a public key exponent `e` such that `gcd(e, phi) = 1`.
   - Compute the private key `d` such that `(d * e) % phi = 1`.

2. **Encryption:**
   - Encrypt the message `msg` using the formula: `c = (msg ** e) % n`.

3. **Decryption:**
   - Decrypt the ciphertext `c` using the formula: `msg = (c ** d) % n`.

## Usage

### Prerequisites
- Python 3.x installed

### Running the Script

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/rsa-encryption.git
   cd rsa-encryption
   ```
2. Run the script:
   ```sh
   python rsa.py
   ```
3. Enter the values for `p`, `q`, and the message when prompted.

### Example
```sh
Enter the value of p: 3
Enter the value of q: 11
Enter a message: 2
Encrypted message: 8
Decrypted message: 2
```

## Notes
- This is a basic implementation of RSA and should not be used for secure applications.
- For real-world cryptography, consider using libraries like `PyCryptodome`.


