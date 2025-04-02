# Introduction
# A stack is a linear data structure that follows the last-in-first-out (LIFO) principle. 
# That means:
    # The last element added is the first to be removed from the stack.
    # The first element added is the last to be removed from the stack.
# In a stack, the last element added is the first to be removed.
# 
# To create a stack:
# 1. Create an empty stack.
# We will use a list to create an empty stack.
        # stack = []
# 2. Push elements to stack.
# We can use list's append() method to add elements at the end of the stack.
        ## add three elements to the stack
        # stack.append(5)
        # stack.append(10)
        # stack.append(100)
# 3. Remove elements from the last.
# We need to pop (remove) elements from the end of the stack. This is because stack works on the 'last-in-first-out' principle.
# We can use the list's pop() method to remove the last element from the list.
        ## remove the last element
        # item = stack.pop()

# ................create stack.....................#
# create class to represent stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def print_stack(self, message):
        print(f"{message}: {self.stack}")

# initialize the stack
stack1 = Stack()

# add items to stack
stack1.push(5)
stack1.push(10)
stack1.push(100)

# print stack
stack1.print_stack("Stack after pushing three items")

# remove an item
removed_item = stack1.pop()

stack1.print_stack("Stack after popping")
print(f"Removed item: {removed_item}")

# remove an item again
removed_item = stack1.pop()

stack1.print_stack("Stack after popping again")
print(f"Removed item: {removed_item}")


#..................Time Complexity.........................#
# In a stack, we only need to deal with the top element, regardless of the operation we perform or the size of the stack.
# Therefore, all stack operations take constant time.
        # Time Complexity: O(1)

# Let's explore stack a little more by converting an infix expression to a postfix. But before that, here's an exercise for you.