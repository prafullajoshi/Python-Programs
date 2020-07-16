from sys import getsizeof

# When comprehension is used with tuple, generator object is created and we have to iterate over it

# Generator : it doesn't loads all the values in memory
values = (x*2 for x in range(100000))
print("gen :", getsizeof(values))

values = [x*2 for x in range(100000)]       # It loads all the values in memory
print("list :", getsizeof(values))
