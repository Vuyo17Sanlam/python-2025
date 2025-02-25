# Task 1.1
# find the letter in each characters name and store it in a new list
# # output: [4, 3, 10, 13, 5, 4]
# avengers = [
#     "Hulk",
#     "Iron man",
#     "Black widow",
#     "Captain america",
#     "Spider man",
#     "Thor",
# ]
# list = []
# for i in range(len(avengers)):
#     list.append(len(avengers[i]))
# print(list)

# # Task 1.2
# list2 = []
# for i in range(len(avengers)):
#     if len(avengers[i]) > 10:
#         list2.append(avengers[i])
# print(list2)


# Task 2.1


total_tax = 0
total = 0
shopping_items = [1000, 5000, 4000, 2000, 3000]
for i in range(len(shopping_items)):
    total += shopping_items[i]
    total_tax += shopping_items[i] + shopping_items[i] * 0.1

print(f"Your total is: R{total}")
print(f"tax: {total_tax - total}")
print(f"Your total with tax is: R{total_tax}")
