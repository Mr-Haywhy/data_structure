# Replace __ with your code

# create class to represent stack
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
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def print_stack(self, message):
        print(f"{message}: {self.stack}")

def reverse_string(text):
    # write your code here
    stack1 = Stack()
    reversed_string = ""

    for char in text: 
        stack1.push(char)
    
    while not stack1.is_empty():
        reversed_string += stack1.pop()
    return reversed_string

# add items to stack
text = input('hello')
print(reverse_string(text))