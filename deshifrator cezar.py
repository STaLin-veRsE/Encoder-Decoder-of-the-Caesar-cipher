import os
import sys

def caesar_cipher(text, shift):
    alphabet = 'XYZABCDEFGHIJKLMNOPQRSTUVWXYZ    ЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            if char in alphabet:
                shifted_index = (alphabet.index(char) + shift) % 65
                shifted_char = alphabet[shifted_index]
                result += shifted_char if is_upper else shifted_char.lower()
            else:
                result += char
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

vopros = input("Вы хотите зашифровать или расшифровать текст (шифровать/расшифровать): ")

if vopros == "шифровать":
    text = input("Введите текст,который хотите зашифровать:")
    shift = 3
    encrypted_text = caesar_cipher(text, shift)
    decrypted_text = caesar_decipher(encrypted_text, shift+3)
    print("Вот зашифрованый текст:", encrypted_text)
    
if vopros == "расшифровать":
    text = input("Введите текст,который хотите расшифровать:")
    shift = 3
    encrypted_text = caesar_cipher(text, shift)
    decrypted_text = caesar_decipher(encrypted_text, shift+3)
    print("Вот расшифрованый текст:", decrypted_text)
    
ending = input("Вы хотите завершить работу (завершить/отменить):")

def restart_program():
    os.execv(sys.executable, [sys.executable] + sys.argv)
    
if ending == "завершить":
    exit()