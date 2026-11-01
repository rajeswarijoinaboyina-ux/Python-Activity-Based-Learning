
items = []
n = int(input("Enter number of products: "))
subtotal = 0
tax = 0

for i in range(n):
    name = input("Product name: ")
    category = input("Category (food/electronics): ").lower()
    price = float(input("Price: "))
    qty = int(input("Quantity: "))

    amount = price * qty
    rate = 5 if category == "food" else 18

    item_tax = amount * rate / 100
    subtotal += amount
    tax += item_tax

    items.append((name, qty, amount, item_tax))

discount = subtotal * 0.10 if subtotal >= 5000 else 0
discount = min(discount, 500)

total = subtotal + tax - discount

print("\n--- RETAIL INVOICE ---")

for item in items:
    print(item[0], "Qty:", item[1],
          "Amount:", item[2], "Tax:", item[3])

print("Subtotal:", subtotal)
print("Total Tax:", tax)
print("Discount:", discount)
print("Final Bill: Rs.", round(total, 2))

