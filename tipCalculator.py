print("Welcome to the tip Calculator")
bill = input("What was the total bill?")
tipPercentage = input(
    "What percentage tip would you like to give? 10, 12, or 15?")
peopleSplit = input("How many people to split the bill?")
actualPercentage = int(tipPercentage) / 100
tip = float(bill) * actualPercentage
total = tip + float(bill)
final = round(total / int(peopleSplit), 2)
finalDistribute = (f"Each person should pay: {final}")
print(finalDistribute)
