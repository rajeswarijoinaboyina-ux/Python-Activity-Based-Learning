# 10. Campus Event Financial Planning Using Python

## 1. Problem Statement

The Campus Event Financial Planning System calculates event expenses such as venue, equipment, catering, transport, and certificates. It determines participant contributions, sponsorship shortfalls, and the minimum number of registrations required to break even.

## 2. Algorithm

1. Start the program.
2. Enter event expenses.
3. Calculate total event cost.
4. Enter sponsorship amount.
5. Calculate sponsorship shortfall.
6. Enter participant contribution.
7. Calculate minimum registrations required.
8. Display financial report.
9. Stop.

## 3. Flowchart
``` mermain
flowchart TD
 A([Start]) --> B[/Enter Event Expenses/]
 B --> C[Calculate Total Cost]
 C --> D[Enter Sponsorship]
 D --> E[Calculate Shortfall]
 E --> F[Enter Participant Fee]
 F --> G[Calculate Break-Even Registrations]
 G --> H[Display Financial Report]
 H --> I([Stop])



```

## 5. Sample Input
Enter venue cost: 10000
Enter equipment cost: 5000
Enter catering cost: 15000
Enter transport cost: 5000
Enter certificate cost: 2000

Enter sponsorship amount: 12000
Enter participant contribution: 500

## 6. Sample Output
--- EVENT FINANCIAL REPORT ---

Total Event Cost: 37000.0
Sponsorship: 12000.0
Sponsorship Shortfall: 25000.0
Participant Fee: 500.0
Minimum Registrations: 50

Break-even Achieved

