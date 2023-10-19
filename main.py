
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö',
            'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']

from art import logo
print(logo)

game_on = True
while game_on:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 29

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                posision = alphabet.index(char)
                new_posision = posision + shift_amount
                new_letter = alphabet[new_posision]
                end_text += new_letter
            else:
                end_text += char
        print(f"The {cipher_direction}d text is {end_text}")



    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Do you want to go again, type 'yes', otherwise type 'no'\n")
    if result == "no":
        game_on = False
        print("Goodbye!")
