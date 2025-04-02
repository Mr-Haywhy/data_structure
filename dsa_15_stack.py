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