# Write a program to find the factorial of the number

num = int(input("Enter the number :"))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print(f"Factorial of the {num} is always 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i

    print(f"Factorial of {num} is {factorial}")
