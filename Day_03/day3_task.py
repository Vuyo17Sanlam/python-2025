# stock1 = "vanilla"
# stock2 = "chocolate"
# stock3 = "tin roof"
# stock4 = "cookie dough"

# ice_cream = input("please enter your favourite ice cream flavour: ").lower().strip()
# if ice_cream == stock1:
#     print(f"Yes, {stock1} is in stock")
# elif ice_cream == stock2:
#     print(f"Yes, {stock2} is in stock")
# elif ice_cream == stock3:
#     print(f"Yes, {stock3} is in stock")
# elif ice_cream == stock4:
#     print(f"Yes, {stock4} is in stock")
# else:
#     print(f"No, {ice_cream} in stock")

stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "tin roof"
stock4 = "cookie dough"

ice_cream = input("Please enter your fav 🍧?: ").lower().strip()
if (
    ice_cream == stock1
    or ice_cream == stock2
    or ice_cream == stock3
    or ice_cream == stock4
):
    print(f"Yes, {ice_cream} is in stock")
else:
    print(f"No, {ice_cream} is not in stock")


ice_cream = input("Please enter your fav 🍧?: ").lower().strip()
if ice_cream in [stock1, stock2, stock3, stock4]:
    print(f"Yes, {ice_cream} is in stock")
else:
    print(f"No, {ice_cream} in stock")
