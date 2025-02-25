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


# Task 2.2

total = 0
tax = 0.1
shopping_items = [1_000, 5_000, 4_000, 2_000, 3_000]
for price in shopping_items:
    total += price

tax_amt = total * tax

print(f"Your total is: R{total}")
print(f"tax (10%) is: R{tax_amt}")
print(f"Your grand total is: R{total + tax_amt}")
