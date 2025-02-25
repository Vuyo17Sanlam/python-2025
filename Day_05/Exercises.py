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

distances = [round((x**2 + y**2) ** 0.5, 2) for x, y in points]
print(distances)
