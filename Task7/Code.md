# 7. Retail Billing with Multiple Discount Rules Using Python

## 1. Problem Statement

The Retail Billing System processes multiple products and quantities, calculates category-specific taxes, applies discounts based on purchase amounts, and limits maximum concessions. Finally, it generates an itemized invoice showing the total bill.

## 2. Algorithm

1. Start the program.
2. Enter the number of products.
3. Enter product name, category, price, and quantity.
4. Calculate subtotal.
5. Apply category-specific taxes.
6. Apply threshold discounts.
7. Check maximum discount limit.
8. Calculate final bill.
9. Display itemized invoice.
10. Stop.

## 3. Flowchart
``` mermaid
flowchart TD
 A([Start]) --> B[/Enter Product Details/]
 B --> C[Calculate Subtotal]
 C --> D[Apply Category Tax]
 D --> E[Apply Discount]
 E --> F[Check Maximum Discount]
 F --> G[Calculate Final Bill]
 G --> H[Display Invoice]
 H --> I([Stop])



##  5.Sample Input
Enter number of products: 2

Product name: Rice
Category: food
Price: 1000
Quantity: 2

Product name: Mobile
Category: electronics
Price: 3000
Quantity: 1

## 6. Sample Output
--- RETAIL INVOICE ---

Rice Qty: 2 Amount: 2000 Tax: 100
Mobile Qty: 1 Amount: 3000 Tax: 540

Subtotal: 5000
Total Tax: 640
Discount: 500

Final Bill: Rs. 5140.0

Note: Tax rates and discount rules are illustrative values for this project.
