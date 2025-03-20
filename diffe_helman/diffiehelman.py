import random

# Step 1: Public parameters
p = int(input("Enter a prime number (p): "))  # Prime number
g = int(input("Enter a primitive root modulo p (g): "))  # Primitive root modulo p

# Step 2: Generate private keys for A and B
private_key_A = int(input("Enter the private key for A: "))  # Private key for A
private_key_B = int(input("Enter the private key for B: "))  # Private key for B

# Step 3: Compute public keys
public_key_A = pow(g, private_key_A, p)  # A's public key: (g^a) mod p
public_key_B = pow(g, private_key_B, p)  # B's public key: (g^b) mod p

# Step 4: Exchange public keys and compute the shared secret
shared_secret_A = pow(public_key_B, private_key_A, p)  # A computes: (B^a) mod p
shared_secret_B = pow(public_key_A, private_key_B, p)  # B computes: (A^b) mod p

# Step 5: Verify that the shared secrets are the same
assert shared_secret_A == shared_secret_B, "Shared secrets do not match!"

# Output results
print("Public Parameters:")
print("  Prime number (p): " + str(p))
print("  Primitive root (g): " + str(g) + "\n")

print("Private Keys:")
print("  Private key for A: " + str(private_key_A))
print("  Private key for B: " + str(private_key_B) + "\n")

print("Public Keys:")
print("  Public key for A: " + str(public_key_A))
print("  Public key for B: " + str(public_key_B) + "\n")

print("Shared Secret Key (computed by both A and B):")
print("  Shared key: " + str(shared_secret_A))
