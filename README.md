# PyFuscator

![PyFuscator](https://raw.githubusercontent.com/PyCSharp/PyFuscator/refs/heads/main/image.png?token=GHSAT0AAAAAADKMP6VAQIQUEMSCKCIRMKU42GTNJDQ)

A multi-stage Python script obfuscator that transforms Python code into obfuscated and encrypted forms. Includes optional junk code injection, base64 encoding, hex manipulation, XOR encryption, and Fernet encryption.  

> **Disclaimer:** This tool is for educational purposes and testing code protection. Use responsibly.

---

## Features

**Multi-stage obfuscation:**  
  1. Base64 encoding  
  2. Hex transformation with character substitution  
  3. XOR encryption with a random key  
  4. Fernet encryption  
  5. Compilation to `.pyc`  

- **Optional Junk Code Injection:** Adds meaningless functions to make reverse-engineering harder.  
- **Supports multiple obfuscation stages:** Layers of transformations for better protection.  

---

## Requirements

- Python 3.8+  
- [cryptography](https://pypi.org/project/cryptography/) library  

Install dependencies:

```bash
pip install cryptography
