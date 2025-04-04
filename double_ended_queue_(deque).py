# .............................Introduction........................
# So far, we learned about two types of queues: linear and circular.

# Now, in this lesson, we will learn about deque.

# As the name suggests, deque is a double ended queue, and we can use any end to insert and delete elements.

#     Insertion--->|7, 3, 1, 6, 8|<-----Insertion
#     removal <----|             |----->Removal

# The deque does not necessarily follow the First-In-First-Out principle.
# A deque (Double-Ended Queue) allows elements to be added and removed from both the front and the rear.

# ...................Thought Process...................
# We can create a deque in five steps:

# 1. Initialize a deque.
# Let's create an empty list to initialize a deque.
#         deque = []

# 2. Insert an element from the rear end.
# To insert an element from the rear, we can use the append() method.
#         deque.append(25)

# Here, we inserted element 25 to the deque.

# 3. Insert an element from the front end.
# To insert an element in the front of the queue means we need to insert it in index 0.
#         deque.insert(0, 12)

# Here, we inserted element 12 at index 0 (front of the queue)

# 4. Delete an element from the rear end.
# We can use the pop() function to delete an element from the rear end (back of the queue).
#         deque.pop()

# 5. Delete an element from the front end.
# To delete an element from the front, we need to remove the element at index 0. We can achieve this by using pop(0).
#         deque.pop(0)


