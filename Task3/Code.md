# 3. Hospital Billing and Patient Classification Using Python

## 1. Problem Statement

The Hospital Billing System calculates patient bills based on consultation, diagnostic, and treatment charges. It applies concessions based on eligibility, validates billing details, and classifies patients according to their payment amount and payment policy.

## 2. Algorithm

1. Start the program.
2. Enter patient details.
3. Enter consultation, diagnostic, and treatment charges.
4. Calculate the total bill.
5. Apply a concession if eligible.
6. Validate billing constraints.
7. Classify the patient according to payment.
8. Display the final bill.
9. Stop the program.

## 3. Flowchart
``` mermaid
flowchart TD
 A([Start]) --> B[/Enter Patient Details and Charges/]
 B --> C[Calculate Total Bill]
 C --> D{Eligible for Concession?}
 D -->|Yes| E[Apply Concession]
 D -->|No| F[No Concession]
 E --> G[Calculate Final Bill]
 F --> G
 G --> H[Classify Patient]
 H --> I[Display Bill]
 I --> J([Stop])


```

## 5. Sample Input
Enter patient name: Raju
Consultation charges: 1000
Diagnostic charges: 2000
Treatment charges: 3000

## 6. Sample Output
Patient Name: Raju
Total Bill: 6000.0
Concession: 600.0
Final Bill: 5400.0
Patient Category: Medium Payment

