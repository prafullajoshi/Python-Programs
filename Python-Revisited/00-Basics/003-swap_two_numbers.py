# Write a program to swap two numbers

x = input("Enter the value for X :")
y = input("Enter the value for Y :")

print("Before swapping :")
print(f"X = {x}")
print(f"Y = {y}")

# Swapping with 3rd variable
temp = x
x = y
y = temp

# Swapping without 3rd variable

# x, y = y, x

print("After swapping :")
print(f"X = {x}")
print(f"Y = {y}")
