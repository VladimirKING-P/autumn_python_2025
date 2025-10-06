#todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.
# Пример:
# x = 10
# y = 15
# z = 2
# Ответ:
# Наибольшее число 15

x = 10
y = 15
z = 2

# Нахождение наибольшего числа
# max
if x >= y and x >= z:
    max_namber: int = x
elif y >= x and y >= z:
    max_namber: int = y
elif z >= x and z >= y:
    max_namber: int = z

print(f"Наибольщее число {max_namber}")


#todo: Пример:
# x = 77
# y = 9
# z = 130
# Ответ:
# Наибольшее число 130

# Задачу решить без функций max и прочих.
# Значение переменных может меняться


x: int = 77
y: int = 9
z: int = 130

if x <= y and x <= z:
    print('Наибольшее число', y)
elif y >= x and y >= z:
    print('Наибольщее число', x)
else :
    print ('Наибольшее число ', z)
    


