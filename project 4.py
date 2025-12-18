# room=int(input("enter the room rent"))
# electricty_bill=int(input("enter the electricty bill"))
# unit_expend=int(input("enter the unit"))

rent  = int(input("Enter the room rent-: "))
food=int(input("enter the food bill-:"))
electricity_bill = int(input("Enter electricity bill per unit:- "))
unit_expend = int(input("Enter total units used:- "))
persons=int(input("enter the total persons-:"))

# Electricity cost
electricity_cost = electricity_bill * unit_expend

# Total rent
total_rent = (rent + electricity_cost+electricity_cost)/3

print("\n--- Rent Details ---")
print("Room Rent:", rent)
print("Electricity Cost:", electricity_cost)
print("Total Rent to Pay:", total_rent)
