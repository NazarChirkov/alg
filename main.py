#==============Algorithm:=================
#================Stack====================
#Creating a stack
def create_stack():
    stack = []
    return stack
#Checking if stack is empty
def check_empty(stack):
    return len(stack) == 0
#Adding item into the stack
def push(stack,item):
    stack.append(item)
    print("Push value: " + item)
#Removing an item from the stack
def pop(stack):
    if(check_empty(stack)):
        return ("Stack is empty")
    return stack.pop()
#==============Implomenting=============
stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))
#===============Queue=====================
# Queue implementation in Python

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()