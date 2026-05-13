from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    today = datetime.now()
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError, TypeError:
        print("Ошибка: Неверный формат даты! Ожидается 'YYYY-MM-DD'.")
        return None
    delta = date - today
    return delta.days


res = get_days_from_today("2024-12-31")
print(res)

res = get_days_from_today("20245-12-31")
print(res)
res = get_days_from_today(100)
print(res)
