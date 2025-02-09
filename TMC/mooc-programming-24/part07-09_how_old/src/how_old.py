# Write your solution here
from datetime import datetime, timedelta
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

waktu = datetime(year, month, day)
eve = datetime(1999, 12, 31)

hasil = eve - waktu

if hasil.days < 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {hasil.days} days old on the eve of the new millennium.")