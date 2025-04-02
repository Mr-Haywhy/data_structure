#......................Peek the Element.........................#
# The pop() method removes the top element (last element) from the stack.
# However, sometimes, we may simply need to peek or examine the top element without removing it.
# We can achieve this by accessing the element at the -1 index.

        # stack = []

        # # add items
        # stack.append(10)
        # stack.append(20)
        # stack.append(30)

        # # get stack's top element (last item of the list)
        # print(stack[-1])   # 30
# 
#.....................Source Code: Complete stack implementation..........................#
# create class to represent stack
class Stack:
    def __init__(self):
        self.stack = []

    # return True if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def print_stack(self, message):
        print(f"{message}: {self.stack}")

stack1 = Stack()

# add items to stack
stack1.push(5)
stack1.push(100)
stack1.push(1000)

# print stack
stack1.print_stack("Initial stack")

# peek the stack
print(f"Peek the stack: {stack1.peek()}")

stack1.print_stack("Stack after peeking")

# pop the stack
print(f"Removing an item: {stack1.pop()}")

stack1.print_stack("After removing the item")