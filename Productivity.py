Name = input("Enter Employee Name: ")
Shifts =int(input("Number of Shifts: "))
Transactions = int(input("Number of transactions: "))
DollarValue = int(input("Transaction dollar value: "))
Pscore = (DollarValue/Transactions/Shifts)

if Pscore <= 30:
    bonus = 50.00
elif Pscore >= 31 and Pscore <= 69:
    bonus = 75.00
elif Pscore >= 70 and Pscore <= 199:
    bonus = 100.00
elif Pscore >= 200.00:
    bonus = 200.00




print("Employee Name: " + str(Name))
print("Employee Bonus: $" + str(bonus))