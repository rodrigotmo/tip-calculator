# This code calculates how much each person will pay in a bill adding the tip to it.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? (10, 12, 15)\n"))
people = int(input("How many people to split the bill?\n"))

bill_per_person = (bill * (tip / 100 + 1)) / people
result = round(bill_per_person, 2)
print(f"Each person should pay: ${result}")