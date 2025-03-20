# LINKED LIST
# A linked list is a linear data structure that includes a series of connected elements. Each element of a linked list is called a node.
# A node stores data and the address of the next node.
# A linked list is a series of connected nodes.
    # The first node is the starting point of a linked list and is called the head of that linked list.
    # The address of the last node must point to None (null), as there are no elements after it.
# 
# ...............Real-Life Analogy.................#
# Imagine playing a game of Treasure Hunt, where you follow a trail of clues connecting one piece of information to the next until you finally reach the treasure.
# A linked list is analogous to this trail of connected clues. And each clue (node) has
    # a piece of information (data)
    # a hint to find the next clue (address of the next node)
# 
# 
#....................CREATING A LINKED LIST..................#
# Since a linked list is a collection of connected nodes, let's first learn to create nodes.
#...........Create a Node.............#
# As mentioned before, a node stores data and the address of the next node.
            # 
            # class Node:
                # def __init__(self, data):   
                #     self.data = data
                #     self.next = None
# NOTE: We have initialized the value of next to None because, currently, there are no nodes after it.
# 
# Now, we can create nodes and add data to them.
            # node1 = Node(11)
            # node2 = Node(2)
            # node3 = Node(88)
# 
# Next, we will create a linked list by connecting the nodes above
# 
# Let's create a LinkedList class to implement linked lists.
            # class LinkedList:
            #     def __init__(self):
            #         # initialize the head field to None
            #         self.head = None
# 
# Next, we will create a method to add nodes. For now, we will only add our first node to the linked list.
            # def create_linked_list(self):
            #     # create the first node
            #     node1 = Node(80)
            #     # set the head field to the first node
            #     self.head = node1
# 
# Let's create the second node.
            # def create_linked_list(self):
            #     # create the first node
            #     node1 = Node(80)
            #     # set the head field to the first node
            #     self.head = node1
            #     # create the second node
            #     node2 = Node(9)
            #     # link the first and second nodes
            #     node1.next = node2
# 
# Here, we have created a node named node2 with value 9. We then linked it with node1 by assigning node2 to the next field of node1.
# 
# Let's add the third node as well.
            # def create_linked_list(self):
            # # create the first node
                # node1 = Node(80)
            # # set the head field to the first node
                # self.head = node1
            # # create the second node
                # node2 = Node(9)
            # # link the first and second nodes
                # node1.next = node2
            # # create the third node
                # node3 = Node(14)
            # # link the second and third nodes
                # node2.next = node3