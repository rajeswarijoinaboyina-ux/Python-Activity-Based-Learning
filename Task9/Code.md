# 9. Multi-Currency Travel Budget Analysis Using Python

## 1. Problem Statement

The Multi-Currency Travel Budget Analysis System converts travel expenses into a selected currency using exchange rates. It includes conversion fees, compares total spending with the budget, and identifies the largest expense category.

## 2. Algorithm

1. Start the program.
2. Enter travel budget.
3. Enter expense categories and amounts.
4. Enter exchange rates.
5. Convert expenses into local currency.
6. Add conversion fees.
7. Calculate total expenses.
8. Identify the largest expense category.
9. Compare spending with budget.
10. Display results and stop.

## 3. Flowchart 
``` mermaid
flowchart TD
 A([Start]) --> B[/Enter Budget and Expenses/]
 B --> C[Enter Exchange Rates]
 C --> D[Convert Expenses]
 D --> E[Add Conversion Fees]
 E --> F[Calculate Total Spending]
 F --> G[Find Largest Expense]
 G --> H{Within Budget?}
 H -->|Yes| I[Budget is Sufficient]
 H -->|No| J[Budget Exceeded]
 I --> K[Display Results]
 J --> K
 K --> L([Stop])
```


## 5. Sample Input
Enter travel budget in INR: 50000
Enter number of expenses: 3

Enter category: Hotel
Enter amount: 100
Enter exchange rate to INR: 85

Enter category: Food
Enter amount: 50
Enter exchange rate to INR: 85

Enter category: Transport
Enter amount: 80
Enter exchange rate to INR: 85

## 6. Sample Output
--- TRAVEL BUDGET REPORT ---

Hotel : Rs. 8670.0
Food : Rs. 4335.0
Transport : Rs. 6936.0

Total Expenses: Rs. 19941.0
Largest Expense: Hotel
Budget Status: Within Budget
Remaining Budget: Rs. 30059.0

