
budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expenses: "))

expenses = {}
total = 0

for i in range(n):
    category = input("\nEnter category: ")
    amount = float(input("Enter amount: "))
    rate = float(input("Enter exchange rate to INR: "))

    fee = amount * rate * 0.02
    converted = amount * rate + fee

    expenses[category] = converted
    total += converted

largest = max(expenses, key=expenses.get)

print("\n--- TRAVEL BUDGET REPORT ---")
for category, cost in expenses.items():
    print(category, ": Rs.", round(cost, 2))

print("Total Expenses: Rs.", round(total, 2))
print("Largest Expense:", largest)

if total <= budget:
    print("Budget Status: Within Budget")
else:
    print("Budget Status: Budget Exceeded")

print("Remaining Budget: Rs.", round(budget-total, 2))

