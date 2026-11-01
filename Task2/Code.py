
bills = []

n = int(input("Enter number of months: "))

for i in range(n):
    units = float(input("Enter units consumed: "))

    if units <= 100:
        charge = units * 2
    elif units <= 200:
        charge = 100 * 2 + (units-100) * 3
    else:
        charge = 200 + 300 + (units-200) * 5

    fixed = 50
    surcharge = charge * 0.05
    rebate = 20 if units < 100 else 0

    total = charge + fixed + surcharge - rebate
    bills.append(total)

    print("Monthly Bill: Rs.", round(total, 2))

print("\nMonthly Bill Comparison")

for i in range(1, n):
    increase = bills[i] - bills[i-1]

    if increase > bills[i-1] * 0.30:
        print("Month", i+1, ": Unusual Increase")
    else:
        print("Month", i+1, ": Normal")

print("All Bills:", bills)

