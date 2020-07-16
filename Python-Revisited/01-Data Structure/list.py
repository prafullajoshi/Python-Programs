letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 100
# print(zeros)

zeros = [0] * 5
combined = zeros + letters
print(combined)
print(len(combined))

numbers = list(range(20))
print(numbers)
print(len(numbers))

chars = list("Hello World")
print(chars)
print(len(chars))

# Accessing the item from list
letters = ["a", "b", "c", "d"]
numbers = list(range(20))
letters[0] = "A"
print(letters[0:3])
print(numbers[::2])
print(numbers[::-1])

# List unpacking
numbers = [1, 2, 3]
first, second, third = numbers  # Unpacking of list
# If we want to get only first two items in a big list then that is done with following :
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *other, last = numbers
print(first)
print(other)

first = numbers[0]
second = numbers[1]
third = numbers[2]

# Loop over list
letters = ["a", "b", "c", "d"]

for letter in letters:
    print(letter)

# Generate tuple with (0, "a") (1, "b") and so on
for letter in enumerate(letters):
    print(letter)

for index, letter in enumerate(letters):    # Tuple is unpacked
    print(index, letter)


letters = ["a", "b", "c"]
# Add
letters.append("d")     # element is added at the end
letters.insert(0, "--")  # element is added in between
print(letters)

# Remove
letters.pop()  # Removes the last item
letters.pop(0)  # Removes item at 0th index
letters.remove("b")  # this will remove the first occurance of letter 'b'
del letters[0:3]  # Removes range of items from the list
letters.clear()     # Removes all the objects from the list
print(letters)

letters = ["a", "b", "c", "d", "b", "t", "b"]
# Find
print(letters.index("b"))  # index of letter 'b'

# count the number of occurances of a letter in the list
print(letters.count("b"))

if "x" in letters:
    print(letters.index("x"))


# Sorting
numbers = [3, 52, 2, 8, 6]
# numbers.sort()          # Ascending order : Modifies the original list
# print(numbers)

# numbers.sort(reverse=True)      # Descending order : Modifies the original list
# print(numbers)

print(sorted(numbers))      # Ascending
print("Original List ", numbers)

print(sorted(numbers, reverse=True))      # Descending
print("Original List ", numbers)


# Sorting a complex object

items = [
    ("p2", 13, "D"),
    ("p4", 2, "A"),
    ("p1", 9, "C"),
    ("p3", 5, "B")
]


def sort_item(item):
    return item[2]


items.sort(key=sort_item)
print(items)


# Lambda Expression : One line anonymous function that we can pass to other function

items = [
    ("p2", 13, "D"),
    ("p4", 2, "A"),
    ("p1", 9, "C"),
    ("p3", 5, "B")
]


# Lambda Expression : Shorter way to define the function that we are going to use only once as an argument to another function
items.sort(key=lambda item: item[1])
print(items)

# map()
items = [
    ("p2", 13, "D"),
    ("p4", 2, "A"),
    ("p1", 9, "C"),
    ("p3", 5, "B")
]
# Suppose we have map above list to different list of prices, then we can use map()

prices = list(map(lambda item: item[1], items))
print(prices)


# filter()
items = [
    ("p2", 13, "D"),
    ("p4", 2, "A"),
    ("p1", 9, "C"),
    ("p3", 5, "B")
]
# Suppose we have map above list to different list of prices with greater than 7, then we can use filter()

filtered = []

for item in items:
    if item[1] > 7:
        filtered.append(item[1])

print(filtered)

filtered = list(filter(lambda item: item[1] > 7, items))
print(filtered)

# List Comprehension
# [expression for item in items]      # Syntax for List Comprehension
items = [
    ("p2", 13, "D"),
    ("p4", 2, "A"),
    ("p1", 9, "C"),
    ("p3", 5, "B")
]

prices = [item[1] for item in items]        # Same as line 135
print(prices)

filtered = [item for item in items if item[1] > 7]      # Same as line 156
print(filtered)


# zip()
list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 20, 30, 40, 50, 60]
# Suppose we want mapping of above lists as [(1,10), (2,20), (3, 30)], we can use zip()

print(list(zip(list1, list2)))

# we can also have string in zip function, that string will be separated in each tuple

print(list(zip("abcdef", list1, list2)))
