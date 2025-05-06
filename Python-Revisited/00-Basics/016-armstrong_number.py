# Write a program to check if the number is armstrong number or not.

"""
It is a number that is equal to the sum of its own digits, each raised to a power equal to the
number of digits in the number.
    For example, let's consider the number 153:
    It has three digits (1, 5, and 3).
    If we calculate 1^3 + 5^3 3^3, we get 1 + 125 + 27 which is equal to 153
So, 153 is an Armstrong number because it equals the sum of its digits raised to the power
of the number of digits in the number.
"""

num = int(input("Enter the number :"))
num_str = str(num)
number_of_digits = len(num_str)
sum_of_powers = 0
temp_num = num


while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** number_of_digits
    temp_num = temp_num // 10

print(f"Number :{num}")
print(f"Sum :{sum_of_powers}")

if num == sum_of_powers:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is NOT an armstrong number")




