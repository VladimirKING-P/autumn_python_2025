#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


cipher_text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for shift in range(1, 27):  # Пробуем все возможные сдвиги от 1 до 25
    decrypted_message = ' '
    for char in cipher_text:
        if char.lower() in alphabet:
            position = alphabet.find(char.lower())
            new_position = (position - shift) % len(alphabet)
            if char.isupper():
                decrypted_message += alphabet[new_position].upper()
            else:
                decrypted_message += alphabet[new_position]
        else:
            decrypted_message += char
    print(f"Сдвиг {shift}: {decrypted_message}")

