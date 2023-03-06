import datetime

def calculate_age(birth_year, birth_month, birth_day):
    today = datetime.date.today()
    age = today.year - birth_year
    if today.month < birth_month or (today.month == birth_month and today.day < birth_day):
        age -= 1
    return age

# Example usage:
birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month: "))
birth_day = int(input("Enter birth day: "))
age = calculate_age(birth_year, birth_month, birth_day)
print("You are", age, "years old.")
