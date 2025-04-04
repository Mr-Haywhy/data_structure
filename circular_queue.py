#......................Introduction.......................#
# In linear queues, space once used couldn't be reused, which caused inefficient utilization of space. This problem can be solved using a circular queue.
# A circular queue is an extended version of a linear queue where the last element is connected to the first element, thus forming a circular structure.
# 
#...................Working of Circular Queues....................#
# In a circular queue, we use a pointer (say front pointer) to track the dequeued elements from the front of the queue.
# 
# 1. Create a circular queue.
    # Let's create a circular queue of size 6 and a front pointer (F).
    # Here, the queue is currently empty, and the front pointer is pointing to index 0.
# 2. Enqueue in an empty circular queue.
    # Now, let's insert elements to the queue.
# 3. Dequeue in a circular queue.
    # To dequeue the element in a circular queue, we will use the front pointer.
    # The element pointed by the front pointer is removed from the queue first. Then, the pointer shifts to the next index.
    # As you can see the index 0 has a vacant space.
    # In linear queues, we couldn't re-utilize these vacant spaces.
    # But as this is a circular queue, we can circularly move from the last index to the first index and insert a value in index 0.
# 4. Fill the vacant space in index 0.
    # Now, to add a new element (5), we can move circularly from the last index to the first index and re-fill index 0.
    # We moved circularly from index 5 to index 0 and inserted an element.
# Next, we will code to create a circular queue and perform enqueue and dequeue operations.
# 

#.........................Create a Circular Queue....................#
# To show the circular nature of a circular queue, we will limit the size of the queue.
# 1. Initialize a circular queue.
# Let's first initialize an empty queue of fixed size.
#         queue = [None] * size
# We will set the size of the queue and replace None with actual elements later.
# Now, let's initialize the front pointer.
#         front = 0
# Initially, the front pointer is set to 0. The element that is pointed by the front is the element to be dequeued.
# There is one more variable we need to declare to count the total number of elements in the queue.
#         count = 0
# After each insertion, count is incremented by 1.
# After each deletion, count is decremented by 1.
# 
# 2. Insert an element (Enqueue).
# In a circular queue, insertion typically occurs at the rear end, but it can also take place at the front if the rear is full and the front index is available for insertion.
# This flexibility is enabled by the circular nature of the data structure, where the front and rear indices wrap around to the beginning of the array when they reach the end.

# Let's insert 5 into the following queue.
        # [ , 16, 12, 20, 23, 26]
        # [ ,  1,  2,  3,  4,  5]

# Technically, 5 should be at the end of the queue.
        # index = (front + count)

        # [ , 16, 12, 20, 23, 26]
        # [0,  1,  2,  3,  4,  5]

            # F = 1
            # Count = 5
            # index = 1 + 5 = 6

# However, our queue has limited size, and there is a space at the front. So, to add 5 to the available space, we will use the circular nature of the queue.
        # index = (front + count) % size

        # [ , 16, 12, 20, 23, 26]
        # [0,  1,  2,  3,  4,  5]

            # F = 1
            # Count = 5
            # index = (1 + 5) % 6 = 6 % 6 = 0

# Now, we will insert an element in this index.
        # queue[index] = item

# This is how we perform enqueue operations in a circular queue.
# Also, after every new insertion, we increment the count by 1.
#         count += 1

# The count is used to check if the queue is full. The queue is full when the count equals the total size of the queue.
#         count == size

# 3. Remove an element (Dequeue).
# We use the front pointer to dequeue an element from the front of the queue.
        # # remove element from front
        # queue[front] = None

# Once we dequeue an element, we need to move the front pointer to the next position. As the pointer can move circularly, we need to calculate its next index by:

#         front = (front + 1) % size
# This code updates the front pointer to point to the next element in the queue.

# After performing the dequeue, we need to decrement the count by 1.

        # count -= 1
# Before we remove an element from a queue, we need to check if the queue is empty or not.

# The queue is empty if

        # count == 0
# Now, we will put all these together and use OOP to implement a circular queue.

#....................Source Code: Circular Queue....................#
# create class to represent a circular queue
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        # initialize front pointer
        self.front = 0 
        # count the number of elements in the queue
        self.count = 0 

    # check if the queue is full
    def is_full(self):
        return self.count == self.size

    # check if the queue is empty
    def is_empty(self):
        return self.count == 0

    # if queue is not full, perform enqueue and increment count
    def enqueue(self, item):
        if self.is_full():
            return
        index = (self.front + self.count) % self.size
        self.queue[index] = item
        self.count += 1

    # if queue is not empty, perform dequeue and decrement count
    def dequeue(self):
        if self.is_empty():
            return
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1

    def print_queue(self, message):
        print(f"{message}: {self.queue}")

# initialize circular queue with size 4
queue1 = CircularQueue(4)

# enqueue operations
queue1.enqueue(5)
queue1.enqueue(10)
queue1.enqueue(100)
queue1.print_queue("Queue after adding 3 elements")

# dequeue operation
queue1.dequeue()
queue1.print_queue("After removing an item")

# enqueue operations
queue1.enqueue(150)
queue1.enqueue(200)
queue1.print_queue("After adding two more items")

# trying to enqueue when queue is full
queue1.enqueue(250)