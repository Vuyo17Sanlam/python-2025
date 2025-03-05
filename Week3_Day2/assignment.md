# ✨ Comparison of `global` vs `nonlocal` in Terms of Scope

In Python, `global` and `nonlocal` are keywords used to modify variable scope in different ways. Understanding their scope is crucial when working with nested functions and modules.

---

## 🔹 1. `global` Keyword

The `global` keyword is used to refer to a variable that exists at the global (module) level. It allows modification of a global variable inside a function.

### 🏷️ Scope of `global`

- 🌍 `global` variables exist in the outermost scope (module-level scope).
- ✅ Using `global` inside a function allows the function to modify a variable defined outside its local scope.

### 💡 Example of `global`

```python
x = 10  # Global variable

def modify_global():
    global x  # Declaring x as global
    x = 20  # Modifying the global variable

modify_global()
print(x)  # Output: 20 (Global variable modified)
```

❌ Without `global`, `x` inside `modify_global` would be treated as a local variable, and modifying it would raise an error if it wasn't defined within the function.

---

## 🔹 2. `nonlocal` Keyword

The `nonlocal` keyword is used to modify variables in an enclosing (but not global) scope. It is particularly useful for working with nested functions.

### 🏷️ Scope of `nonlocal`

- 🔄 `nonlocal` is used inside a nested function to refer to a variable from the enclosing function’s scope.
- ❌ It does not modify global variables, only variables from an outer (non-global) function.

### 💡 Example of `nonlocal`

```python
def outer():
    y = 5  # Enclosing function variable

    def inner():
        nonlocal y  # Declaring y as nonlocal
        y = 15  # Modifying the enclosing function's variable

    inner()
    print(y)  # Output: 15 (Modified by inner function)

outer()
```

❌ Without `nonlocal`, `y` inside `inner` would be considered a local variable, and modifying it would not affect the `y` defined in `outer`.

---

## 🔥 Key Differences

| 🔹 Feature        | 🌍 `global`                          | 🔄 `nonlocal`                                          |
| ----------------- | ------------------------------------ | ------------------------------------------------------ |
| 🔎 Scope Affected | Global (module-level)                | Enclosing (non-global) function scope                  |
| 🛠️ Use Case       | Modify variables at the global level | Modify variables in an outer (but non-global) function |
| 🚀 Works Inside   | Any function                         | Only in nested functions                               |
| 💡 Example        | Modifying a global counter           | Updating a variable in a closure                       |

---

## 🎯 Conclusion

✅ Use `global` when you need to modify a variable at the module level inside a function.
✅ Use `nonlocal` when you need to modify a variable in an enclosing function (not global).
⚠️ Both should be used carefully to avoid unintended side effects and maintain code readability.

---
