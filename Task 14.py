#todo: Дан массив размера N. Найти минимальное расстояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !

def find_min_distance(arr):

    indices = {}

    # Заполняем словарь
    for i, value in enumerate(arr):
        if value not in indices:
            indices[value] = []
        indices[value].append(i)

    min_dist = float('inf')  # Минимальное расстояние
    result = None  # Результат (индексы)

    # Ищем минимальное расстояние для каждого значения
    for value, idx_list in indices.items():
        if len(idx_list) < 2:
            continue  # Если значение встречается только один раз

        # Ищем минимальное расстояние между соседними индексами
        for i in range(1, len(idx_list)):
            dist = idx_list[i] - idx_list[i - 1]
            if dist < min_dist:
                min_dist = dist
                result = (idx_list[i - 1], idx_list[i])

    return result, min_dist

arr = input()
indices, distance = find_min_distance(arr)


print(f"Минимальные индексы: {indices}")
print(f"Минимальное расстояние: {distance}")

