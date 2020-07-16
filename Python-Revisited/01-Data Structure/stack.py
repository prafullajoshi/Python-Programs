# Stack : LIFO

browsing_session = []
# Pushing element onto stack
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
browsing_session.append(4)
# Displaying stack
print(browsing_session)
# Popping element from top of stack
last = browsing_session.pop()
print("Popped element :", last)
print(browsing_session)

# Return top of stack
if browsing_session:
    print("redirect :", browsing_session[-1])

# Checking if the stack is empty
if not browsing_session:
    print("disable")
