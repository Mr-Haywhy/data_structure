#..........FIND.THE.LARGEST.NUMBER.IN.A.LINKED.LIST...............#
# The process of finding the largest value in a linked list is similar to how we find the largest number in a list.
# To find the largest value in a linked list, we start by assuming the first node's value is the largest.
# Then, we traverse through each node. As we go through the nodes, we compare each node's value with our current largest value and update the largest value if needed.

# method to return the largest number 
def find_largest(self):
    # condition to handle empty linked list
    if not self.head:
        return None
    
    current = self.head

    # initialize the value of head as largest
    largest = current.data

    # iterate until the last node
    while current:
        # update largest if necessary
        if current.data > largest:
            largest = current.data
        current = current.next
    return largest