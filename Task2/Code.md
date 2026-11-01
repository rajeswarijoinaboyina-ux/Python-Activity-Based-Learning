# Progressive Electricity Billing System Using Python

## 1. Problem Statement

The Progressive Electricity Billing System calculates household electricity bills based on monthly electricity consumption.

The system uses multiple consumption slabs, fixed charges, surcharges, and rebates to calculate the total bill. It also compares bills across different months and identifies unusual increases in electricity usage.

## 2. Algorithm

1. Start the program.
2. Enter the number of months.
3. Enter monthly electricity units.
4. Calculate charges using different slabs.
5. Add fixed charges and surcharge.
6. Apply rebate if applicable.
7. Calculate the final bill.
8. Compare monthly bills.
9. Identify unusual increases.
10. Display monthly bills and stop.

## 3. Flowchart
``` mermaid
flowchart TD
 A([Start]) --> B[/Enter Monthly Units/]
 B --> C[Calculate Slab Charges]
 C --> D[Add Fixed Charges]
 D --> E[Add Surcharge]
 E --> F[Apply Rebate]
 F --> G[Calculate Final Bill]
 G --> H{More Months?}
 H -->|Yes| B
 H -->|No| I[Compare Monthly Bills]
 I --> J[Identify Unusual Increase]
 J --> K[Display Bills]
 K --> L([Stop])

```

## 5. Sample Input
Enter number of months: 3

Enter units consumed: 80
Enter units consumed: 120
Enter units consumed: 250

## 6. Sample Output
Monthly Bill: Rs. 218.0
Monthly Bill: Rs. 365.0
Monthly Bill: Rs. 1160.0

Monthly Bill Comparison
Month 2 : Unusual Increase
Month 3 : Unusual Increase

All Bills: [218.0, 365.0, 1160.0]


