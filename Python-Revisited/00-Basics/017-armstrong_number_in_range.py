# Write a program to print armstrong number in range

lower = int(input("Enter lower bound :"))
upper = int(input("Enter upper bound :"))

for num in range(lower, upper + 1):
    number_of_digits = len(str(num))
    sum_of_power = 0
    temp_num = num
    while temp_num > 0:
        digit = temp_num % 10
        sum_of_power += digit ** number_of_digits
        temp_num = temp_num // 10
    if num == sum_of_power:
        print(num)
