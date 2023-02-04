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