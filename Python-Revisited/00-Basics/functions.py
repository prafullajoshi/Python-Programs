def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Prafulla", "Joshi")
greet("John", "Micey")

# In Python, all function by default 'None' by default unless specified

# Function can be of two types
# 1 - Perform a task
# 2 - Return a value
# Let's convert the above function into 2nd type


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Prafulla")
file = open("content.txt", "w")
file.write(message)


# Keyword Argument
def increment(number, by):
    return number + by


print(increment(number=3, by=1))  # Keyword argument

# Default Arguments


def increment(number, by=5):
    return number + by


print(increment(2, 7))


# Variable number of arguments - xargs
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")
print(multiply(2, 3, 4, 5, 6))


# xxargs - multiple keyword args; python will convert them into dictionary

def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name="Prafulla", age=26)


# Exercise

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return input


print(fizz_buzz(15))
