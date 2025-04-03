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