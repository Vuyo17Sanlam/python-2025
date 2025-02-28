movies = [
    {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
    {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
    {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
    {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
    {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
]
# Task 1.1

print([movie["title"] for movie in movies])


# Task 1.2

print([sum(movie["ratings"]) / len(movie["ratings"]) for movie in movies])

# Task 1.3

# [
#     {"title": "Inception", "ratings": [5, 4, 5, 4, 5], "average_rating": 4.6},
#     {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4], "average_rating": 4.2},
#     {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4], "average_rating": 4.1},
#     {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5], "average_rating": 5},
#     {"title": "Memento", "ratings": [4, 5, 4, 5, 4], "average_rating": 4.2},
# ]

# print(
#     [
#         {**movie, "average_rating": sum(movie["ratings"]) / len(movie["ratings"])}
#         for movie in movies
#     ]
# )


# print(
#     [
#         movie["title"]
#         for movie in movies
#         if sum(movie["ratings"]) / len(movie["ratings"]) >= 4.5
#     ]
# )


# print([ movie["average_rating"] = sum(movie["ratings"])/len(movie["ratings"]) for movie in movies])

# updated_movies = [
#     {**movie, "average_rating": sum(movie["ratings"]) / len(movie["ratings"])}
#     for movie in movies
# ]
# high_rated_movies = [
#     mov["title"] for mov in updated_movies if mov["average_rating"] >= 4.6
# ]

# print(high_rated_movies)

# dict = {}
# for i in range(1, 6):
#     dict[i] = i * i
# print(dict)

print({i: "even" if i % 2 == 0 else "odd" for i in range(1, 10)})


# Task 1.2

fruits = {"apple": 1.2, "banana": 2.5, "orange": 3.0, "kiwi": 4.0}

print({fruit for fruit in fruits.items() if fruit[1] > 2.0})


# Task 1.3
employees = [
    {"id": 101, "name": "Alice", "age": 30},
    {"id": 102, "name": "Bob", "age": 35},
    {"id": 103, "name": "Charlie", "age": 40},
    {"id": 104, "name": "David", "age": 45},
    {"id": 105, "name": "Eve", "age": 50},
]

print({employee.get("id"): employee.get("name") for employee in employees})
print(
    {
        employee.get("id"): employee.get("age")
        for employee in employees
        if employee["age"] > 28
    }
)
