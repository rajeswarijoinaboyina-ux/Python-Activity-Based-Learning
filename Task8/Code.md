# 8. Manufacturing Cost and Profitability Analysis Using Python

## 1. Problem Statement

The Manufacturing Cost and Profitability Analysis System calculates production costs using material costs, labour charges, wastage, and machine costs. It calculates selling price and profit, then checks whether production meets the specified profit target.

## 2. Algorithm

1. Start the program.
2. Enter material, labour, and machine costs.
3. Enter wastage percentage.
4. Calculate total production cost.
5. Enter selling price.
6. Calculate profit.
7. Compare profit with target.
8. Display the result.
9. Stop.

## 3. Flowchart
``` mermaid
flowchart TD
 A([Start]) --> B[/Enter Production Costs/]
 B --> C[Calculate Total Cost]
 C --> D[Enter Selling Price]
 D --> E[Calculate Profit]
 E --> F{Profit Meets Target?}
 F -->|Yes| G[Target Achieved]
 F -->|No| H[Target Not Achieved]
 G --> I[Display Result]
 H --> I
 I --> J([Stop])


```

## 5. Sample Input
Enter material cost: 10000
Enter labour charges: 3000
Enter machine cost: 2000
Enter wastage percentage: 10
Enter selling price: 18000
Enter profit target: 2000

## 6. Sample Output
--- COST ANALYSIS ---
Material Cost: 10000.0
Wastage Cost: 1000.0
Labour Cost: 3000.0
Machine Cost: 2000.0
Total Cost: 16000.0
Selling Price: 18000.0
Profit: 2000.0

Profit Target Achieved


