print("Welcome to the tip calculator")
bill= float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people will split the bill? "))

tip_Percent = int(tip)  / 100
check_Percent = bill * tip_Percent
total_Check = (bill) + check_Percent
split = total_Check / people


print(f"Each person should pay: ${split: .2f}")