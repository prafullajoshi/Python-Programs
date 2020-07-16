# Sets : Unordered collection of unique items
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 1]
first = set(numbers)
# print(uniques)
second = {1, 4, 7, 3, 8}
# second.add(5)
# second.remove(4)
# print(second)

print(first | second)  # Union of sets
print(first & second)  # Intersection of sets
print(first - second)  # Difference between two sets
# Symmetric Difference between two sets : Items either from first or from second but not from both
print(first ^ second)


# Due to unordered collection, we cannot access them with index
# print(first[0])     # This will give an error

if 1 in second:
    print("Yes")

numbers = [1, 2, 3, 2, 4, 3]
# numbers.add(100)
print(set(numbers))

# Hackerrank problem : Set Mutations
# (_, A) = (int(input()),set(map(int, input().split())))
# B = int(input())
# for _ in range(B):
#     (command, newSet) = (input().split()[0],set(map(int, input().split())))
#     getattr(A, command)(newSet)
# print (sum(A))

