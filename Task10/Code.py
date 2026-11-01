
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))

sponsor = float(input("Enter sponsorship amount: "))
fee = float(input("Enter participant contribution: "))

total = venue + equipment + catering + transport + certificates

shortfall = max(0, total - sponsor)

if fee > 0:
    registrations = (shortfall + fee - 1) // fee
else:
    registrations = 0

print("\n--- EVENT FINANCIAL REPORT ---")
print("Total Event Cost:", total)
print("Sponsorship:", sponsor)
print("Sponsorship Shortfall:", shortfall)
print("Participant Fee:", fee)
print("Minimum Registrations:", int(registrations))

if sponsor + registrations * fee >= total:
    print("Break-even Achieved")
else:
    print("Break-even Not Achieved")

