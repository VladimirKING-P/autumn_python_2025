#todo: Вы работаете с данными цен товаров, которые приходят в разном формате.
# Создайте список числовых значений цен,  игнорируя некорректные записи.
# Все цены переведите в рубли. Задачу следует решить с использованием списковых включений.

RATES = {'USD': 80, 'EUR': 90, 'JPY': 0.6, '$': 80}


# Основной список цен
prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99", "18.99", "N/A", "¥5000"]


# Создание списка числовых значений цен в рублях
result = [
    float(price.replace('₽', '')) if '₽' in price
    else float(price.split()[0]) * RATES[price.split()[1]] if len(price.split()) == 2 and price.split()[1] in RATES
    else float(price.replace('€', '')) * RATES['EUR'] if '€' in price
    else float(price.replace('¥', '')) * RATES['JPY'] if '¥' in price
    else float(price.replace('$', '')) * RATES['$'] if '$' in price
    else None
    for price in prices
]

# Фильтруем только числовые значения (убираем None)
result = [price for price in result if price is not None]


print(result)
