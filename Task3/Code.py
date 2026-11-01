
name = input("Enter patient name: ")

consultation = float(input("Consultation charges: "))
diagnostic = float(input("Diagnostic charges: "))
treatment = float(input("Treatment charges: "))

if min(consultation, diagnostic, treatment) < 0:
    print("Invalid billing charges")

else:
    total = consultation + diagnostic + treatment

    concession = 0

    if total >= 5000:
        concession = total * 0.10

    bill = total - concession

    if bill < 3000:
        category = "Low Payment"
    elif bill <= 10000:
        category = "Medium Payment"
    else:
        category = "High Payment"

    print("\nPatient Name:", name)
    print("Total Bill:", total)
    print("Concession:", concession)
    print("Final Bill:", bill)
    print("Patient Category:", category)

