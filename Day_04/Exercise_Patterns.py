# task 1.1
count = 1
while count <= 5:
    print("🔥" * count)
    count += 1

# Task 1.2
for i in range(1, 6):
    print("🔥" * i)


# Task 1.3
row = int(input("Please tell the no of rows?: "))
pattern = input("Please tell the pattern?: ")
count = 1
while count <= row:
    print(pattern * count)
    count += 1


# Task 1.4
row = int(input("Please tell the no of rows?: "))
pattern = input("Please tell the pattern?: ")
for i in range(row):
    print(pattern * (i + 1))
