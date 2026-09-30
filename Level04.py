# Level #3 - Expense Analyzer
# IS 303 - Hilton
# Rylek Staker

#Creating the expense list
expenses = []

# input loop
expense = 1

while expense != 0:
    expense = float(input("Enter an expense or 0 to finish: "))
    if expense < 0:
        print("Expenses can't be negative.")
    elif expense > 0:
        expenses.append(expense)
    

print(expenses)