# Queue : FIFO

from collections import deque

queue = deque([])

# Adding an item to the list
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# Removing first item from queue
queue.popleft()         # We do not have this function on list
print(queue)

if not queue:
    print("Empty")
