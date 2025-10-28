# Инкапсуляция и property
#todo: Класс "Товар" (Защита от отрицательной цены)
# Создайте класс Product. У него есть свойства name (простая строка) и price.
# При установке цены проверяйте, что она не отрицательная.
# Если пытаются установить отрицательную цену, устанавливайте 0.

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = 0
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Имя должно быть строкой")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            self._price = 0
        else:
            self._price = value

product = Product("Book", 10)
print(product.price)  # 10

product.price = -5
print(product.price)  # 0


print(product.name)
product.name = "New Book"
print(product.name)

