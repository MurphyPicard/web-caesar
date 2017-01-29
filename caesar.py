# returns a number from 0-25 corresponding with a-z or A-Z
def alphabet_position(letter):
    if ord(letter) >= 97 and ord(letter) <= 122: # lowercase letter ascii values
        return ord(letter) - 97
    elif ord(letter) >= 65 and ord(letter) <= 90: # uppercase
        return ord(letter) - 65

# rotates a letter a specified number of times
def rotate_character(char, rot):
    if 97 <= ord(char) <= 122: # char is a lowercase letter
        return chr((alphabet_position(char) + rot) % 26 + 97) # lowercase letter
    elif 65 <= ord(char) <= 90: # char is a capital letter
        return chr((alphabet_position(char) + rot) % 26 + 65) # uppercase
    else:
        return char


def encrypt(text, rot):
    scrambled_text = ""
    for letter in text:
        scrambled_text += rotate_character(letter, rot)
    return scrambled_text
