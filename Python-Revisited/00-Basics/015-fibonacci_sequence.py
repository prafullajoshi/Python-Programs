# Write a program to print the fibonacci sequence


n_terms = int(input("How many terms :"))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid

if n_terms <= 0:
    print("Please enter positive integer")
# if there is only one term, then return n1
elif n_terms == 1:
    print(f"Fibonacci sequence upto {n_terms} :")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence :")
    while count < n_terms:
        print(n1)
        nth = n1 + n2
#       update the values
        n1 = n2
        n2 = nth
        count += 1
