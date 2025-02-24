# Conditional (Control Flow)
# take a decision -> Choice

# if....else
# if no_of_person <= 2 -> bike else car

no_of_person = 4
if no_of_person <= 2:
    print("We will take the bike for the party")
else:
    print("We will take the car for the party")


# Task 1.2


name1 = input("person1 name? ")
name2 = input("person2 name? ")
height1 = float(input("person1 height? "))
height2 = float(input("person2 height? "))
difference = abs(height1 - height2)
if height1 > height2:
    print(f"{name1} is taller than {name2} by {difference}cm")
elif height1 < height2:
    print(f"{name2} is taller than {name1} by {difference}cm")
else:
    print(f"{name1} and {name2} are of the same height")


# lexical Order: e.g. a < b < c
