## Day 4 notes

> **Refactoring:** Is the process of improving code quality but not changing the code functionality
>
> - e.g Raptor engines 1,2, 3
>
> ![alt text](image-2.png)

## control flow

- Decision Tree
  'if_else'
  'if_elif_else'
  Loops

1. while
2. for

Purpose: simply repeating statements

```py
print("vote for Jevani")
print("vote for Jevani")
print("vote for Jevani")
```

### while

![alt text](image-3.png)

```py
# print("Vote for Jevan 🎊")
# print("Vote for Jevan 🎊")
# print("Vote for Jevan 🎊")


# Refactor in while loop

# i = 1

# while i <= 3:
#     print("Vote for Jevan 🎊")
#     i = i + 1

# print("Voting Ended 🎊")


# Refactor in for loop
# for and range (pair)

# range always starts with 0
# range excludes the end

# range(start, end, step)
# range(3) -> range(end)
# for i in range(3):
#     print(i)


# range(start, end) -> range(start, end)
# for and range takes care of incrementing `i`
for i in range(1, 11):
    print(i)
```

- repitition operator ("\*")

> ## Git
>
> - U means untracted
> - A means added
>   Commit message: should be why you did it.
