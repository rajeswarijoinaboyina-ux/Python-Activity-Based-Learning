
students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i+1)
    name = input("Name: ")
    marks = float(input("Aggregate marks: "))
    subject = list(map(int, input("3 subject marks: ").split()))
    attendance = float(input("Attendance: "))
    income = float(input("Family income: "))

    if (marks >= 75 and len(subject) == 3
        and min(subject) >= 50 and max(subject) <= 100
        and attendance >= 75 and attendance <= 100
        and income <= 250000 and income >= 0):

        students.append((name, marks, attendance, income))

students.sort(key=lambda x: (-x[1], -x[2], x[3], x[0].lower()))

print("\nScholarship Eligible Students")
for rank, s in enumerate(students, 1):
    print(rank, s[0], s[1], s[2], s[3])

print("Total Eligible Students:", len(students))

