# inventory = [
#     {"name": "Apple 🍎", "quantity": 30, "price": 0.50},
#     {"name": "Banana 🍌", "quantity": 20, "price": 0.20},
# ]

# while True:
#     item_name = input("What is the product name? ")
#     item_qty = int(input("What is the quantity? "))
#     item_price = float(input("What is the price? "))
#     if input("Do you want to continue shopping? (Y/N) ").lower() == "n":
#         break

# print(item_name)
# print(item_qty)
# print(item_price)

# product = {"name": item_name, "quantity": item_qty, "price": item_price}
# inventory.append(product)

# spiderman = {
#     "name": "Spiderman",
#     "address": {
#         "city": "New York",
#         "country": "USA",
#     },
#     "age": 25,
# }
# print ( spiderman.get("city") )


# captain_america = {
#     "name": "Steve Rogers 🦸‍♂️",
#     "age": 100,
#     "height": 185,
#     "address": {"city": "Brooklyn", "country": "US"},
# }


# spiderman = {
#     "name": "Peter Parker",
#     "age": 18,
#     "team_name": "Avengers",
#     "team": ["Iron Man", "Thor", "Hulk", "Captain America"],
# }

# hulk = {
#     "name": "Bruce Banner",
#     "age": 35,
# }

# heroes = [captain_america, spiderman, hulk]

# captain_america = {
#     "name": "Steve Rogers 🦸‍♂️",
#     "age": 100,
#     "height": 185,
#     "address": {"city": "Brooklyn", "country": "US"},
# }


# spiderman = {
#     "name": "Peter Parker",
#     "age": 18,
#     "team_name": "Avengers",
#     "team": ["Iron Man", "Thor", "Hulk", "Captain America"],
# }

# hulk = {
#     "name": "Bruce Banner",
#     "age": 35,
# }

# heroes = [captain_america, spiderman, hulk]

# for hero in heroes:
#     adr = hero.get("address", {}).get("city")
#     hero_name = hero["name"]
#     if adr is None:
#         print(f"{hero_name} location is Top Secret 🔒")
#     else:
#         print(f"{hero_name} lives in {adr}")


# # Output
# Steve Rogers 🦸‍♂️ lives in Brooklyn
# Peter Parker location is Top Secret 🔒
# Bruce Banner location is Top Secret 🔒


employees = [
    {"name": "Chelo", "experience": 3},
    {
        "name": "Diyali",
    },
    {
        "name": "Luvuyo",
    },
    {"name": "Jevan", "experience": 4},
]

# increase the experience year in each employee
# for employee in employees:
#     if employee.get("experience"):
#         employee["experience"] += 1
#     else:
#         employee["experience"] = 1


for employee in employees:
    if employee["experience"] > 5:
        employee["status"] = "Senior"
    elif employee["experience"] > 3:
        employee["status"] = "Mid-Level"
    else:
        employee["status"] = "Junior"

print(employees)
