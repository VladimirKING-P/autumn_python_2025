#todo Дан номер месяца (1 — январь, 2 — февраль, ...). Вывести название соответствующего
#  времени года ("зима", "весна" и т.д.).


def get_season(month):
    if month in [12, 1, 2]:
        return "зима"
    elif month in [3, 4, 5]:
        return "весна"
    elif month in [6, 7, 8]:
        return "лето"
    elif month in [9, 10, 11]:
        return "осень"
    else:
        return "Неверный номер месяца"


month_number = int(input("Введите номер месяца: "))
print(f"Время года: {get_season(month_number)}")
