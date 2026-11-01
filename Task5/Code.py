
data = int(input("Enter data usage (GB): "))
calls = int(input("Enter call minutes: "))
budget = float(input("Enter budget: "))
required_days = int(input("Enter required validity days: "))

plans = [
    ("Plan A", 199, 2, 100, 28, 20, 1),
    ("Plan B", 299, 3, 200, 56, 15, 1),
    ("Plan C", 399, 5, 300, 84, 10, 1)
]

best = None

for name, price, gb, mins, days, extra_data, extra_call in plans:

    excess = max(0, data - gb) * extra_data
    excess += max(0, calls - mins) * extra_call
    total = price + excess

    print(name, "Total Cost:", total)

    if days >= required_days and total <= budget:
        if best is None or total < best[1]:
            best = (name, total)

print("\n--- BEST MOBILE PLAN ---")

if best:
    print("Plan:", best[0])
    print("Total Cost: Rs.", best[1])
else:
    print("No eligible plan found")

