A simple command-line tool written in Python to perform encryption and decryption using the Caesar cipher algorithm.


The `Caesar cipher` is one of the simplest and oldest encryption techniques. Named after `Julius Caesar`, who used it to encode his private messages, it works by shifting each letter in the message a fixed number of places down or up the alphabet.

## Features

- Encrypt messages using a Caesar cipher with a specified shift value.
- Decrypt messages that were encrypted using a Caesar cipher.

```bash
Select operation:
1. Encrypt
2. Decrypt
3. Exit
Enter choice (1-3): 1
Enter text: Hello World
Enter shift value: 3
Encrypted text: Khoor Zruog
```
```bash
Select operation:
1. Encrypt
2. Decrypt
3. Exit
Enter choice (1-3): 2
Enter text: Khoor Zruog
Enter shift value: 3
Decrypted text: Hello World
```

## How It Works

### Shift Value
You choose a number, called the shift value or key. This number determines how many positions each letter in the message will be shifted.

### Encryption
To encrypt a message, you shift each letter in the message forward by the shift value. For example, if the shift value is 3:

- The letter 'A' becomes 'D'
- The letter 'B' becomes 'E'
- The letter 'Z' becomes 'C' (since it wraps around from the end of the alphabet)

### Decryption
To decrypt a message, you shift each letter backward by the same shift value. This reverses the encryption and retrieves the original message.

### Example
**Original Message:** HELLO  
**Shift Value:** 3  
**Encrypted Message:** KHOOR

Here's how it works with the shift value of 3:

- 'H' (the 8th letter) becomes 'K' (the 11th letter)
- 'E' (the 5th letter) becomes 'H' (the 8th letter)
- 'L' (the 12th letter) becomes 'O' (the 15th letter)
- 'O' (the 15th letter) becomes 'R' (the 18th letter)

### Decryption Example
**Encrypted Message:** KHOOR  
**Shift Value:** 3  
**Decrypted Message:** HELLO

Here, each letter is shifted back by 3 positions:

- 'K' becomes 'H'
- 'H' becomes 'E'
- 'O' becomes 'L'
- 'R' becomes 'O'

