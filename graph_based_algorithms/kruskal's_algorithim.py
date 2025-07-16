"""
~ Introduction
Kruskal's algorithm is another greedy algorithm that is used to find minimum cost spanning trees in a weighted graph.

Remember, a minimum spanning tree is a subgraph that touches all the vertices without forming any cycles and does so with the least total edge weight.

In other words, the algorithm helps to find the cheapest way to connect all the vertices in a graph without forming any cycles.

* Real Life Scenario
Imagine you are in a telecommunications company that wants to set up a new network in a region with several towns.

You want to ensure that every town has access to the network, but laying down fiber optic cables is expensive. So, your goal is to connect all the towns with the least amount of cable to minimize costs.

This is an example of a minimum spanning tree. Here, we are connecting all the cities to the network without any redundant connections i.e. without any cycles.

We can use Kruskal's algorithm to build the minimum spanning tree that can be used as a network model to set up a network.

~ Kruskal's Algorithm
Suppose we have a graph with vertices, edges, and weight. Our goal is to make a minimum spanning tree.

Follow these steps to build a minimum spanning tree:

1. Start with the lowest-cost edge and add it to the minimum spanning tree.
2. Move to the next lowest-cost edge and add it to the minimum spanning tree.
3. However, if adding the edge forms a cycle, ignore that edge and move to the next lowest-cost edge.
4. The minimum spanning tree will be formed once you've scanned all the edges of the graph.

~ Working of Kruskal's Algorithm
Suppose we have the following graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.7.1.png
Now, let's learn how to create a minimum spanning tree from this graph.

~ Step I: Create an Edge List
Before we begin, let's create a list to keep track of the edges we will use along the way, sorted in increasing order of their weight.

For the above graph, the edge list would be:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.7.2.png

Now, let's move on to the next step.

~ Step II: Remove All Edges
Before creating something, one must first destroy! So, we remove all the edges from the graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.7.3.png

Next, we'll add the lowest-cost edges one by one.
~ Step III: Add the Lowest-Cost Edge
The lowest cost edge is the one connecting A and F with a cost of 5. Let's add this edge to the minimum spanning tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.7.4.png

Now, we move on to the edge with the second-lowest cost.
~ Step IV: Add the Next Lowest-Cost Edge
The edge with the second-lowest cost is 6, and it connects B and G. Adding this edge doesn't form a cycle, so let's add it to the spanning tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.7.5.png

~ Step V: Add B-C and C-D to the Spanning Tree
Let's add the next lowest-cost edges B-C and C-D to the tree. Adding these edges doesn't form a cycle, which means we can add them to the tree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.7.6.png

~ Step VI: Ignore the Edge That Creates a Cycle
The next low cost edge is 11, connecting D and G.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.7.7.png

However, adding this edge to the tree forms a cycle, so we omit this edge and move to the next lowest-cost edge.

So everytime we encounter an edge like this that forms a cycle, we ignore it. If we continue like this we should get our MST.

~ Step VII: Add E-D and Ignore E-G
* Add E-D to the Spanning Tree
The next lowest-cost edge is 12 connecting edges E and D. Adding them to the tree does not form a cycle.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.7.8.png

Ignore E-G as it forms a cycle.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.7.9.png

~ Step VIII: Add the Final Edge
We now have two edges left. Let's see if they form a cycle and add them to the tree if they don't.

* Add E-F to the Spanning Tree
The next lowest cost is 18 connecting E and F. Let's add it to the tree as it does not form a cycle.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.7.10.png

* Ignore A-B as it forms a cycle.
At this point, we've gone through all the edges from the lowest cost to the highest cost. Thus, the minimum spanning tree of the graph is now ready.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.7.11.png

Next, you'll take a quiz, then we'll implement the algorithm using Python code.
"""

'''
~ Thought Process: Kruskal's Algorithm
1. Generate the Sorted Edge List.
Create a list of all edges in the graph, sorted by their weights. The edges are in the form (start, end, weight)

    edges = [(start, end, weight) for start, neighbors in graph.items() for end, weight in neighbors.items()]
    sorted_edges = sorted(edges, key=lambda edge: edge[2])

2. Define the Forest.
Since we are creating a tree, we need to ensure that there will be no cycles. So we create a dictionary tree to track the parent of each vertex. Initially, each vertex will be its own parent.

    tree = {vertex: vertex for vertex in graph}
    MST = []

We have also created an empty list MST to hold the minimum spanning tree.

Next, we'll iterate through the sorted edges.

3. Iterate Through the Sorted Edges.
For each edge (start, end, weight) in the sorted list of edges:

    for start, end, weight in sorted_edges:
    
4. Add edge to MST.
Check if adding the edge would create a cycle. If the parent of the starting vertex is not equal to the parent of the ending vertex, then it won't create a cycle.

If there's no cycle, add the edge to the MST.

    if tree[start] != tree[end]:
        MST.append((start, end, weight))
        
5. Update the parent.
When a new connection (edge) is made between two points (vertices), the subsets of the connected vertices need to be merged.

    for vertex, parent in tree.items():
        if parent == tree[end]:
            tree[vertex] = tree[start]

Here,
tree[end] and tree[start] represent the subsets of the end and start vertices, respectively.

The algorithm checks each vertex in the tree.If a vertex is part of the same subset as the end vertex, the algorithm updates it to be the same subset as the start vertex.

This process merges the subsets of the start and end vertices into a single subset.
'''

# Source Code: Kruskal's Algorithm
graph = {
    'A': {'B': 25, 'F': 5},
    'B': {'A': 25, 'C': 9, 'G': 6},
    'C': {'B': 9, 'D': 10},
    'D': {'C': 10, 'G': 11, 'E': 12},
    'E': {'D': 12, 'G': 16, 'F': 18},
    'F': {'E': 18, 'A': 5},
    'G': {'D': 11, 'E': 16, 'B': 6}
}

def kruskal(graph):
    # initialize a variable
    tree = {vertex:vertex for vertex in graph}
    MST = []

    # get edge list
    edges = [(start, end, weight) for start, neighbors in graph.items() for end, weight in neighbors.items()]
    sorted_edges = sorted(edges, key=lambda edge: edge[2])
    for start, end, weight in sorted_edges:
        if tree[start] != tree[end] :
            MST.append((start, end, weight))
            # update all vertices that belong to the 'end' set
            # and assign them to the 'start' set
            for vertex, parent in tree.items():
                if parent == tree[end]:
                    tree[vertex] = tree[start]
    return MST

print(kruskal(graph))


'''
Output:
[('A', 'F', 5), ('B', 'G', 6), ('B', 'C', 9), ('C', 'D', 10), ('D', 'E', 12), ('E', 'F', 18)]
'''

'''
This is a simplified version of Kruskal's algorithm. It follows the algorithm but isn't the optimal way to do so.

For more efficient execution, we can use union find data structure to keep track of the tree/parent.

~ Time Complexity
The ideal time complexity of Kruskal's algorithm (when we use Union Find data structure) is O(E logE) or O(E logV).

This implementation results in a time complexity of O(E*V), dominated by the section used to find the MST.
'''