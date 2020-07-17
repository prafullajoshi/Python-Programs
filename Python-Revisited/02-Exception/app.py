numbers = [1, 2]
# print(numbers[3])

# try:
#     age = int(input("Age :"))
# except ValueError as ex:
#     print("You didn't enter valid age")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exception thrown.")
# print("Execution continues...")

# Multiple exception
# try:
#     age = int(input("Age :"))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) as ex:
#     print("You didn't enter valid age")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exception thrown.")
# print("Execution continues...")


# finally :

# try:
#     file = open("app.py")
#     age = int(input("Age :"))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) as ex:
#     print("You didn't enter valid age")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exception thrown.")
# finally:
#     file.close()  # Release the resources
#     print("File closed")
# print("Execution continues...")


# 'with' statement

# try:
#     with open("app.py") as file:
#         print("file opened")
#     age = int(input("Age :"))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) as ex:
#     print("You didn't enter valid age")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exception thrown.")
# print("Execution continues...")

# raising exception
def cal_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    cal_xfactor(-1)
except ValueError as error:
    print(error)
