# Write a program to calculate the GCD of two input numbers:
"""
    GCD, or Greatest Common Divisor, is the largest positive integer that divides two or more
numbers without leaving a remainder.
"""

num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number :"))

if num1 < num2:
    smaller = num1
else:
    smaller = num2

for i in range(1, smaller + 1):
    if (num1 % i) == 0 and (num2 % i) == 0:
        gcd = i

print(f"GCD of {num1} and {num1} is :{gcd}")

