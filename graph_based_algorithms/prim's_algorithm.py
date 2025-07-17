'''
~ Introduction
Just like Kruskal's algorithm, Prim's algorithm follows a greedy method to find the minimum spanning tree.

Prim's algorithm is similar to Kruskal's algorithm, except that you can add a new edge to the minimum spanning tree only if it is connected to an existing vertex.

Consider the graph below.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.1.png

While creating the minimum spanning tree, we start from the lowest-cost edge, which is A-B with a weight of 2. The next lowest-cost edge is D-C with weight 3.

But we can't accept D-C because it doesn't connect to the tree. Hence, we reject this edge and move to the next lowest-cost edge, which is A-D with weight 5.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.2.png

This still doesn't contain all the vertices. So, we again check the edge with the lowest weight which is D-C with weight 3.

Unlike before, we can accept this as it links to an element in the tree. So we add D-C.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.3.png

The next edge with the lowest weight is B-C. But since adding B-C will result in a cycle, we will not add it.

So, this will be our resulting MST.

Next, we will implement a prim's algorithm to solve a graph.

~ Working of Prim's Algorithm
Consider the graph below:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.4.png

Step I: Add the Lowest-Cost Edge
Now, let's use the process we described before to create a minimum spanning tree from the given graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.5.png

Since A-F is the edge with the lowest weight let's start by adding A-F.

Add A-F with cost 5 to the spanning tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.6.png

Step II: Add Vertex Connected to A or F
Now, we will filter the vertices that are connected to the existing vertices A and F.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.7.png

Add F-E with cost 18 to the tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.8.png

Step III: Add Vertex Connected to A, F, or E
Again, look for possible edges that we can add to the tree. These edges are
    * A-B (cost 25)
    * E-G (cost 16)
    * E-D (cost 12)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.9.png

Add E-D with cost 12.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.10.png

Step IV: Add the Edge D-C to the Spanning Tree
Similarly, the next lowest-cost edge that is connected to some vertex in the spanning tree is D-C.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.11.png

Add D-C with cost 10.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.12.png

Step V: Add the Remaining Vertices
Now, we'll add all the remaining vertices to the spanning tree.

Add C-B with cost 9.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.13.png

Add B-G with cost 6.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.8.14.png

If we add any more vertices to the tree, it forms a cycle. Thus, the minimum cost tree is complete.

NOTE: The end result is the same as Kruskal's algorithm.

Now, let's implement this algorithm in Python. But first, you'll be taking a quiz.
'''

'''
~ Thought process: Prim's Algorithm
Now that we are well caught up with the working of the algorithm, let's try implementing it in Python.

1. Choose a graph and a starting vertex.

        def prim(graph, start):

2. Initialize a dictionary to keep track of vertices included in the MST.

        in_tree = {vertex: False for vertex in graph}
        in_tree[start] = True

Also define an empty list named MST.

        MST = []


3. Get the shortest edges that connect a vertex in the MST to a vertex outside the MST.

        edges = [(start, end, weight) for start, neighbors in graph.items() for end, weight in neighbors.items() if in_tree[start] and not in_tree[end]]
        sorted_edges = sorted(edges, key=lambda edge: edge[2])
        shortest_edge = sorted_edges[0]

4. Add the shortest edge to the MST and mark the connected vertex as included.

        start, end, weight = shortest_edge
        MST.append((start, end, weight))
        in_tree[end] = True

5. Repeat Step 3 and 4 until all vertices are included in the MST.

        while not all(in_tree.values()):
'''

# Source Code: Prim's Algorithm

# define the graph
graph = {
    'A': {'B': 25, 'F': 5},
    'B': {'A': 25, 'C': 9, 'G': 6},
    'C': {'B': 9, 'D': 10},
    'D': {'C': 10, 'G': 11, 'E': 12},
    'E': {'D': 12, 'G': 16, 'F': 18},
    'F': {'E': 18, 'A': 5},
    'G': {'D': 11, 'E': 16, 'B': 6}
}

def prim(graph, start):
    
    # initialize a dictionary to keep track of vertices included in the MST
    in_tree = {vertex: False for vertex in graph}
    in_tree[start] = True

    # start with an empty tree
    MST = []

    # continue until all vertices are included in the MST
    while not all(in_tree.values()):
        # get the shortest edge that connect a vertex in the MST to a vertex outside the MST
        edges = [(start, end, weight) for start, neighbors in graph.items() for end, weight in neighbors.items() if in_tree[start] and not in_tree[end]]
        sorted_edges = sorted(edges, key=lambda edge: edge[2])
        shortest_edge = sorted_edges[0]

        # add the shortest edge to the MST and mark the connected vertex as included
        start, end, weight = shortest_edge
        MST.append((start, end, weight))
        in_tree[end] = True

    return MST

mst = prim(graph, 'A')
for (start, end, weight) in mst:
    print(f"{start} - {end} : {weight} ")


'''
Output:
    A - F : 5 
    F - E : 18 
    E - D : 12 
    D - C : 10 
    C - B : 9 
    B - G : 6 
'''

"""
~ Time Complexity
The time complexity of Prim's algorithm ranges from O(E log V) to O(V^2). Our implementation is the worst-case scenario and has a time complexity of O(V^2).

This is because the outer loop runs until all the vertices are included in the MST and the inner loop iterates over all edges.So, for each vertex, the code potentially checks all edges in the worst case.
"""