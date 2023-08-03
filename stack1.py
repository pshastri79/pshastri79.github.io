from collections import deque

myStack = deque()
myStack.append(10)
myStack.append(9)
myStack.append(8)


print(myStack.pop())
print(myStack.pop())
print(myStack.pop())


myStack.append(11)

print(len(myStack))