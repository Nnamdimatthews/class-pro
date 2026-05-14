print("Welcome to the Birthday Store! Buy all your birthday essentials here.")
print("\nWe have the following items in stock:")
items = {
    "Balloons": 1.50,
    "Birthday Cake": 20.00,
    "Party Hats": 2.00,
    "Toys": 5.00,
    "Gift Cards": 25.00,
    "Gift Wrapping": 3.00
}
for item, price in items.items():
    print(f"{item}: ${price:.2f}")

print("\nLet's calculate the total cost of your purchase.")
total_cost = 0
while True:
    item = input("Enter the item you want to buy (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    elif item in items:
        total_cost += items[item]
        print(f"Added {item} to your cart. Current total: ${total_cost:.2f}")
    else:
        print("Sorry, we don't have that item. Please choose from the list.")

print(f"\nYour total cost is: ${total_cost:.2f}")
print("Thank you for shopping at the Birthday Store! Next Please!")


print("\nWelcome to the Birthday Storage! Stock all the dates of your birthdays here.")

birthdays = {}
while True:
    name = input("Enter the name of the person (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    date = input("Enter the birthday date (MM/DD/YYYY): ")
    birthdays[name] = date
    print(f"Added {name}'s birthday on {date} to the storage.")

print("\nHere are all the birthdays you've stored:")
for name, date in birthdays.items():
    print(f"{name}: {date}")
print("\nThank you for using the Birthday Storage! Next Please")

print("\nWelcome to the Birthday Invitation mail! Invite all your friends and family to your birthday party!")

invitations = []
while True:
    name = input("Enter the name of the person to invite (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    invitations.append(name)
    print(f"Added {name} to the invitation list.")

print("\nHere are all the people you've invited:")
for name in invitations:
    print(f"- {name}")
print("\nThank you for using the Birthday Invitation mail! Next... PARTY TIME!")