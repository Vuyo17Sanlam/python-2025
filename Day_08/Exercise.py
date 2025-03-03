# Task 1
# Create function


# greet("Ragav") -> Hi Ragav! 👋
# greet("Jamie") -> Hi Jamie! 👋

"""
def greet(name):
    return f"Hi {name}! 👋"
print(greet("Ragav"))

"""
# Task 2
# Create a function named driving_test which takes name, age are parameter and returns eligibility

# Case 1:
# Anita is eligible for driving.

# Case 2:
# Try again after few years 👶🍼

"""def driving_test(name, age):
    return (
        f"{name} is eligible for driving."
        if age >= 18
        else "Try again after few years 👶🍼"
    )


print(driving_test("Anita", 17))
"""


# ## Task 3
# Pattern creation

# `pattern("🥕", 5)`

# ## Output
# 🥕
# 🥕🥕
# 🥕🥕🥕
# 🥕🥕🥕🥕
# 🥕🥕🥕🥕🥕

# `pattern("🥔", 3)`

# ## Output
# 🥔
# 🥔🥔
# 🥔🥔🥔


"""
def pattern(item, num):
    for i in range(1, num+1):
        print(item * i)
pattern("🥕", 5)

# list comprehension
def pattern(item, num):
    print("\n".join([item * i for i in range(1, num+1)]))
pattern("🥕", 5)

"""
emoji = "🥕"
times = 5


# Task 4


"""def greet(name):
    return f"Hi {name}! 👋"


names = ["Anita", "Jamie", "Divyali", "Siyanda"]
for name in names:
    print(greet(name))
"""
# Output
# Hi Anita! 👋
# Hi Jamie! 👋
# Hi Divyali! 👋
# Hi Siyanda! 👋


# Output
# Welcome to our Library app
# Main menu:
# 1. Add book to the library
# 2. Print all the books
# 3. Exit

# Please choose an option: 1
# Please tell me the title?
# Please tell me the author?
# Please tell me the year?
# Please tell me the available?

# Successfully added 😄✅

# Main menu:
# 1. Add book to the library
# 2. Print all the books
# 3. Exit

# Please choose an option: 2

books = [
    {
        "title": "Python Programming",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True,
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "year": 2020,
        "available": True,
    },
    {
        "title": "Learning Python I",
        "author": "Mark Lutz",
        "year": 2013,
        "available": False,
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "year": 2015,
        "available": True,
    },
    {
        "title": "Adavance Python",
        "author": "Mark Lutz",
        "year": 2015,
        "available": False,
    },
]


def book_options():
    book_name = input("Please tell me the title? ")
    author_name = input("Please tell me the author? ")
    year = int(input("Please tell me the year? "))
    avaialbility = bool(input("Please tell me the available? "))
    return book_name, author_name, year, avaialbility


def add_book(book_name, author_name, year, avaialbility):
    books.append(
        {
            "title": book_name,
            "author": author_name,
            "year": year,
            "available": avaialbility,
        }
    )


def show_books():
    return "\n".join([i["title"] for i in books])


def menu_option():
    print(
        """
        Main menu:
        1. Add book to the library
        2. Print all the books
        3. Exit
        """
    )


while True:
    menu_option()
    number = int(input())
    if number == 1:
        add_book(*book_options())
        number = int(input())

    elif number == 2:
        print(show_books())
        menu_option()
        number = int(input())
    elif number == 3:
        print("Bye 😄👋")
        break
    else:
        print("number not in the menu")
        menu_option()
        number = int(input())

# Main menu:
# 1. Add book to the library
# 2. Print all the books
# 3. Exit

# Bye 😄👋
