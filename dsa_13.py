#...................CIRCULAR.LINKED.LIST.......................#
# In the previous chapter, we created linked lists where each node directly points to the next node, and the last node points to None. This type of linked list is known as a singly linked list.

# Now, we'll make linked lists where the last node points back to the head node. This kind of linked list is called a circular linked list.

# Here, the last node points to the head node, creating a circular structure.

# Circular linked lists are suitable for implementing circular data structures or algorithms like circular queues, circular buffers, and circular lists. They can efficiently handle situations where elements need to wrap around or loop back to the beginning.

#...............Why Circular Linked List?..................#
# Imagine you are playing songs from a playlist. The songs in the playlist are organized like a chain using a linked list.

# Each song becomes a node in the list, and they're connected in the order they play.

# Once you reach the last song, the playlist will stop. But what if you want to keep the music playing in a loop?

# With a regular linked list, you'd need to start from the beginning to replay the first song after the last one.

# But there's a simpler solution—the circular linked list.

# In a circular linked list, the next pointer of the last song points back to the first song, creating a closed loop. This allows us to play songs continuously.

# Circular linked lists have uses beyond music.

#...............Create a circular linked list..............#
# To convert a regular linked list to a circular linked list, we will make the last node point to the head node.
    ## i.e. (80, 9, 14)
        # node3.next = self.head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # create circular linked list.
    def create_linked_list(self):
        node1 = Node(80)
        self.head = node1

        node2 = Node(9)
        node1.next = node2

        node3 = Node(14)
        node2.next = node3

        # make the last node point back to the head, making it circular
        node3.next = self.head




#..............Traverse a Circular Linked List...............#
# RECALL: Traversal is the process of going through each node one by one.

# In a singly linked list, we traverse until a node points to None (there is no next node).

# However, in a circular linked list, we will traverse until a node points to the head node.

#............Thought Process to apply Traversal..............#
# To traverse a circular linked list,
# 1. Start at the head.
        # current = self.head
# 2. Loop as long as the next node is not the head node.
        # current = self.head
        # while current.next is not self.head:
            ## move to next node
            # current = current.next

# If current.next is head, we know for sure that it's the last node.

# However, if we try to traverse an empty linked list, the code will not be executed as current is None.

# So, it's important to check if the list is empty before traversing it. We can do this by creating an is_empty() method:

        # def is_empty(self):
            # return self.head is None

# The is_empty() method will return
    # True - If the linked list is empty.
    # False - If the linked list is not empty.


#................Source Code: Traversal of Circular Linked List...............#

        # add an is_empty() method
    def is_empty(self):
        return  self.head is None

    def traverse_list(self):

        # add a condition to check if the list is empty
        if not self.head:
            print("Empty Linked List")
            return

        current = self.head
        while current.next is not self.head:
            print(f"{current.data} ->", end=" ")
            current = current.next
        # print the last node's data as well
        print(f"{current.data} -> {self.head.data}")




linked_list = CircularLinkedList()
linked_list.create_linked_list()