balance = 5000

while True:
    print("\n1.Check Balance  2.Deposit  3.Withdraw  4.Exit")
    choice = input("Choose: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amt = int(input("Deposit amount: "))
        balance += amt
        print("Deposited")

    elif choice == "3":
        amt = int(input("Withdraw amount: "))
        if amt <= balance:
            balance -= amt
            print("Withdrawn")
        else:
            print("Insufficient balance")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
