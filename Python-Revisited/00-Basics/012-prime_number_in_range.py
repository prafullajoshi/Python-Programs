# Write a program to print prime numbers in range

lower = int(input("Enter lower bound :"))
upper = int(input("Enter upper bound :"))

print(f"Prime numbers between {lower} and {upper} is :")

for num in range(lower, upper):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
