avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]
name_lengths = list(map(lambda name: len(name), avengers))
print(name_lengths)
hero_names = list(filter(lambda name: len(name) > 10, avengers))
print(hero_names)
# Task (map or filter)
# Number letter in the name
# [4, 8, 11, 15, 10, 4]
scores = [
    {
        "marks": 32,
        "name": "Yvette Merritt",
    },
    {
        "marks": 57,
        "name": "Lillian Ellis",
    },
    {
        "marks": 22,
        "name": "Mccall Carter",
    },
    {
        "marks": 21,
        "name": "Pate Collier",
    },
    {
        "marks": 91,
        "name": "Debra Beard",
    },
    {
        "marks": 75,
        "name": "Nettie Hancock",
    },
    {
        "marks": 20,
        "name": "Hatfield Hodge",
    },
]

filtered_names = list(
    map(
        lambda student: student["name"],
        filter(lambda student: student["marks"] > 40, scores),
    )
)
# print(filtered_names)


fillered_marks = list(filter(lambda x: x["marks"] > 40, scores))
extracted_names = list(map(lambda x: x["name"], fillered_marks))
print(extracted_names)


sorted_scores = sorted(scores, key=lambda student: student["marks"])
print(sorted_scores[-1]["name"])
