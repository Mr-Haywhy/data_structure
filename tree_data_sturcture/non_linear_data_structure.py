#..............Introduction.................
# The data structures we learned up until this point—lists, stacks, queues, and linked lists—are linear data structures.

# To recap, in a linear data structure:

# Elements are arranged sequentially.
# Each element has previous and next elements, except for the first and last elements.
# Elements can be traversed in a single run.
# Linear data structures are powerful and versatile. However, they have certain limitations, which we will explore next.

#............Real-Life Analogy: Planning a Travel Route.......
# Assume you have to travel from city A to F.
# This is a perfect problem for linear data structures because every city has a unique previous and next landmark.
# However, in real life, there may be multiple paths leading from A to F:
# If we take a linear approach to solve this nonlinear problem, our solution may not be optimal, which we will explore next.

#.........Solving the Problem Using a Linear Approach.........
# In a linear approach, each element must have a unique predecessor and successor. However, our problem presents a branching path at city B.
# To maintain linearity, we will choose the nearest immediate landmark, city C, as the successor city of city B.
# Using this logic, our route taken is: A -> B -> C -> D -> E -> F.
# Here, the total distance covered is: 13km (2 + 4 + 4 + 1 + 2).

# In a non-linear approach, an element can have a number of predecessors and successors. Here, we list out all the possible paths and choose the best one.
# From this image, we can see that there are multiple ways to reach from A to F.

# *Path 1: A -> B -> C -> D -> E -> F (13 km)
# *Path 2: A -> B-> E -> F (10 km)

# Since Path 2 provides the shortest path from A to F, we choose Path 2.

#............Why Use a Non-Linear Approach?...............
# From the previous problem, we learned that the linear approach and, by extension, linear data structures, work great when the problem is characterized by a one-to-one relationship.

# However, they may not offer the optimal solution when the elements are characterized by a one-to-many relationship.
# Let's take a look at another example to understand the limitations of linear data structures better.
# Say a family of three enters a room. And suppose that Max is the father (parent) of Alice and Bob.
# We can use a list to store their name like this:

# [Alice| Bob| Max]

# Can you use a linear data structure to show the relationship between them?
# Since our example consists of a parent having two children (one-to-many), we can't use linear data structures to show this information.

# TAKEAWAY: The primary limitation of linear data structures is that they cannot naturally represent hierarchical or branching relationships, as each element is limited to exactly one predecessor and one successor.

# So, how about we use something like this:

#                 Max
#                 /\
#                /  \
#               /    \
#             Bob    Alice

# From this figure, it's clear that Max is the parent of Bob and Alice.

# This figure is called a Tree, which is the first non-linear data structure we will be covering in our course starting from the next lesson.