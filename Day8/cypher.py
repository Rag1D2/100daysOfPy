# Create a function that builds a Caesar Cipher
# Will ask user if they want to encode or decode
# Prompt user for input (the message), and then prompt for a shift number
# Cipher will take given message, apply the appropriate shift in letters, and print the ciphered message
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

initialize = input("Would you like to Encode or Decode?\n ").lower()
text = input("Type your message\n ").lower()
shift = int(input("Type the shift number\n"))
cipher_running = True


def encode(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


def decode(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


if initialize == "encode":
    encode(plain_text=text, shift_amount=shift)
elif initialize == "decode":
    decode(plain_text=text, shift_amount=shift)
