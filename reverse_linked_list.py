#...................REVERSE.LINKED.LIST......................#

# In the previous example, we reversed the elements of the linked list. Here, we are reversing the linked list itself. 
# Meaning we are making the last element the new head. The data of the linked list will remain the same. However, they will point to its preceding node, instead of pointing to their succeeding node.
# To solve this, we can use the sliding references technique.

#...........Understanding Sliding References............#
# Before we dive into reversing the linked list, let's grasp the concept of sliding references.
# Sliding references refer to a technique where multiple references move together, allowing us to traverse and manipulate linked list nodes efficiently.
# In our example, we'll use three references: prev_node, current, and next_node. Initially, these references will be positioned as follows:

# 1. Start by setting three references.

        # previous = None
        # current = self.head
        # next_node = current.next

# 2. Move to the succeeding nodes.

        # prev_node = current
        # current = next_node
        # next_node = next_node.next

# Since multiple references slide or move together in a coordinated manner; they are called sliding references.


#......To reverse a linked list, we will use the following steps.
# 1. Create three references.
        # prev_node = None
        # current = self.head
        # next_node = current.next

# 2. Make the current node point to its preceding node.
        # current.next = prev_node

# 3. Slide the references.

        # prev_node = current
        # current = next_node
        # next_node = next_node.next

# 4. Repeat Steps 2 and 3 until the subsequent node of the current node points to None.
        # while True:
        #     # Step 2 and 3

        # if next_node == None:
        #     current.next = prev_node
        #     break

# 5. Make the current node the new head node.
        # self.head = current



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # helper method to append a node at the end
    def append_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # helper method to insert a node at the beginning
    def insert_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # helper method to insert a node at a specific position
    def insert_node_at_position(self, data, position):
        
        new_node = Node(data)
        current = self.head
        
        for i in range(1, position -1 ):
            current = current.next 
        
        new_node.next = current.next
        current.next = new_node

    # universal insert method
    def insert_node(self, data, position=None):
        # if no position is given
        # or position exceeds the length of the list
        # insert at the end
        if position is None or position >= self.get_length():
            self.append_node(data)
        elif position == 0:
            self.insert_node_at_beginning(data)
        else:
            self.insert_node_at_position(data, position)
        

    # helper method to get the length of the linked list
    def get_length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    # traverse the list
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)
   

   # reverse linked list
    def reverse_linked_list(self):

        prev_node = None
        current = self.head
        next_node = current.next

        while True:

            current.next = prev_node
                    
            prev_node = current
            current = next_node
            next_node = next_node.next
                    
            if next_node == None:
                current.next = prev_node
                break

        self.head = current   