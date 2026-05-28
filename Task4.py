from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
  
  results = []
  today = datetime.today().date()

  for user in users:
      # get user day of birth(user_db)  and replaced with current year
      user_db = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
      user_db_this_year = user_db.replace(year = today.year)

    # compare dates and add aditional one if condition is True 
    if user_db_this_year < today:
      user_db_this_year = user_db_this_year.replace(year=today.year +1)

    # difference betwen dates
    day_difference = (user_db_this_year - today).days
    if 0 <= day_difference <= 7:
      birth_date = user_db_this_year

      # here we add aditional days if it 5 = Saturday or 6 = Sunday
      if birth_date.weekday() == 5:
        birth_date = birth_date + timedelta(days=2)
      elif birth_date.weekday() == 6:
        birth_date = birth_date + timedelta(days=1)

      results.append({"name": user["name"], "congratulation_date": birth_date.strftime("%Y.%m.%d")})

  return results


users = [
    {"name": "John Doe", "birthday": "1985.05.26"},
    {"name": "Jane Smith", "birthday": "1990.05.31"},
    {"name": "Smith Doe", "birthday": "1990.07.28"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
