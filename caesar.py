
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char 
    return result


def decrypt(text, shift):
    return encrypt(text, 26 - shift)


if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (1-25): "))

    encrypted = encrypt(message, shift)
    print("Encrypted Text:", encrypted)

    decrypted = decrypt(encrypted, shift)
    print("Decrypted Text:", decrypted)
