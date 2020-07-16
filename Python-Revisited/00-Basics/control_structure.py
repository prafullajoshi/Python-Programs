temperature = 15

# if temperature > 30:
#     print("It's warm")
#     print("Drink Water")
# elif temperature > 20:
#     print("It's nice")
# else:
# print("It's cold")
# print("Done")

# Ternary Operators
# age = 22
# if age >= 18:
#     # print("Eligible")
#     message = "Eligible"
# else:
#     # print("Not eligible")
#     message = "Not Eligible"
# print(message)

# message = "Eligible" if age >= 18 else "Not Eligible"       # Ternary Operators
# print(message)

# Logical Operators
# high_income = False
# good_credit = True
# student = True

# # and operator
# if high_income and good_credit:
#     # print("Eligible")
# else:
#     # print("Not Eligible")

#     # or operator
# if high_income or good_credit:
#     # print("Eligible")
# else:
#     # print("Not Eligible")

#     # not operator : example 1
# if not student:
#     # print("Eligible")
# else:
#     # print("Not Eligible")

#     # not operator : example 2
# if (high_income or good_credit) and not student:
#     # print("Eligible")
# else:
# print("Not Eligible")

# Chaining comparision operators
# age should be between 18 and 65
# age = 22

# if 18 <= age < 65:              # equivalent to  - if age >= 18 and age < 65:
#     print("Eligible")

# for loop

# for number in range(1, 10, 2):
# print("Attempt", number, (number) * ".")

# for...else loop
# successful = True
# for number in range(3):
#     print("Attemt")
#     if successful:
#         print("Successful")
#         break
# else:
#     #This is executed only when the loop completely executes without terminate
#     print("Attempted 3 times")

# Nested Loop
# for x in range(5):
#     for y in range(3):
# print(f"({x}, {y})")

# while loop
# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# Infinite Loop
# while True:
# command = input(">")
# print("ECHO", command)
# if command.lower() == "quit":
#     break
count = 0
for x in range(1, 10):
    if x & 1:
        continue
    count += 1
    print(x)
print(f"We have {count} even numbers")
