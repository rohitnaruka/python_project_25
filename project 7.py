




contacts = {}

while True:
    print("\n1.Add  2.View  3.Search  4.Exit")
    ch = input("Choose: ")

    if ch == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Saved")

    elif ch == "2":
        print(contacts)

    elif ch == "3":
        name = input("Search name: ")
        print(contacts.get(name, "Not found"))

    elif ch == "4":
        break

    else:
        print("Invalid")
