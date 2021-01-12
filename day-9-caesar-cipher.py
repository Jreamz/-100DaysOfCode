### JREAMZ VERSION ###

def caesar(plain_text, direction_text, shift_amount):
    if direction_text == "encode":
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        print(f"The encoded message is {cipher_text}")        
    elif direction_text == "decode":
        direction_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            direction_text += alphabet[new_position] 
        print(f"The decoded message is {direction_text}")

caesar(plain_text=text, direction_text=direction, shift_amount=shift)

### INSTRUCTOR VERSION ###

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}.")

caesar(start_text=text, cipher_direction=direction, shift_amount=shift)
