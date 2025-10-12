#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().
# Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.



with open( 'Task20inverted_file.txt', 'r+' ) as file:

    lines = file.readlines()

    file.seek(0,2)

    file.write("\n")
    for line in reversed(lines):
        file.write(line.rstrip('\n')+ '\n')

file.close()
