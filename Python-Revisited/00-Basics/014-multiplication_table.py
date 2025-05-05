# Write a program to print the multiplication table of the number provided by the user

num = int(input("Display the multiplication table of :"))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
