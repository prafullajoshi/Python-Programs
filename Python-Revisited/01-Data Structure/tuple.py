# Tuple is immutable i.e., we cannot modify them

# point = (1, 2)
# point = 1,
# point = (1, 2) + (2, 4)
# point = (1, 2) * 3
point = tuple([1, 2, 3, 4])


print(type(point))
print(point)
print(point[0:3])

if 3 in point:
    print("exists")

# Tuple unpacking

x, y, z, w = point
print(x, y, z, w)

x, *other = point
print(x, other)

# Immutability : We cannot modify or change it

# point[0] = 10       # This will give an error
