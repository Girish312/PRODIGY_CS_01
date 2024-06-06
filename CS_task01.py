letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if letter == ' ':
            ciphertext += ' '
        else:
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = (index + key) % num_letters
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if letter == ' ':
            plaintext += ' '
        else:
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = (index - key) % num_letters
                plaintext += letters[new_index]
    return plaintext

def main():
    print('Do you want to encrypt or decrypt text?')
    user_input = input('e/d: ').lower()

    if user_input == 'e':
        print('\nENCRYPTION MODE SELECTED')
        text = input('Enter the text to encrypt: ')
        key = int(input('Enter the key between 1 to 26: '))
        ciphertext = encrypt(text, key)
        print(f'CIPHERTEXT: {ciphertext}')

    elif user_input == 'd':
        print('\nDECRYPTION MODE SELECTED')
        text = input('Enter the text to decrypt: ')
        key = int(input('Enter the key between 1 to 26: '))
        plaintext = decrypt(text, key)
        print(f'PLAINTEXT: {plaintext}')
    else:
        print('Invalid option selected. Please choose "e" for encrypt or "d" for decrypt.')

if __name__ == "__main__":
    main()
