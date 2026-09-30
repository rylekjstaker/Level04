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
    

#Classify Expenses
small_expenses = 0
moderate_expenses = 0
large_expenses = 0

for number in expenses:
    if number < 25 and number > 0:
        small_expenses += 1
    elif number >= 25 and number <= 100:
        moderate_expenses += 1
    elif number > 100:
        large_expenses += 1

print(small_expenses, moderate_expenses, large_expenses)
print(expenses)