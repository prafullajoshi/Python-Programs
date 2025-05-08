# Write a program to calculate the LCM of two input numbers:
"""
    LCM, or Least Common Multiple, is the smalest multiple that is exactly divisible by two or
    more numbers.
"""

num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number :"))

if num1 > num2:
    greater = num1
else:
    greater = num2

while(True):
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break
    greater += 1

print(f"LCM of {num1} and {num1} is :{lcm}")
