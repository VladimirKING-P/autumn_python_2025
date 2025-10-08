#todo: Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм,
#  4 — тонна, 5 — центнер. Дан номер единицы массы и масса тела M в этих единицах (вещественное число).
#  Вывести массу данного тела в килограммах


# 1 — килограмм
# 2 — миллиграмм,
# 3 — грамм
# 4 — тонна
# 5 — центнер


unit_number = int(input("Введите номер единицы массы (1-5): "))
mass = float(input("Введите массу тела в этих единицах: "))

def convert_to_kilograms(unit_number, mass):
    if unit_number == 1:
        # килограмм
        return mass
    elif unit_number == 2:
        # миллиграмм
        return mass / 1_000_000
    elif unit_number == 3:
        # грамм
        return mass / 1_000
    elif unit_number == 4:
        # тонна
        return mass * 1_000
    elif unit_number == 5:
        # центнер
        return mass * 100
    else:
        raise ValueError("Неправильный номер единицы массы")

mass_in_kilograms = convert_to_kilograms(unit_number, mass)

print(f"Масса тела в килограммах: {mass_in_kilograms:.6f}")