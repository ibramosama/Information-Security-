from tkinter import *

def get_cipherletter(new_key, letter):
    #still need alpha to find letters
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter in alpha:
        return alpha[new_key]
    else:
        return letter

def encrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result
def main():
    x = int(input("hello; for encrypt press 1, for decrypt press 2: "))
    if x == 1:
        print("enter the word for encrypt: ")
        word = input();
        print("enter the key for encrypt: ")
        key = int(input());
        encrypted = encrypt(3, word)
        print("the message after encrypt is: " + encrypted)  # should print "BYFFI QILFX?!"
    # decrypt "BYFFI QILFX?!" with a key of 20
    elif x == 2:
        word = input("enter the word for decrypt: ")
        key = int(input("enter the key for decrypt: "))
        decrypted = decrypt(3, word)
        print("the message after decrypt is: " + decrypted)




