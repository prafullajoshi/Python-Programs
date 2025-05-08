# Write a program to check whether the number is prime or not
import sys

num = int(input("Enter the number :"))

flag = False

if num <= 1:
    print(f"{num} is not a prime number")
    sys.exit(0)
elif num == 2:
    print(f"{num} is a prime number")
    sys.exit(0)
else:
    for i in range(3, num, 2):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(f"{num} is NOT a prime number")
else:
    print(f"{num} is a prime number")
