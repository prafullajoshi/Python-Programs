
# point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point)

point["x"] = 10
point["z"] = 20
print(point)

# Check for key existance
if "a" in point:
    print(point["a"])

print(point.get("a", 0))

# delete key-value pair
del point["x"]
print(point)


# Looping over dictionary
# mothod - 1
for key in point:
    print(key, point[key])

# method - 2
for x in point.items():         # This will give tuple
    print(x)

# method - 3
for key, value in point.items():
    print(key, value)


# Dictionary Comprehension
values = {}

for x in range(5):
    values[x] = x * 2

# Above code can be rewritten using dictionary comprehension

values = {x: x * 2 for x in range(5)}
print(values)
