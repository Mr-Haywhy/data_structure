#...................Stack operations......................#
# Now that we know what a stack is, let's perform a few more functionalities to our stack.
    # 1. is_empty - Check if the stack is empty or not.
    # 2. peek - Return the element on the top of the stack without deleting it.

# ...............Check if stack is empty.................#
# If we try to pop an element from an empty stack, we will get an error. This error is called stack underflow.
# Therefore, it's important to check if a stack is empty before popping elements.
# To determine if a stack is empty, we can simply find its length. If the length is 0, we know that the stack is empty.

        # # return True if stack is empty
        # # return False if stack is not empty
        # def is_empty(self):
        #     return len(self.stack) == 0


#...................Source Code....................#

class Stack:
    def __init__(self):
        self.stack = []

    # check and return True if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
        
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        # pop if the stack is not empty

        if not self.is_empty():
            return self.stack.pop()


    def print_stack(self, message):
        print(f"{message}: {self.stack}")

stack1 = Stack()

# add items to stack
stack1.push(5)
stack1.push(100)

# print stack
stack1.print_stack("Stack after pushing 2 items")

# pop 100
stack1.pop()

# print stack
stack1.print_stack("After first popping")

# pop 5
stack1.pop()

stack1.print_stack("After second popping")

# doesn't execute because the stack is empty
stack1.pop()

stack1.print_stack("After third popping")