# Data Encryption Standard (DES) Key Generation

## Overview
This Python script generates encryption keys based on a modified version of the Data Encryption Standard (DES). The script takes a user-input string, converts it to binary, applies bit manipulations, and generates 8 encryption keys through bit-shifting and random bit removal.

## Features
- Converts input text to binary representation
- Removes every 8th bit to introduce randomness
- Splits the binary string into left and right halves
- Applies bitwise left shifts based on predefined values
- Generates 8 encryption keys by removing random bits

## Prerequisites
- Python 3.x

## Usage
1. Run the script:
   ```sh
   python script.py
   ```
2. Enter a string when prompted.
3. The script will generate and display 8 encryption keys.

## Code Explanation
### Steps Involved:
1. **Binary Conversion**: The input string is converted into an 8-bit binary format.
2. **Bit Removal**: Every 8th bit is removed to add randomness.
3. **Splitting**: The modified binary string is split into left and right halves.
4. **Bitwise Left Shift**: Both halves undergo left shifts based on predefined values.
5. **Key Formation**: Left and right halves are concatenated and pruned to form keys.
6. **Random Bit Removal**: 8 bits are randomly removed from the new key.
7. **Key Storage & Display**: The final 8 keys are stored and printed.

## Example Output
```
Enter a string: hello
Key 1 = 101010...
Key 2 = 110011...
...
Key 8 = 011100...
```

## Notes
- The bit shift values are predefined in an array (`lt`)
- The random bit removal ensures that the generated keys have additional randomness



