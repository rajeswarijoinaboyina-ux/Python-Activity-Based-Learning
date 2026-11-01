# University Scholarship Allocation System Using Python

Project Title: University Scholarship Allocation System

Programming Language: Python

## 1. Problem Statement

The University Scholarship Allocation System is designed to identify eligible students for scholarships based on their academic performance, attendance percentage, and family income.

The system evaluates each applicant using the following criteria:

1. Aggregate Marks: Students must score at least 75% aggregate marks.
2. Subject-wise Minimum Marks: Students must score at least 50 marks in each subject.
3. Attendance: Students must have at least 75% attendance.
4. Family Income: Annual family income must not exceed ₹2,50,000.

The system ranks eligible students based on their aggregate marks. If two or more students have equal aggregate marks, ties are resolved using attendance, lower family income, and alphabetical order of names.

The main objective is to make scholarship allocation fair, transparent, and efficient.

## 2. Algorithm

Step-by-step algorithm:

1. Start the program.
2. Read the number of applicants.
3. Enter each student's name.
4. Enter aggregate marks.
5. Enter subject-wise marks.
6. Enter attendance percentage.
7. Enter annual family income.
8. Check all eligibility conditions.
9. If all conditions are satisfied, add the student to the eligible list.
10. Sort eligible students using these tie-breaking rules:
    - Higher aggregate marks.
    - Higher attendance.
    - Lower family income.
    - Alphabetical order of name.
11. Display the eligible students with their ranks.
12. Display the rejected students and reasons.
13. Stop the program.

## 3. Flowchart
``` mermaid
flowchart TD
 A([Start]) --> B[/Enter Student Details/]
 B --> C{Check Eligibility}
 C -->|Eligible| D[Add to Eligible List]
 C -->|Not Eligible| E[Reject Student]
 D --> F[Rank Students]
 E --> F
 F --> G[Display Results]
 G --> H([Stop])



```

## 5. Sample Input
Enter number of applicants: 4

Enter details of Student 1
Student Name: Ravi
Aggregate Marks (%): 90
Enter marks in 3 subjects: 85 90 95
Attendance (%): 85
Annual Family Income: 200000

Enter details of Student 2
Student Name: Sita
Aggregate Marks (%): 90
Enter marks in 3 subjects: 90 92 88
Attendance (%): 90
Annual Family Income: 220000

Enter details of Student 3
Student Name: Anu
Aggregate Marks (%): 85
Enter marks in 3 subjects: 80 85 90
Attendance (%): 80
Annual Family Income: 180000

Enter details of Student 4
Student Name: Ram
Aggregate Marks (%): 70
Enter marks in 3 subjects: 65 70 75
Attendance (%): 80
Annual Family Income: 150000

## 6. Sample Output
===== SCHOLARSHIP ELIGIBLE STUDENTS =====

Rank  Name       Aggregate  Attendance  Income
1     Sita       90.0       90.0        220000.0
2     Ravi       90.0       85.0        200000.0
3     Anu        85.0       80.0        180000.0

===== NOT ELIGIBLE STUDENTS =====

Ram : Low aggregate marks

Scholarship allocation process completed.

