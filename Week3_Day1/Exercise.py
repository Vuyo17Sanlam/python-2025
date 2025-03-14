"""def mood_report(**feeling):
    mood = feeling.get("mood", "🙂")
    time_of_day = feeling.get("time_of_day", "morning 🌅")
    return f"Feeling {mood} this {time_of_day}."


# Example outputs:
print(mood_report())  # "Feeling 🙂 this morning 🌅."
print(
    mood_report(mood="😎", time_of_day="afternoon ☀️")
)  # "Feeling 😎 this afternoon ☀️."


# Tas"""

books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"author": "J.K. Rowling"},  # Missing title and year
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "To Kill a Mockingbird", "year": 1960},  # Missing author
    {"author": "Ernest Hemingway", "year": 1952},  # Missing title
]


# Output
# '1984' by George Orwell (1949)
# 'Untitled' by J.K. Rowling (N/A)
# 'The Great Gatsby' by F. Scott Fitzgerald (1925)
# 'To Kill a Mockingbird' by Unknown (1960)
# 'Untitled' by Ernest Hemingway (1952)


"""def format_book_info(**book):
    title = book.get("title", "Untitled")
    author = book.get("author", "Unknown")
    year = book.get("year", "N/A")
    return f"'{title}' by {author} ({year})"


def main():
    for book in books:
        print(format_book_info(**book))


main()
"""
recipe = {
    "name": "Spaghetti Carbonara",
    "servings": 4,
    "ingredients": [
        "200g spaghetti",
        "100g pancetta",
        "2 eggs",
        "1/2 cup grated Parmesan",
        "1 clove garlic",
    ],
}

# Task 1
# ======= Spaghetti Carbonara =======
# - 200g spaghetti
# - 100g pancetta
# - 2 eggs
# - 1/2 cup grated Parmesan
# - 1 clove garlic
# Serves: 4 people


def format_recipe_output(name, servings, ingredients):
    output = f"{' ' + name + ' ':=^30}" + "\n"
    output += f"-{'\n-'.join(ingredients)}" + "\n"
    output += f"Serves: {servings} people"
    return output


def main():
    print(format_recipe_output(**recipe))


main()
tuple1 = (1, 3)
tuple2 = {"first": "list1"}
tuple2.update
