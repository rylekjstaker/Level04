# Level #4 - Expense Analyzer
# IS 303 - Hilton
# Rylek Staker

#Creating the expense list
expenses = []
expense = 1

# input loop
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


#Calculate results
expense_count = len(expenses)
total_expense = sum(expenses)
average_expense = total_expense / expense_count
smallest_expense = min(expenses)
largest_expense = max(expenses)

#Print results
print("Expense Summary")
print("---------------")
print(f'Number of expenses: {expense_count}')
print(f'Total: ${total_expense:,.2f}')
print(f'Average: ${average_expense:,.2f}')
print(f'Smallest expense: ${smallest_expense:,.2f}')
print(f'Largest expense: ${largest_expense:,.2f}')

print(f'\nSmall expenses: {small_expenses}')
print(f'Moderate expenses: {moderate_expenses}')
print(f'Large expenses: {large_expenses}')


