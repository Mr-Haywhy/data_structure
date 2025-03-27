#................CONCATENATE.TWO.LINKED.LISTS..................#
# If we append one linked list to the end of another linked list, it's called concatenation.

# To concatenate two linked lists, we can follow these two steps:
# 1. Traverse until we reach the last node of the first linked list.
        # current = list1.head
        ## traverse the linked list
        # while current.next:
            # current = current.next

# 2. Link the last node of the first linked list to the first node of the second linked list.
        # current.next = list2.head



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
   
    # method to concatenate two linked lists
    # self is the first linked list
    # list2 is the second list 
    def concatenate(self, list2):

        # handle if the first linked list is empty
        if not self.head:
            self.head = list2.head
            return
        
        current = self.head
        
        # traverse the linked list
        while current.next:
            current = current.next

        # link the last node of list1 to the first node of list2
        current.next = list2.head