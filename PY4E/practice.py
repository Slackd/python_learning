calculationUnits = 24 * 60 * 60
nameUnit = "seconds"

def days_to_units(days):
    print(f"{days} days are {days * calculationUnits} {nameUnit}")

days_to_units(20)
days_to_units(50)
days_to_units(70)
days_to_units(110)
