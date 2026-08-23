stack = []

def push(item):
    stack.append(item)

def pop():
    return stack.pop()

def peek():
    return stack[-1]

def is_empty():
    return len(stack) == 0

def display():
    print(stack)

push(10)
push(20)
push(30)
push(40)
push(50)

print("Top element =", peek())

pop()
pop()

display()