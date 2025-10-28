class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = max(0, price)  # Гарантируем неотрицательную цену

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            self._price = 0
        else:
            self._price = value


class Order:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        """
        Добавляем товар в заказ
        :param product: экземпляр класса Product
        :return TypeError: если передан не экземпляр Product
        """
        if not isinstance(product, Product):
            raise TypeError('Добавить товар класса Product')
        self._products.append(product)

    def remove_product(self, product):
        """
               Удаляет товар из заказа.
               :param product: экземпляр класса Product для удаления
               :raises ValueError: если товар не найден в заказе
               """
        if product not in self._products:
            raise ValueError(f"Товар '{product.name}' не найден в заказе")
        self._products.remove(product)

    @property
    def total_price(self):
        """
                Вычисляемое свойство — общая стоимость заказа.
                Суммирует цены всех товаров в заказе.
                :return: число (общая стоимость)
                """
        return sum(product.price for product in self._products)

    @property
    def product_count(self):
        """
               Вычисляемое свойство — количество товаров в заказе.
               :return: целое число
               """
        return len(self._products)

    def __len__(self):
        """Возвращает количество товаров в заказе."""
        return len(self._products)

    def __bool__(self):
        """Позволяет проверять, есть ли товары в заказе."""
        return bool(self._products)


if __name__ == "__main__":
    book = Product("Book", 10)
    pen = Product("Pen", 2)

    order = Order()

    # Добавляем товары
    order.add_product(book)
    order.add_product(pen)

    print(f"Общая  стоимость: {order.total_price}")
    print(f"Количество товаров: {order.product_count}")

    # Удаляем товар
    order.remove_product(pen)
    print(f"Общая стоимость после удаления ручки: {order.total_price}")  # 11.5
# проверка заказа
    if order:
        print("Заказ не пустой")
    else:
        print("Заказ пустой")

