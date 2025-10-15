# Создаем алфавит для шифрования
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# Функция для шифрования символа
def caesar_cipher(char, shift):
    if char.lower() in alphabet:
        # Находим позицию символа в алфавите
        position = alphabet.find(char.lower())
        # Вычисляем новую позицию с учетом сдвига
        new_position = (position - shift) % len(alphabet)
        # Сохраняем регистр
        if char.isupper():
            return alphabet[new_position].upper()
        else:
            return alphabet[new_position]
    else:
        return char


# Открываем файл и шифруем
with open('message.txt', 'r', encoding='utf-8') as file:
    # Читаем все строки
    lines = file.readlines()

    # Результат шифрования
    encrypted_text = []

    # Проходим по строкам с учетом сдвига
    for i, line in enumerate(lines):
        # Вычисляем сдвиг для текущей строки
        shift = i + 1
        # Шифруем каждый символ
        encrypted_line = ''.join([caesar_cipher(char, shift) for char in line])
        # Добавляем к результату
        encrypted_text.append(encrypted_line)

# Выводим результат
print("Зашифрованный текст:")
for line in encrypted_text:
    print(line, end='')

