# Write a program to print the ASCII value of the character

"""
    ASCII, or American Standard Code for Information Interchange, is a character encoding
    standard that uses numeric values to represent characters. Each ASCII character is
    assigned a unique 7-bit or 8-bit binary number, alowing computers to exchange information
    and display text in a consistent way.
"""

char = str(input("Enter a character :"))

print(f"The ASCII value of {char} is {ord(char)}")
