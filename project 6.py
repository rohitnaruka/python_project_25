name = input("Student name: ")
m1 = int(input("Marks 1: "))
m2 = int(input("Marks 2: "))
m3 = int(input("Marks 3: "))

total = m1 + m2 + m3
percent = total / 3

if percent >= 60:
    grade = "A"
elif percent >= 40:
    grade = "B"
else:
    grade = "Fail"

print("\nName:", name)
print("Total:", total)
print("Percentage:", percent)
print("Grade:", grade)
