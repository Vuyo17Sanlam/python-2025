percent = int(input("Please provide a number: "))
loader = "=" * (percent // 10)
space = " " * (10 - (percent // 10))
print(f"[{loader}{space}] {percent}%")
