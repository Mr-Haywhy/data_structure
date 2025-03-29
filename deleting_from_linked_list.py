#................Delete From the linked list....................#
# We can delete a node at any position in a circular linked list. There are two cases for node deletion:
    # Delete the first node.
    # Delete a node at a given position
#..............delete the first node..................#
# Deleting the first node in a linked list is a special case. This is because the first node is the head node of the linked list. And the only way to access the linked list is through the head node

# Suppose we have a linked list like:
        # (8, 3, 9, 7, 6)

# To delete the first node (i.e., 8) from this linked list, we perform the following steps:

# 1. Get reference to the head node.
        # temp = self.head
# 
# 2. Get reference to the last node.
        # current = self.head
        # while current.next is not self.head:
        #     current = current.next
#  
# 3. Move the head to the second node.
        # self.head = self.head.next
# 
# 4. Make the last node point to the new head node.
        # current.next = self.head

#..............Code to delete first node..................#
        # def delete_from_beginning(self):
        #     # get a reference to head
        #     temp = self.head
        #     current = self.head

        #     # get a reference to the last node
        #     while current.next is not self.head:
        #         current = current.next

        #     # shift head to second node    
        #     self.head = self.head.next

        #     # adjust the next pointer of the last node to the new head
        #     current.next = self.head
# 


#................Delete from a circular linked list with a single node..................#
# 
# Let's implement our previous deletion algorithm to a circular linked list that only has a single node.
# 
# 1. Get reference to the head node.
        # temp = self.head
# 
# 2. Get reference to the last node.
        # current = self.head
        # while current.next is not self.head:
        #     current = current.next
# 
# 3. Move the head node to the second node.
        # self.head = self.head.next
# 
# 4. Make the last node point to the new head node.
        # current.next = self.head
# 
# This approach doesn't work when our linked list has only one element.
#.............
# To handle the scenario of deleting from a circular linked list with a single node, we can implement the following code:

#.............helper to delete the only node of the linked list..............#
        # def delete(self):
        #     temp = self.head
        #     self.head = None
# 
# We know, in an empty circular linked list, the head is None. So, when deleting the node, we can simply assign the head to None and avoid all computations.

#.....................Delete a node at a given position..................#
#
# Let's delete a value from a given position in a linked list.
# Suppose we have the following linked list:
        # (8, 3, 9, 7, 6)
# 
# To delete a node at the given position (say, the 4th position) in a linked list, we have to follow the steps below:
# 
# 1. Move to the third node and make it point to the fifth node.
# 2. Delete the fourth node.
# 
#...................Thought Process of deleting at a given position...................#
# 
# Let's learn how to delete nodes at a given position programmatically.
# For that, we will take two references:
    # The first to point to the 4th node.
    # The second to point to the node before that (3rd node).
# 
# We will follow the following steps to delete a node in a linked list:
# 
# 1. Take two references: let one reference point to the head of the list, and the other reference point to None.
        # current = self.head
        # prev_node = None
# 
# 2. Move the pointers till we have one reference at the 4th node and another pointer at the 3rd node.
        # for i in range(1, position):
        #     prev_node = current
        #     current = current.next
# 
# 3. Link the third node to the fifth node.
        # prev_node.next = current.next
# 
# 
#.............Code to delete from given position...............#
# 
        # def delete_at_position(self, position):
        #.....# take two pointers
        #     current = self.head
        #     prev_node = None

        #.....# move pointers until we reach our desired node
        #     for i in range(1, position):
        #         prev_node = current
        #         current = current.next

        #.....# point the previous node to the current.next node
        #     prev_node.next = current.next
# 
# 

#..............Source Code: Delete Nodes from a linked list.............#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        node1 = Node(80)
        self.head = node1

        node2 = Node(9)
        node1.next = node2

        node3 = Node(14)
        node2.next = node3

        node3.next = self.head
    
    # helper to traverse the list 
    # and display the elements
    def display(self):
        nodes = []
        if self.head is None:
            return "Empty Linked List"
        current = self.head
        while current.next is not self.head:
            nodes.append(str(current.data))
            current = current.next
        nodes.append(str(current.data))
        return " -> ".join(nodes) + f" -> {self.head.data} "
    
    # helper to delete from beginning
    def delete_from_beginning(self):
        # get a reference to head
        temp = self.head
        current = self.head
        # get a reference to the last node
        while current.next is not self.head:
            current = current.next
        # shift head to second node    
        self.head = self.head.next
        # adjust the next pointer of the
        # last node to the new head
        current.next = self.head

    # helper to delete the only node of the linked list
    def delete_only_node(self):
        temp = self.head
        self.head = None
    
    # delete at any given position
    def delete_at_position(self, position):
        # take two pointers
        current = self.head
        prev_node = None
        # move pointers until we reach our desired node
        for i in range(1, position):
            prev_node = current
            current = current.next
        # point the previous node to the current.next node
        prev_node.next = current.next
    
    def delete_nodes(self, position):
        # step 1: Check if the list is empty
        if self.head is None:
            return "Error: The list is empty."

        # step 2: If position is 1, check if it's the only node
        if position == 1:
            if self.head.next == self.head:  # Only one node in the list
                self.delete_only_node()
            else:
                self.delete_from_beginning()
        else:
            # step 3: For positions other than 1, use delete_at_position
            # but first, ensure the position is not out of bounds
            temp = self.head
            count = 1
            while temp.next != self.head:
                count += 1
                temp = temp.next
            
            if position > count:
                return "Error: Position is out of bounds."

            self.delete_at_position(position)

# 
# 
# In the above program, we implemented all the helper methods we have learned so far to delete a node.
# Then, we incorporated these helper methods into a single method named delete_nodes() to handle all cases of deletion.