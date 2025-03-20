# Diffie-Hellman Key Exchange

This repository contains a simple Python implementation of the **Diffie-Hellman Key Exchange Algorithm**, which allows two parties to securely establish a shared secret key over an insecure communication channel.

## How It Works

1. **Public Parameters:**
   - Choose a prime number `p`.
   - Choose a primitive root `g` modulo `p`.

2. **Generate Private Keys:**
   - Each participant (A and B) selects a private key: `private_key_A` and `private_key_B`.

3. **Compute Public Keys:**
   - A computes: `public_key_A = (g^private_key_A) % p`
   - B computes: `public_key_B = (g^private_key_B) % p`

4. **Exchange Public Keys and Compute the Shared Secret:**
   - A computes: `shared_secret_A = (public_key_B^private_key_A) % p`
   - B computes: `shared_secret_B = (public_key_A^private_key_B) % p`
   - Both should get the same shared secret key.

## Usage

### Prerequisites
- Python 3.x installed

### Running the Script

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/diffie-hellman.git
   cd diffie-hellman
   ```
2. Run the script:
   ```sh
   python diffie_hellman.py
   ```
3. Enter the required values when prompted.

### Example
```sh
Enter a prime number (p): 23
Enter a primitive root modulo p (g): 5
Enter the private key for A: 7
Enter the private key for B: 21

Public Parameters:
  Prime number (p): 23
  Primitive root (g): 5

Private Keys:
  Private key for A: 7
  Private key for B: 21

Public Keys:
  Public key for A: 17
  Public key for B: 14

Shared Secret Key (computed by both A and B):
  Shared key: 19
```

## Notes
- This implementation is a basic demonstration and should not be used in real-world secure communications.
- In practical applications, additional security measures such as key hashing and encryption should be applied.

## License
This project is open-source and available under the MIT License.

