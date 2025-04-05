# ..........................Introduction.........................
# Hash collisions are inevitable because we cannot predict the input that will be used for hashing.

# Therefore, it is more practical to manage collisions when they occur rather than try to avoid them entirely.

# Two of the most common strategies for collision resolution are:
#     Separate Chaining
#     Open Addressing
# Let's start with separate chaining.
# .................Separate Chaining.....................#
# Consider the hash function: H(x) = x mod 10 and the following keys 12, 17, 15, 4, 27, 14, and 37.
# Here, 4 and 14 keys have the same hash, and 37, 27, and 17 keys have the same hash, resulting in collisions.

# The separate chaining technique resolves these collisions by utilizing linked lists.

# In this technique, each slot is a linked list. If two keys have the same hash, both will be placed into the same cell as items of a linked list.
# Instead of simply rejecting a new key/value pair when a collision occurs, separate chaining allows multiple keys to exist in the same bucket slot.


#.................Thought process: chaining...................#
# In separate chaining, each slot of the hash table is a linked list.

# So, let's first create a linked list class to handle linked list operations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # return the linked list elements
    def traverse(self):
        current = self.head

        result = ""

        while current:
            result += (f"{current.data}->")
            current = current.next

        result += "None"
        return result
    
    # Append item into new node 
    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

data = [1, 4, 2, 9]

li = LinkedList()

# append the data to the linked list
for i in data:
    li.append(i)

# display the linked list

print(li.traverse())