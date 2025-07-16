"""
Introduction
The Bellman–Ford algorithm finds shortest paths from a node to all other nodes of the graph.

What sets it apart from Dijkstra's algorithm is the fact that Bellman-Ford algorithm can detect the presence of negative cycles in the graph.

~ Why Negative Weights?
At first, negative-weight edges might appear useless in real life. But they actually play a crucial role in explaining a wide range of processes, such as cash flow or heat changes during a chemical reaction.

Imagine a group of friends who often lend money to each other. Each friend is represented as a vertex in the graph, and the edges between them represent the amount of money borrowed or lent.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.1.png

Here,
    * Positive Weight: If Alice lends Bob $10, there's an edge from Alice to Bob with a weight of +10. This means Bob owes Alice $10.
    * Negative Weight: Now, let's say Bob lends Charlie $15. This can be shown by an edge from Charlie to Bob with a weight of -15, indicating Charlie owes Bob $15.

Negative Cycles
A negative cycle in a graph is a cycle that, when traversed, leads to a net decrease in the overall weight.

Let's look at an example.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.2.png

Here, the overall cost of traveling from vertex A back to vertex A is -3. So, the overall weight decreases whenever we travel through this loop in the graph.

* So, what's the shortest path from vertex A to vertex D?
A negative cycle implies that there's no shortest path because you can keep traversing the negative cycle indefinitely to keep reducing the total cost or distance.

This makes the concept of a shortest path meaningless for any path that interacts with this cycle.

In other words, there is no shortest path from vertex A to vertex D because you can keep on reducing the total distance indefinitely by traveling from vertex A to vertex A (through vertices B and C) before finally deciding to go to vertex D.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.3.png

Bellman Ford's algorithm can detect such negative cycles but cannot find the correct shortest distance if negative cycles are present.

~ Working of Bellman Ford's Algorithm
Let's take a weighted graph as shown below.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.6.png

Let us assume vertex A to be our starting vertex. We want to find the shortest path between vertex A and all other vertices.

In the beginning, we set the distance to the starting vertex (in this case, vertex A) as 0, since it's our source vertex.

The distances to all other vertices are set to infinity (or a very large value) because we haven't explored any paths yet.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.7.png

The values represent the cost to reach a given vertex. Our starting vertex has no cost since we start at vertex A.

By contrast, all other vertices are at infinity because we haven't explored any paths yet. So, they can never be reached.


~~ Working of Bellman Ford's Algorithm
So far, we have tentatively set the distance of source vertex A to 0 and that of the other vertices to infinity.

Now, we'll find the actual distances to the vertices by exploring each path and updating the cost of each vertex. The pseudocode below shows how this can be done:

        for each path:
            if (source vertex cost + path cost) < destination vertex cost:
                destination vertex cost = source vertex cost + path cost
                
This process of updating the cost of the destination vertex of each path is called relaxation.

Let's look at this with the help of a figure.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.8.png

Now, let's begin the relaxation for each edge.

Let's start with vertex B. The weight of the edge connecting A and B is 2. So, let's calculate the total cost of going from A to B:

        Cost of A->B = Cost of A + Weight of Edge AB = 0 + 2 = 2

Here, 2 is less than infinity. So, we assign the distance 2 to vertex B.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.9.png
Next, let's update the distances to the remaining vertices.

Now, let's find the distances for A->D and B->D to find out which is the shortest path from A to D.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.10.png

Here,

        A->D = 0 + 6 = 6 < ∞

So, we set 6 as the distance to D. However, there's an alternate path to D i.e. A->B->D or just B->D.

        B->D = 2 + 1 = 3 < 6

Since B->D (3) is shorter than A->D (6), we set the distance of D to 3.

Similarly, we update the destination vertex costs for the remaining edges.

    For C->B,
    Cost of B = Cost of C + Weight of CB = ∞ - 3 = ∞  > 2 (keep 2)
    
    For D->B,
    Cost of B = Cost of D + Weight of DB = 3 + 3 = 6  > 2 (keep 2)
    
    For D->C,
    Cost of C = Cost of D + Weight of DC = 3 - 7 = -4 < ∞ (change to -4)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.11.png

This is a single iteration of the relaxation process. In a graph with V vertices, we perform relaxation for V-1 times.

This is because the cost of a vertex can be affected by the cost of another vertex. Repeating this for V-1 times ensures that all vertices have already had their effect on other vertices.

In our case, we have four vertices. Therefore, we relax three times.

NOTE: In a graph with V vertices, a path can have a maximum length of V-1. So, repeating relaxation for V-1 times means all paths have been considered.

Next, we'll explore the second iteration of the algorithm.

* Second Iteration

Similarly to the first iteration, we repeat the relaxation process and update the values of the destination vertices:

    For A->B,
    Cost of B = Cost of A + Weight of AB = 0 + 2 = 2 (unchanged)

    For A->D,
    Cost of D = Cost of A + Weight of AD = 0 + 6 = 6 > 3 (Keep 3)

    For B->D,
    Cost of D = Cost of B + Weight of BD = 2 + 1 = 3 (unchanged)

    For C->B,
    Cost of B = Cost of C + Weight of CB = -4 - 3 = -7 < 2 (change to -7)

    For D->B,
    Cost of B = Cost of D + Weight of DB = 3 + 3 = 6  > -7 (keep -7)

    For D->C,
    Cost of C = Cost of D + Weight of DC = 3 - 7 = -4 (unchanged)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.12.png
Next, let's look at the final iteration.

* Third Iteration

Let's repeat the relaxation process for the third time:

    For A->B,
    Cost of B = Cost of A + Weight of AB = 0 + 2 = 2 > -7(keep -7)

    For A->D,
    Cost of D = Cost of A + Weight of AD = 0 + 6 = 6 > 3 (Keep 3)

    For B->D,
    Cost of D = Cost of B + Weight of BD = -7 + 1 = -6 < 3 (change to -6)

    For C->B,
    Cost of B = Cost of C + Weight of CB = -4 - 3 = -7 (unchanged)

    For D->B,
    Cost of B = Cost of D + Weight of DB = -6 + 3 = -3  > -7 (keep -7)

    For D->C,
    Cost of C = Cost of D + Weight of DC = -6 - 7 = -13 (change to -13)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.13.png

This marks the completion of the relaxation process. For a graph with four vertices and no cycles, we get the shortest path to all vertices after three iterations.

However, if the graph has a negative cycle, the cost of the vertices will still decrease if we iterate it again.

~ Working: Our Graph Has a Negative Cycle!
This is the result of our third iteration of relaxation:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.14.png

In our graph, if we relax one more time, we can see the edge CB will decrease the weight of vertex B from -7 to -16.

    For C->B,
    Cost of B = Cost of C + Weight of CB = -13 - 3 = -16 (reduced further)

Thus, our graph has negative cycles, and it's not possible to find the shortest path to the vertices.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.15.png

NOTE: The Bellman Ford algorithm can only detect negative cycles but cannot avoid or remove them.

Now, let's take another weighted graph as shown below.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.16.png

Once again, let's calculate the distance to all vertices from source vertex A using the process of relaxation.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.17.png

Since the graph has 4 edges, the relaxation process will have 3 iterations.

* First Iteration

For (A->B), 
Cost of B = Cost of A + Weight of AB = 0 + -2 = -2 < inf (Change to -2)

For (A->D), 
Cost of D = Cost of A + Weight of AD = 0 + 6 = 6 < inf (Change to 6)

For (B->D), 
Cost of D = Cost of B + Weight of BD = -2 + 1 = -1 < 6 (Change to -1)

For (C->B), 
Cost of B = Cost of C + Weight of CB = inf + 3 = inf >= -2 (Keep -2)

For (D->B), 
Cost of B = Cost of D + Weight of DB = -1 + 3 = 2 >= -2 (Keep -2)

For (D->C), 
Cost of C = Cost of D + Weight of DC = -1 + 7 = 6 < inf (Change to 6)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.18.png

* Second Iteration

For (A->B), 
Cost of B = Cost of A + Weight of AB = 0 + -2 = -2 >= -2 (Keep -2)

For (A->D), 
Cost of D = Cost of A + Weight of AD = 0 + 6 = 6 >= -1 (Keep -1)

For (B->D), 
Cost of D = Cost of B + Weight of BD = -2 + 1 = -1 >= -1 (Keep -1)

For (C->B), 
Cost of B = Cost of C + Weight of CB = 6 + 3 = 9 >= -2 (Keep -2)

For (D->B), 
Cost of B = Cost of D + Weight of DB = -1 + 3 = 2 >= -2 (Keep -2)

For (D->C), 
Cost of C = Cost of D + Weight of DC = -1 + 7 = 6 >= 6 (Keep 6)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.19.png

Third Iteration

For (A->B), 
Cost of B = 
Cost of A + Weight of AB = 0 + -2 = -2 >= -2 (Keep -2)

For (A->D), 
Cost of D = 
Cost of A + Weight of AD = 0 + 6 = 6 >= -1 (Keep -1)

For (B->D), 
Cost of D = Cost of B + Weight of BD = -2 + 1 = -1 >= -1 (Keep -1)

For (C->B), 
Cost of B = Cost of C + Weight of CB = 6 + 3 = 9 >= -2 (Keep -2)

For (D->B), 
Cost of B = Cost of D + Weight of DB = -1 + 3 = 2 >= -2 (Keep -2)

For (D->C), 
Cost of C = Cost of D + Weight of DC = -1 + 7 = 6 >= 6 (Keep 6)

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.20.png

As you can see the cost of vertices have stopped changing. We can do any number of iterations but our final cost of each vertex will remain the same.

        [('A', 0), ('B', -2), ('C', 6), ('D', -1)]

Thus, in the case of graph without negative cycles, the cost of vertices will stop changing after (V-1) iterations. This way, we can get the shortest path from any given vertex(A) to all other vertices.

~ Edge List Representation
We use the edge list representation of a graph to implement the Bellman Ford algorithm to make it easier to represent the weights.

An edge list is a list of tuples with each tuple representing an edge in the following format:

        (source_vertex, destination_vertex, weight)

Let's look at an example.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.22.png

The edge list of the above graph is:

graph_edge_list = [
    ('A', 'B', 2),
    ('A', 'C', 4),
    ('B', 'D', 1),
    ('B', 'E', 3),
    ('F', 'C', 5),
    ('A', 'F', -1),
    ('C', 'E', -2),
    ('D', 'E', 5)
]
"""

'''
~ Thought Process: Bellman Ford's Algorithm
1. Initialize distances and predecessors.
Initialize the distance to all vertices as infinity, and the distance to the start vertex as 0. Also set the predecessor of all vertices to None.

        distance = {vertex: float('inf') for vertex in vertices}
        predecessor = {vertex: None for vertex in vertices}
        distance[start_vertex] = 0

2. Relax all edges V-1 times.
For each vertex in the graph, iterate through all the edges. Update the distance value of the destination vertex if there's a shorter path from the source vertex through this edge.

        for _ in range(len(vertices) - 1):
            for u, v, w in edge_list:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u

3. Check for negative weight cycles.
After V-1 iterations, if we can still relax an edge, it means there's a negative weight cycle in the graph.

        for u, v, w in edge_list:
            if distance[u] + w < distance[v]:
                print("Graph contains a negative-weight cycle")
                return

4. Return distances and predecessors.
If there's no negative weight cycle, return the shortest distances and predecessors. For simplicity, we are sorting the vertices based on their cost.

        sorted_distances = sorted(distance.items())
        sorted_predecessors = sorted(predecessor.items())

The bellman_ford() function then uses these steps to determine shortest paths from the given start_vertex to all other vertices in the graph represented by the edge_list.
'''

# Source Code
# edge list representation of graph
graph_edge_list = [
    ('A', 'B', 2),
    ('A', 'C', 4),
    ('B', 'D', 1),
    ('B', 'E', 3),
    ('F', 'C', 5),
    ('A', 'F', -1),
    ('C', 'E', -2),
    ('D', 'E', 5)
]

def bellman_ford(edge_list, start_vertex):
    # create a set of vertices from the edge list
    vertices = set()
    for u, v, _ in edge_list:
        vertices.add(u)
        vertices.add(v)

    # initialize distance and predecessor dictionaries
    distance = {vertex: float('inf') for vertex in vertices}
    predecessor = {vertex: None for vertex in vertices}
    distance[start_vertex] = 0

    # relax the edges V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, w in edge_list:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u

    # check for negative weight cycles
    for u, v, w in edge_list:
        if distance[u] + w < distance[v]:
            print("Graph contains a negative-weight cycle")
            return None

    # sort and return results
    sorted_distances = sorted(distance.items())
    sorted_predecessors = sorted(predecessor.items())
    
    print(f"Sorted distance: {sorted_distances}")
    print(f"Sorted predecessors: {sorted_predecessors}")

bellman_ford(graph_edge_list, 'A')

'''
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.4.23.png
Output

Sorted distance: [('A', 0), ('B', 2), ('C', 4), ('D', 3), ('E', 2), ('F', -1)]
Sorted predecessors: [('A', None), ('B', 'A'), ('C', 'A'), ('D', 'B'), ('E', 'C'), ('F', 'A')]
'''

"""
Time Complexity
The most time consuming part of Bellman Ford's algorithm is the two for loops used for relaxation.

for _ in range(len(vertices) - 1):
    for u, v, w in edge_list:
The outer loop has a time complexity of O(V - 1) and the inner loop has time complexity of O(E).

Here,
    * V - number of vertices
    * E - number of edges
    
Combining both, we get:

Time complexity: O(V * E)
"""