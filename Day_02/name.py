name = "Chelo, says"
age = 20
balance = 1000000.50
is_rich = True

print(name)
print(age)
print(balance)

# Dynamically typed > Python smart

print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(balance))  # <class 'float'>
print(type(is_rich))  # <class 'bool'>

# {} -> interpolation
# {} -> expression are allowed
# auto converts for us.

print("My name is " + name)
print(f"My age is {age}")
print(f"She has {2 * 2000} followers 😘")
