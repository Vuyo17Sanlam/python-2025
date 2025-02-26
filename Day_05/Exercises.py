# # Task 1.1
# Scrambled_message = "world the save to time no is there"
# list = Scrambled_message.split(" ")
# list = list[::-1]
# print(" ".join(list))

# Task 1.2
# playlist = "🎵Dancing Queen;🎸Sweet Child O' Mine;🎹Piano Man;🎤Bohemian Rhapsody;🎺All That Jazz"
# songs = playlist.split(";")
# print("My favorite playlist:")
# count = 1
# for song in songs:
#     print(f"{count}. {song}")
#     count += 1


# Task 1.1

points = [(3, 4), (6, 12), (10, 13)]
# distances = []
# for point in points:
#     distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
#     distances.append(round(distance, 2))
# print(distances)


# distances = []
# for point in points:
#     x, y = point
#     distance = (x**2 + y**2) ** 0.5
#     distances.append(round(distance, 2))
# print(distances)

# distances = [round((x**2 + y**2) ** 0.5, 2) for x, y in points]
# print(distances)

books = [
    {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
    {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
    {"title": "Sapiens", "rating": 4, "genre": "History"},
    {"title": "A Brief History of Time", "rating": 4, "genre": "Science"},
    {"title": "Clean Code", "rating": 4.9, "genre": "Technology"},
]
# # Task 1.1
# print([book["title"] for book in books])


# # Task 1.2
# print([book["title"] for book in books if book["genre"] == "Fiction"])


# # Task 1.3
# print([book["title"] for book in books if book["rating"] >= 4.7])
# # There are no books with a rating of 4.7 or higher
# # There is only one book with a rating of 4.7 or higher
# # There are multiple books with a rating of 4.7 or higher


titles = []
for book in books:
    if book["rating"] >= 4.7:
        titles.append(book["title"])
if len(titles) > 1:
    titles_string = ", ".join(titles)
    print(f"Highest rated books are: {titles_string}")
elif len(titles) == 0:
    print("There are no books with a rating of 4.7 or higher😭")
else:
    print(f"The highest rated book is: {titles[0]}")
