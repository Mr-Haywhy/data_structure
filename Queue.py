#.........................Introduction to Queue......................#
# The queue is a first-in-first-out (FIFO) data structure.
# A queue data structure is similar to a queue in real life. Suppose you're in line at a movie theater.
# The first person in the line will be the first to get a ticket, and the last person in the line is last to get the tickets. This is the concept of FIFO.

# In computer science, a queue is used to maintain a particular order of operations, like managing processes in an operating system and handling requests on a web server.

#.................Create a Queue..................#
# We can create a queue in three steps:

# 1. Create an empty queue...................................
# We will use a list to create an empty queue.
#     queue = []
#
# 2. Add elements to the queue................................
# Adding elements to the queue is called enqueue.
# We can use the list's append() method to enqueue elements. This adds an element from the back of the queue.
# The back of the queue is also called the rear.
#     # add two elements to the queue
#     queue.append(10)
#     queue.append(5)

# 3. Remove elements from the queue...........................
# Removing elements from the queue is called dequeue.
# As the queue follows the first-in-first-out (FIFO) principle, it utilizes a different end (front) for removing elements to ensure the first element goes out first.
# We can use pop(0) to remove the first element of the queue.
#     # remove the first element
#     item = queue.pop(0)

#......................Source Code...........................#
# create class to represent queue
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def print_queue(self, message):
        print(f"{message}: {self.queue}")

# initializes queue attribute to an empty list
queue1 = Queue()

# take list of numbers as input
numbers = list(map(int, input().split()))

for num in numbers:
    # add each input to the queue
    queue1.enqueue(num)

# add elements to the queue
    # queue1.enqueue(5)
    # queue1.enqueue(10)
    # queue1.enqueue(100)

# print queue
queue1.print_queue("Queue after adding 3 elements")

# remove item from last
print(f"Dequeue an Element {queue1.dequeue()}")
queue1.print_queue("After removing an item")

# remove item again
print(f"Dequeue Another Element {queue1.dequeue()}")
queue1.print_queue("After removing another item")