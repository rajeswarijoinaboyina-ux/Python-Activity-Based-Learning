
material = float(input("Enter material cost: "))
labour = float(input("Enter labour charges: "))
machine = float(input("Enter machine cost: "))
wastage = float(input("Enter wastage percentage: "))
selling = float(input("Enter selling price: "))
target = float(input("Enter profit target: "))

if min(material, labour, machine, wastage, selling, target) < 0:
    print("Invalid input")
else:
    waste_cost = material * wastage / 100
    total = material + labour + machine + waste_cost
    profit = selling - total

    print("\n--- COST ANALYSIS ---")
    print("Material Cost:", material)
    print("Wastage Cost:", waste_cost)
    print("Labour Cost:", labour)
    print("Machine Cost:", machine)
    print("Total Cost:", total)
    print("Selling Price:", selling)
    print("Profit:", profit)

    if profit >= target:
        print("Profit Target Achieved")
    else:
        print("Profit Target Not Achieved")

