fav_movie = "John Wick"

print(fav_movie[5])


print(f"{fav_movie[-4]}{fav_movie[-3]}{fav_movie[-2]}{fav_movie[-1]}")


fav_hero = "The Hulk"  # Strings are immutable

catchphrase = "I am Groot"
print(catchphrase.upper())
print(catchphrase.capitalize())
print(catchphrase.title())
print(catchphrase.swapcase())

# will remove the leading and trailing characters

message = " With great power comes great responsibility "
clean_message = message.strip()
print(clean_message)

print(message.lstrip())
print(message.rstrip())
quote = "Dream is not something that you see in sleep, Dream is something that does not let you sleep"
print(quote.count("Dream"))
print(
    quote.replace(
        "Dream",
        "🛌💭",
    )
)

print(quote.find("something"))
print(quote.find("**"))
