# secret_message = "   Programming in Python is not only powerful but it is also fun!   "
# secret_message = secret_message.strip()
# index_python = secret_message.find("Python")
# index_powerful = secret_message.find("powerful")
# print(
#     secret_message[index_python : index_python + 6].upper()
#     + "-"
#     + secret_message[index_powerful : index_powerful + 8].upper()
# )


# flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"
# reverse_message = flipped_message[::-1]
# print(reverse_message)
# index_python = reverse_message.find("Python")
# index_powerful = reverse_message.find("powerful")

# print(
#     reverse_message[index_python : index_python + 6].lower()
#     + " 🗡️  "
#     + reverse_message[index_powerful : index_powerful + 8].lower()
#     + " 🌸"
# )


# Dot chaining strip().upper()

message = "    🚨🔍📱🔑secret_code✌️"
index_key = message.find("🔑")
print(message[index_key + 1 :].upper())
