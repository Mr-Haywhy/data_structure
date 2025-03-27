#............Find the Smallest Value in a Linked List...............#

# Can you write a program to print the smallest value in a linked list?
    # Add the find_smallest() method to the LinkedList class, using the outline provided in the editor.
    # The method should return the smallest value in the linked list.
    # Then print the smallest value.




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        node1 = Node(80)
        self.head = node1

        node2 = Node(9)
        node1.next = node2

        node3 = Node(14)
        node2.next = node3

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
    
    # method to return the smallest number 
    def find_smallest(self):
        # write your code here
        if not self.head:
            return None
        current = self.head

        smallest = current.data

        while current:
            if current.data < smallest:
                smallest = current.data
            current = current.next
        return smallest
 