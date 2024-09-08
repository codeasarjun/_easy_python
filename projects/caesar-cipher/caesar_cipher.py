def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        print("Select operation:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")

        if choice == '3':
            break
        
        if choice in ['1', '2']:
            text = input("Enter text: ")
            shift = int(input("Enter shift value: "))

            if choice == '1':
                result = encrypt(text, shift)
                print(f"Encrypted text: {result}")
            elif choice == '2':
                result = decrypt(text, shift)
                print(f"Decrypted text: {result}")

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
