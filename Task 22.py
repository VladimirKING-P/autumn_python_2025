#todo: Модифицировать программу таким образом чтобы она выводила
# приветствие "Hello", которое только что записали в файл text.txt
# f = open("text.txt", "w+t")
# f.write("Hello\n")
# Ваше решение.
# f.close()
import requests

with open('Task22text.txt', 'w+t', encoding="utf-8") as f:
  # Записываем приветствие в файл
  f.write('Hello\n')

  # Перемещаемся в начало файла для чтения
  f.seek(0)

  # Читаем и выводим содержимое
  print(f.read().strip())




