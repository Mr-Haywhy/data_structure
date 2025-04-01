# Delete First Node
# Deleting the first node is a special case since it is the head node. And the only way to access the linked list is through the head node
# NOTE: While you can access a doubly linked list from the tail node as well, you can't perform a forward traversal without specifying the head node.
# 
# Suppose we have the following linked list.
        # 10<=>80<=>9<=>11<=>14
# 
# We can follow the simple steps below to delete the first node from the linked list.
# 
# 1. Shift the 'head' node and break the link.
    # We first make the second node the new head node. Then, we make the prev pointer of the new head node point to None.
# 2. Make the 'next' pointer of the first node point to 'None'.
# 
# 
#..............Code: Delete From the Beginning.................#
# So, our helper method to delete a node from the beginning will look like this:

        # # delete from beginning
        # def delete_from_beginning(self):
        #     # get reference to the head node
        #     current = self.head
        #     # shift head
        #     self.head = self.head.next
        #     # update prev of head
        #     self.head.prev = None
        #     # update the next of current 
        #     current.next = None
# 
# 
#.................Delete From a Doubly Linked List with a Single Element................#
# To delete from a doubly linked list with a single element, we simply set both head and tail to None.

        # # delete a linked list with a single element
        # def delete_single_element(self):
        #     self.head = None
        #     self.tail = None
# 
# 
#..................Delete a Node From the End...................#
# Let's delete a value from the end of a linked list; we can perform the same operation as the deletion at the beginning.

# Suppose we have the following linked list.
                # 10<=>80<=>9<=>11<=>14
# 
# 1. Shift the 'tail' node to the second-last element.
# 2. Update the 'next' pointer of the new 'tail' to 'None'.
# 3. Update the 'prev' pointer of the last node to 'None'.
# 

#.............Code: Delete a Node from the End.................#
            # # delete from end
            # def delete_from_end(self):
            #     # get reference to the tail node
            #     current = self.tail
            #     # shift tail
            #     self.tail = self.tail.prev
            #     # update next of tail
            #     self.tail.next = None
            #     # set the previous of current to None
            #     current.prev = None

# 
#.................Delete a Node from given position...............#
# Suppose we have the following linked list:
            # 10<=>80<=>9<=>11<=>14
# To delete the node at the fourth position, i.e., 11, we follow the given steps:

# 1. Get reference to the nodes before and after the given position.
# 2. Update the references.
# To update the references, we:
    # Set the next of the third node to point to the fifth node.
    # Set the prev of the fifth node to point to the third node.
# 3. Make the 'prev' and 'next' pointers of the fourth node point to 'None.'

# 
#.............Code: Delete from a given position.................#
# delete from given position 
        # def delete_from_position(self, position):
        #     # get reference to the nodes
        #     # before and after the given position
        #     current = self.head
        #     prev_node = next_node = None
        #     for i in range(position-1):
        #         current = current.next
        #     prev_node = current.prev
        #     next_node = current.next

        #     # update pointers
        #     prev_node.next = next_node
        #     next_node.prev = prev_node

        #     # delete node
        #     current.next = None
        #     current.prev = None
# 


#.....................Source Code: Deleting node........................#
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # create doubly linked list
    def create_linked_list(self):
        # add first node
        node1 = Node(80)
        # both head and tail is the first node
        self.head = node1
        self.tail = node1

        # add second node
        node2 = Node(9)
        # update the pointers
        node1.next = node2
        node2.prev = node1
        # node2 becomes the new tail
        self.tail = node2

        # add third node
        node3 = Node(14)
        # update the pointers
        node2.next = node3
        node3.prev = node2
        # node3 becomes the new tail
        self.tail = node3
    
    #  traverse the linked list
    def traverse(self):
        # start at head
        current = self.head
        print("None", end = " <-> ")
        # loop until the node is None
        while current is not None:
            print(f"{current.data} <-> ", end="") 
            current = current.next
        print("None")
    
    # reverse traverse the linked list
    def reverse_traverse(self):
        # start at tail
        current = self.tail
        print("None", end = " <-> ")
        # loop until node is None
        while current is not None:
            print(f"{current.data} <-> ", end="") 
            current = current.prev
        print("None")
    
    # helper method to get the length of the list
    def length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    # delete from beginning
    def delete_from_beginning(self):
        # get reference to the head node
        current = self.head
        # shift head
        self.head = self.head.next
        # update prev of head
        self.head.prev = None
        # update the next of current 
        current.next = None
    
    # delete a linked list with a single element
    def delete_single_element(self):
        self.head = None
        self.tail = None
    
    # delete from end
    def delete_from_end(self):
            # get reference to the tail node
            current = self.tail
            # shift tail
            self.tail = self.tail.prev
            # update next of tail
            self.tail.next = None
            # set the previous of current to None
            current.prev = None
    
    # delete from given position 
    def delete_from_position(self, position):
        # get reference to the nodes
        # before and after the given position
        current = self.head
        prev_node = next_node = None
        for i in range(position-1):
            current = current.next
        prev_node = current.prev
        next_node = current.next
    
        # update pointers
        prev_node.next = next_node
        next_node.prev = prev_node
    
        # delete node
        current.next = None
        current.prev = None
    
    # universal delete method
    def delete_node(self, position=None):
        # check if the list is empty
        if self.head is None:
            print("The list is empty.")
            return
        
        # single element case
        if self.length() == 1:
            self.delete_single_element()
            return
    
        # first element case
        if position == 1:
            self.delete_from_beginning()
            return
        
        # last element case (or no position given)
        if position is None or position == self.length():
            self.delete_from_end()
            return
    
        # specific position case
        if 1 < position < self.length():
            self.delete_from_position(position)
            return
        else:
            print("Invalid position.")
            return


# initialize the doubly linked list
linked_list = DoublyLinkedList()

# populate the list
linked_list.create_linked_list()  

# display the list before deletion
print("Original List:")
linked_list.traverse()
print()

# delete the first node
print("Deleting the first node.")
linked_list.delete_node(position=1)
linked_list.traverse()
print()

# delete the last node
print("Deleting the last node.")
linked_list.delete_node() # no position specified
linked_list.traverse()
print()

# delete a node from a specific valid position 
print("Deleting a node from the 2nd position.")
linked_list.delete_node(position=2)
linked_list.traverse()
print()

# attempt to delete a node from an invalid position 
print("Attempting to delete a node from an invalid position (5th).")
linked_list.delete_node(position=5)
print()

# delete the only remaining node
print("Deleting the only remaining node.")
linked_list.delete_node()  
linked_list.traverse()