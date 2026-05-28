import random

def get_numbers_ticket(min, max, quantity):
    if min < 1:
        return []
    if max > 1000:
        return []
    if quantity < 1 or quantity > (max - min + 1):
        return []
    result = set()    
    while len(result) < quantity:
        number = random.randint(min, max)
        result.add(number)
    return sorted(result)

res = get_numbers_ticket(2, 1001, 5)
print(res)
res = get_numbers_ticket(10, 100, 9)
print(res)
res = get_numbers_ticket(3, 100, 6)
print(res)
