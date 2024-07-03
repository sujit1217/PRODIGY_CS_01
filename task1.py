def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if mode == 'decrypt':
                shift_amount = -shift_amount
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (Enter 'q' to quit): ").lower().strip()
        print(f"Your choice: {choice}")  # Debugging statement

        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("Please choose 'e' to encrypt or 'd' to decrypt.")
            continue
        
        message = input("Enter your message: ").strip()
        try:
            shift = int(input("Enter the shift value: ").strip())
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
        
        if choice == 'e':
            result = caesar_cipher(message, shift, mode='encrypt')
            print(f"Encrypted message: {result}")
        elif choice == 'd':
            result = caesar_cipher(message, shift, mode='decrypt')
            print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
