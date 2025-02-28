from email.headerregistry import Address

guests = [
    {"name": "Alice", "age": 25, "code": "VIP123"},
    {"name": "Bob", "age": 17, "code": "VIP123"},
    {"name": "Charlie", "age": 30, "code": "VIP123"},
    {"name": "Dave", "age": 22, "code": "GUEST"},
    {"name": "Eve", "age": 29, "code": "VIP123"},
]


blacklist = ["Dave", "Eve"]

# Task
# People who are 21 or above and VIP123
# Blacklist are not allowed


PASS_CODE = "VIP123"

guestlist = []  # ?

# task 1.1

# # for loop
# for guest in guests:
#     if (
#         guest.get("code") == PASS_CODE
#         and guest.get("age", 0) >= 21
#         and guest.get("name") not in blacklist
#     ):
#         guestlist.append(guest.get("name"))
# print(guestlist)

# # list comprehension
# guestlist = [
#     guest.get("name")
#     for guest in guests
#     if guest.get("age", 0) >= 21
#     and guest.get("code") == PASS_CODE
#     and guest.get("name") not in blacklist
# ]
# print(guestlist)


# for guest in guests:
#     if (
#         guest["age"] >= 21
#         and guest["code"] == PASS_CODE
#         and guest["name"] not in blacklist
#     ):
#         guestlist.append(guest["name"])
# print(guestlist)


# guestlist = [
#     guest["name"]
#     for guest in guests
#     if guest["age"] >= 21
#     and guest["code"] == PASS_CODE
#     and guest["name"] not in blacklist
# ]
# print(guestlist)


# Task 2 (Challenging)
# Use nested dictionary comprehension to create a dictionary of restaurants with items under $10

# Restaurant menus with emoji food items and prices
restaurant_menus = [
    {
        "restaurant": "Italian Place",
        "menu": {"🍕": 12.99, "🍝": 10.99, "🥖": 3.99, "🥗": 7.99},
    },
    {
        "restaurant": "Burger Joint",
        "menu": {"🍔": 8.99, "🍟": 3.99, "🥤": 1.99, "🍦": 4.99},
    },
    {
        "restaurant": "Sushi Bar",
        "menu": {"🍣": 15.99, "🍜": 12.99, "🍙": 6.99, "🍶": 9.99},
    },
    {
        "restaurant": "Health Spot",
        "menu": {"🥗": 9.99, "🥙": 8.99, "🥑": 4.99, "🥝": 3.99},
    },
]

# Expected output
# Output
"""
{
    "Italian Place": {"🥖": 3.99, "🥗": 7.99},
    "Burger Joint": {"🍔": 8.99, "🍟": 3.99, "🥤": 1.99, "🍦": 4.99},
    "Sushi Bar": {"🍙": 6.99},
    "Health Spot": {"🥙": 8.99, "🥑": 4.99, "🥝": 3.99},
}
"""
okay = {
    place["restaurant"]: {
        key: value for key, value in place["menu"].items() if value < 10
    }
    for place in restaurant_menus
}
# print(okay)
# for restaurant in restaurant_menus:
#     print(
#         {
#             restaurant["restaurant"]: {
#                 item: price for item, price in restaurant["menu"].items() if price < 10
#             }
#         }
#     )


# filtered_menus = {
#     restaurant["restaurant"]: {
#         item: price for item, price in restaurant["menu"].items() if price < 10
#     }
#     for restaurant in restaurant_menus
# }

# print(id(filtered_menus))


t1 = [100, 200]

employees_hours = {
    "Alice": {"Monday": 8, "Tuesday": 7, "Wednesday": 5, "Thursday": 9, "Friday": 6},
    "Bob": {"Monday": 4, "Tuesday": 5, "Wednesday": 3, "Thursday": 4, "Friday": 5},
    "Charlie": {"Monday": 10, "Tuesday": 9, "Wednesday": 8, "Thursday": 7, "Friday": 6},
    "Dave": {"Monday": 6, "Tuesday": 7, "Wednesday": 5, "Thursday": 8, "Friday": 7},
}


print(
    {
        employee: {
            day: hour for day, hour in employees_hours[employee].items() if hour > 6
        }
        for employee in employees_hours.keys()
        if sum(employees_hours[employee].values()) > 30
    }
)
