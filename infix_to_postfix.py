#.............................Infix Expressions.......................#
# Generally, we write expressions in the form of a * b + c.
# Here, we evaluate a * b first, then add c to the result.
# Similarly, let's take another expression: a + b * c.
# We perform multiplication first, then addition. Thus, b * c is evaluated first, then the result is added to a.
# These expressions are called infix expressions because the operator is placed between the operands.
# From the second example, we can see that the operators cannot be evaluated immediately. We have to check the precedence of the operators and evaluate them accordingly.
# Such a process is slow for computers (to check precedence and then evaluate infix expressions).
# Instead, computers use postfix expressions (operators after the operands) to evaluate these expressions.

#.......................Postfix Expression......................#
# Before we learn the conversion of infix to postfix expressions, let's take a look at how postfix works.
# The equivalent postfix expression for a * b + c is ab*c+.
# Here's how a computer processes this expression:
    # Start with an empty stack.
    # Scan a: push a onto the stack.
    # Scan b: push b onto the stack.
    # Scan *: pop a and b, calculate a*b, and push the result back onto the stack.
    # Scan c: push c onto the stack.
    # Scan +: pop c and the result of a*b, calculate their sum and push the result back onto the stack.
# 
# So instead of having to wait and check for precedence, in postfix expression, we can simply:
    # Push each operand to the stack.
    # Each operator pops the last two operands from the stack, evaluates them, and pushes the result back to the stack.
# Computers can perform computations much faster by utilizing a stack to process postfix expressions.
# 

#.....................Infix to Postfix Conversion Using Stack....................#
# Our goal is to convert expressions like a * b + c to ab*c+. Similarly, a + c * b should be converted to acb*+.
# The conversion requires a stack to keep track of the operators and a string to store the postfix expression.
# 
# In the case of operands, we simply append the operands to the postfix expression. However, operators follow the following steps:
    # If the stack is empty, add the operator to the stack.
    # If an operator with lower precedence tries to enter the stack, pop items until the operator at the top of the stack has lower or equal precedence.
    # All popped operators are appended to the postfix expression.
    # After the infix expression is done, pop all operators from the stack and append it to the postfix expression.

# NOTE: The stack can never have a higher precedence operator below the lower precedence operator.

# 
#......................Working of Infix to Postfix Conversion....................#
# Let's see with images how a*b+c is converted to a postfix expression.
# We start with an empty stack and an empty postfix expression.
    # 1. Append operand a to postfix.
    # 2. Push the operator * to the stack.
    # 3. Append operand b to postfix.
    # 4. Compare the operator + with the top of stack *. Since the precedence of * is higher than +, pop * from the stack and add it to postfix.
# Now, since the stack is empty, push the operator + to stack.
    # 5. Append the operator c to postfix.
    # 6. Since the infix expression is done, pop all remaining operators from the stack and append them to postfix.
# 


# NOTE: This program works for only * and + operators. We can easily change it to work for other operators as well.
class Stack:
    def __init__(self):
        self.stack = []

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

def infix_to_postfix(infix): 
    
    operators = {'+':1, '*':2} 

    stack = Stack()
    postfix = '' 

    for character in infix:

        # append operand to postfix
        if character not in operators:  
            postfix += character
            continue
        
        # if stack is empty, push operator to stack
        if stack.is_empty():
            stack.push(character)
            continue
        
        # if stack is not empty  and the operator has lower precedence than the top of the stack, 
        # pop from stack and append to postfix
        while not stack.is_empty() and operators[character] <= operators[stack.peek()]:
            postfix += stack.pop()
        # if the stack is empty or the precedence of operator is higher precedence
        # push the operator to stack
        stack.push(character)
    
    # pop all remaining operators from stack and append to postfix
    while not stack.is_empty():
        postfix += stack.pop()

    return postfix

infix = 'a*b+c'

print(f'infix notation: {infix}')
print(f'postfix notation: {infix_to_postfix(infix)}')

infix = 'a+b*c'

print(f'infix notation: {infix}')
print(f'postfix notation: {infix_to_postfix(infix)}')

infix = 'a+b*c*d+e'

print(f'infix notation: {infix}')
print(f'postfix notation: {infix_to_postfix(infix)}')