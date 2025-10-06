# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"

age = "23"
age_namber = int(age)
print (age_namber)


#todo: Преобразуйте переменную age в Boolean
# age = "123abc"

age = "123abc"
bol =int( age == age)
print(age)
print(bol)



#todo: Преобразуйте переменную flag в Boolean
# flag = 1

flag = 1

bolo_one = bool(flag) # True
print(bolo_one)

#todo: Преобразуйте значение в Boolean
# in task6

str_one = "Privet"
str_two = ""

bool_one = bool(str_one)  # True, так как строка не пустая
bool_two = bool(str_two)  # False, так как строка пустая

print(bool_one)
print(bool_two)


#todo: Преобразуйте значение 0 и 1 в Boolean

a = 1
b = 0

print(a == b)   #False
print(a > b)   #False
print(a >= b)   #False
print(a < b)   #True
print(a <= b)   #True
print(a != b)   #True


#todo: Преобразуйте False в строку

bool_value = False
print(type(bool_value))

string_result = str(bool_value)
print(string_result)
print(type(string_result))
