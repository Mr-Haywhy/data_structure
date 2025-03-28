#...................CIRCULAR.LINKED.LIST.......................#
# In the previous chapter, we created linked lists where each node directly points to the next node, and the last node points to None. This type of linked list is known as a singly linked list.

# Now, we'll make linked lists where the last node points back to the head node. This kind of linked list is called a circular linked list.

# Here, the last node points to the head node, creating a circular structure.

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

linked_list = CircularLinkedList()
linked_list.create_linked_list()


#..............Traverse a Circular Linked List...............#
# RECALL: Traversal is the process of going through each node one by one.

