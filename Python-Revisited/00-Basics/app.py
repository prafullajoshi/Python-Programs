# print("Hello World ")
import math
2 + 3
# print("* " * 10)
a = 10
unit_price = 12
unit_price_symbol = 12
x = 1

# course = "Python Programming"
course = "www.google.com"
# print(len(course))
# print(course[0])
# print(course[-1])
# print(course[0:3])
# print(course[0:])
# print(course[:3])
# print(course[::-1])
# print(course[4:-4])

# Exscape Sequences
# \"
# \'
# \\
# \n
course_name = "Programming\" is fun"
# print(course_name)

# Format Strings
first = "Prafulla"
last = "Joshi"
full = first + " " + last
# print(full)

full = f"{first} {last}"
# print(full)

# String Methods
#

name = "    prafulla joshi"
# Methods return new modified string, original string is not affected
name.upper()
print(name.upper())
print(name)
print(name.lower())
print(name.title())
print(name.strip())
print(name.find("jo"))
print(name.replace("jo", "po"))
print("lla " in name)
print("M" not in name)

# Numbers
print("Number Operations ::")
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)      # Floored division, only integer is returned
print(10 % 3)
print(10 ** 3)

# Functions on Numbers

print("Various functions on numbers ::")
print(round(2.9))
print(abs(-2.91))
print(math.ceil(2.2))

# Type conversion

print("Type Conversion ::")

# x = input("x :")  # when we receive input from user, it always comes as a string
x = 10
print(type(x))
y = int(x) + 1
print(f"x : {x}, y : {y}")

# Falsy values :
# ""
# 0
# None

# Above values are considered as False in Python. Anything else is True
print("Falsy Values in Python ::")
print(f"bool(0) :: {bool(0)}")
print(f"bool(5) :: {bool(5)}")
print(f"bool(-5) :: {bool(-5)}")
print(f"bool(\"\") :: {bool('')}")
print(f"bool(\"Anything\") :: {bool('Anything')}")
print(f"bool(\"False\") :: {bool('False')}")
print(f"bool(None) :: {bool(None)}")
