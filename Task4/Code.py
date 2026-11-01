
name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentive = float(input("Enter incentives: "))

if min(basic, allowance, overtime, incentive) < 0:
    print("Invalid salary details")
else:
    gross = basic + allowance + overtime + incentive

    if gross <= 20000:
        deduction = gross * 0.05
    elif gross <= 40000:
        deduction = 1000 + (gross - 20000) * 0.10
    else:
        deduction = 3000 + (gross - 40000) * 0.15

    net = gross - deduction

    print("\n--- SALARY STATEMENT ---")
    print("Employee Name:", name)
    print("Basic Salary:", basic)
    print("Gross Salary:", gross)
    print("Total Deduction:", deduction)
    print("Net Salary:", net)

