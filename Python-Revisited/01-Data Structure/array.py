# Array is statically typed, we have to specify the typecode i.e, type of elements in array
# For typecode : https://docs.python.org/3/library/array.html

# Use array only if you are dealing with large sequence of numbers / when you encounters performance problems, otherwise use list and tuple by default

from array import array

numbers = array("i", [1, 2, 3, 4, 5])

numbers.append(99)
numbers.insert(1, 500)

numbers[0] = 10
# numbers[3] = 26.7     # This will give an error : only integer argument is allowed. Array is statically typed
print(numbers)
