def numbers_to_letters(numbers):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(alphabet[int(num)-1] for num in numbers.split())

numbers = input("Введите число через пробел ")
print(numbers_to_letters(numbers))




