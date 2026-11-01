
n = int(input("Enter number of passengers: "))
distance = float(input("Enter travel distance (km): "))
total = 0

for i in range(n):
    print("\nPassenger", i+1)
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    cls = input("Enter class (Sleeper/AC): ").lower()

    rate = 2 if cls == "sleeper" else 5

    if distance <= 100:
        fare = distance * rate
    elif distance <= 500:
        fare = 100 * rate + (distance-100) * rate * 0.8
    else:
        fare = (100 * rate + 400 * rate * 0.8
                + (distance-500) * rate * 0.6)

    concession = 0.5 if age >= 60 else 0

    fare = fare * (1-concession) + 50
    total += fare

    print("Passenger:", name)
    print("Ticket Fare: Rs.", round(fare, 2))

print("\nTotal Reservation Fare: Rs.", round(total, 2))

cancel = input("Cancel tickets? (yes/no): ")

if cancel.lower() == "yes":
    penalty = total * 0.20
    print("Cancellation Penalty: Rs.", round(penalty, 2))
    print("Refund Amount: Rs.", round(total-penalty, 2))

