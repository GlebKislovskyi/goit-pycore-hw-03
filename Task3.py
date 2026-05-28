import re


def normalize_phone(phone_number):
    """Normalize phone number to +38XXXXXXXXXX format."""
    # Remove all non-digit characters
    digits_only = re.sub(r'\D', '', phone_number)
    
    # Add country code if not present
    if digits_only.startswith('380'):
        return '+' + digits_only
    else:
        return '+38' + digits_only


raw_numbers = [
    "067 123 4567",
    "(095) 234-5678",
    "+380 44 123 4567",
    "380501234567",
    "+38(050)123-32-34",
    "0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
