numbers = [1, 2, 3]
print(numbers)  # This will print as [1,2,3]
# What if you want to print individual numbers without square brackets, unpacking operator is used

print(*numbers)  # unpacking operator

values = [*range(5), *"HELLO"]

print(*values)  # unpacking operator

# We can combine two lists with unpacking operator
first = [1, 2]
second = [3, 4]

values = [*first, "a", *second, "WELCOME"]
values = [*first, *second]
print(*values)  # unpacking operator


# We can use unpacking operator to combine dictionaries with **

first = {"x": 1}
second = {"x": 10, "y": 3}

combined = {**first, **second, "z": 1}
print(combined)
