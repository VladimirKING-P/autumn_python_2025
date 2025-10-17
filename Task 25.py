#todo Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.
from fileinput import filename


def count_vowels_in_file():
    # Создаем словарь для подсчета гласных
    vowels_count = {
        'а': 0, 'е': 0, 'ё': 0, 'и': 0, 'о': 0,
        'у': 0, 'ы': 0, 'э': 0, 'ю': 0, 'я': 0,
        'А': 0, 'Е': 0, 'Ё': 0, 'И': 0, 'О': 0,
        'У': 0, 'Ы': 0, 'Э': 0, 'Ю': 0, 'Я': 0
    }

    try:
        # Открываем файл
        with open('dump.txt', 'r', encoding='utf-8') as file:
            # Читаем содержимое файла
            content = file.read()

            # Проходим по каждому символу
            for char in content:
                # Если символ является гласной, увеличиваем счетчик
                if char in vowels_count:
                    vowels_count[char] += 1

        return vowels_count

    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return None


if __name__ == "__main__":
    filename = 'dump.txt'
    result = count_vowels_in_file()

    if result:
        print("Статистика гласных букв:")
        for vowel, count in result.items():
            print(f"Буква '{vowel}': {count} раз(а)")

f = open('Task_25len.txt', 'w', encoding='utf-8')
for vowel, count in result.items():
    f.write(f"Буква '{vowel}': {count} раз(а)\n")


f.close()


