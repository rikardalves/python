from datetime import date
bi = int(input("Type a year to knows if it's leap year. type 0 to knows actual year: "))
if bi == 0:
    bi = date.today().year
if bi % 4 == 0 and bi % 100 != 0 or bi % 400 == 0:
    print(f"The {bi} is a leap year")
else:
    print(f"The {bi} isn't a leap year")
