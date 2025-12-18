expenses = []

while True:
    print("\n1.Add Expense  2.View Total  3.Exit")
    ch = input("Choose: ")

    if ch == "1":
        amt = int(input("Amount: "))
        expenses.append(amt)
        print("Added")

    elif ch == "2":
        print("Total Expense:", sum(expenses))

    elif ch == "3":
        break

    else:
        print("Invalid")
