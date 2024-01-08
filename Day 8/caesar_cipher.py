def encrypt(plain_text, shift_amount):
    sample_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]
            sample_text += new_letter
        else:
            sample_text += char
    print(sample_text)

def decrypt(plain_text,shift_amount):
    sample_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift)
            new_letter = alphabet[new_position]
            sample_text += new_letter
        else:
            sample_text += char
    print(sample_text)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(plain_text=text, shift_amount=shift)


