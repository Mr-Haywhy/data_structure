'''
~ Introduction
In this chapter, you will learn about different terminologies and the theory behind graph data structure. Let's start with the concept of graph connectivity.

~ Connectivity
Connectivity in a graph refers to the level of connectedness of a graph. In practical terms, it signifies the fewest number of nodes or edges you must remove to split the graph into at least two isolated parts.

The greater the connectivity of a graph, the stronger and more reliable the network becomes.

~ Cut Vertex (Articulation Point)
A cut-vertex is a node in a graph that, when removed (with its incident edges), splits the graph into two or more isolated parts.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.1.png

In the figure above, the node colored in red is the cut vertex.

A graph can have multiple cut vertices like this.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.2.png

These cut vertices represent vulnerabilities in a connected network—single points whose failure would split the network into two or more components.

So, a reliable network has as few cut vertices as possible.

~ Vertex-Cut Set
In some cases, the removal of a single node may not split the graph into two isolated parts. However, the removal of a certain set of vertices will disconnect the graph. This is known as the vertex-cut set.

A vertex-cut set of a connected graph is a set of vertices with the following properties:
    *The removal of all the vertices in the set disconnects the graph.
    *The removal of some (but not all) vertices in the set does not disconnect the graph.

Consider the following graph:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.3.png

We can disconnect the graph by removing the two vertices b and e.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.4.png

However, we cannot disconnect it by removing just one of these vertices.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.5.png
So, the vertex-cut set of our graph is {b, e}.

~ Cut Edge (Bridge)
A bridge is a specific edge that, when removed, results in a disconnected graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.6.png

In the figure above, the edge connecting the vertices 0 and 4 is a bridge because removing it will result in two distinct graphs. However, removing any other edge will still result in a single graph.

Thus, a bridge serves as a critical point in the network's structure, and its removal can break the network into separate components.

~ Cut Set
A cut set is the set of all the edges in a graph that must be removed to disconnect the graph.

It represents the minimum set of edges needed to separate the graph into distinct components.

For example, consider the following graph:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.7.png

We can disconnect the graph by removing the three edges bd, be, and ce, but we cannot disconnect it by removing just one or two of these edges.

So, our cut-set is {bd, be, ce}.

~ Subgraph
A subgraph is a part of another graph formed by selecting some subset of vertices and edges from the original graph without adding any new elements.

A subgraph retains the same vertices and edges as the original graph and must have the same endpoints for its edges.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.8.png

In the figure, H1, H2, and H3 are subgraphs of G.
Mathematically, a subgraph of a graph G is a graph H such that:
    * Every vertex in H is also a vertex in G.
    * Every edge in H is also an edge in G.
    * Every edge in H has the same endpoints in H as it has in G.

~ Connected Graphs
A connected graph is a type of graph where there is a path between every pair of vertices.

In other words, it is possible to reach any vertex in the graph from any other vertex by traversing along the edges of the graph.
Remember: There should not be any isolated vertices in a connected graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.9.png

In this graph,
    * We can visit any vertex from any other vertex.
    * There is at least one path between every pair of vertices.
    * There are no isolated vertices.
Therefore, it is a connected graph.

~ Strongly Connected Graph
A strongly connected graph is a type of directed graph where there is a directed path between every pair of distinct vertices.

That means, in a strongly connected graph, you can traverse from any vertex to any other vertex.

Let's look at an example.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.10.png
The graph shown above is a strongly connected graph as there is a forward path between every pair of distinct vertices.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.11.png
Here, we have taken vertices 1, 2, and 3, displaying forward traversal from each of these respective vertices.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.12.png
On the other hand, the graph above is not a strongly connected graph as there is no forward path from 4 to any other vertex.

~ Strongly Connected Components
Sometimes, the whole graph may not be strongly connected but parts of the graph may be strongly connected. These strongly connected parts are known as strongly connected components.

Let's look at an example.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.13.png

This graph is not a strongly connected graph. However, if you look closely, parts of it are strongly connected.

The strongly connected components of the above graph are:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.14.png

Here, if we divide the graph into two components A and B, each component will be strongly connected.

Thus, strongly connected components are subgraphs of a graph that form a strongly connected graph.

NOTE: An isolated vertex is also counted as a strongly connected component.

~ Island
An island is a set of vertices and edges not connected to the rest of the graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.16.png

As you can see in the figure, there are two islands in the same graph.

While there might be paths connecting all the vertices within an island, no edges connect one island to another even though both islands belong to the same graph.

~ Disconnected Graph
A graph is considered disconnected when it contains one or more islands.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.1.17.png

The graph above consists of the islands A, B, and C. Thus, this graph is a disconnected graph.

~ Walk
A walk is a route from a starting vertex to an end vertex. In a walk, you can have repeated vertices and repeated edges.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.2.1.png

In the above figure, 1 -> 2 -> 3 -> 4 -> 2 -> 1 -> 3 is a walk.

The number of edges encountered during a walk is called the length of a walk.

Hence,
    Length of the above walk: 6
Let's look at one more example of a walk.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.2.2.png

Walk: 5 -> 3 -> 2 -> 1 -> 2 -> 4 -> 5

Length of the above walk: 6
NOTE: A walk can start and end in the same vertex.

~ Trail
A walk in which an edge doesn't repeat is called a trail.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.2.3.png

Here, 1 -> 3 -> 8 -> 6 -> 3 -> 2 is a trail.

Let's look at another example of a trail.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.2.4.png

Here, 1 -> 3 -> 8 -> 6 -> 3 -> 2 -> 1 is a trail.

If a trail starts and ends in the same vertex, it is called a circuit.
Therefore, the above trail is also a circuit because it starts and ends in vertex 1.

NOTE: Vertices can be repeated in a trail, just not edges.

~ Path
A path is a trail that doesn't allow repetition of vertices.

So, neither the edges nor the vertices can be repeated in a path.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.2.5.png

Here, the sequence of vertices 1 -> 2 -> 5 -> 3 represents a path from vertex 1 to vertex 3.

However, the starting and end vertex in a path can be the same. Such paths are called closed paths.

NOTE: A closed path is also called a cycle.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.2.6.png
Here, the path 1 -> 2 -> 5 -> 3 -> 4 -> 1 is a closed path starting from and ending in vertex 1.

~ Summary
We learned some pretty similar concepts in this lesson, and it's easy to confuse them with one another. So, you can review this summarized version to avoid possible confusion:
    * Walk: Vertices may repeat. Edges may repeat.
    * Trail: Vertices may repeat. Edges cannot be repeated.
    * Circuit: A closed trail. Starts and ends with the same vertex.
    * Path: Vertices cannot repeat. Edges cannot be repeated.
    * Cycle: A closed path. Starts and ends with the same vertex.

~ Euler Trail and Euler Circuit
An Euler trail refers to a trail in a graph that visits every edge exactly once.

If the Euler trail starts and ends with the same vertex, it is called an Euler circuit.

Not all graphs have an Euler trail. For a graph to have an Euler trail, it must satisfy one of two conditions:
    * There are exactly two vertices of odd degrees.
    * Each vertex has an even degree.
Now, let's looks at these conditions in greater detail.

~ Condition I: Exactly Two Vertices of Odd Degrees
As a reminder, a vertex has an odd degree if it has an odd number of edges. For example,
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.2.7.png

Now, if there are exactly two nodes of odd degrees, we can simply put them as the endpoints of the route. Here,
    * The two odd-degree vertices serve as the start and end points of the trail.
    * As you traverse the graph, every time you enter a vertex (other than the starting and ending vertices), you can always leave it along another edge since they have even degrees.
    * The trail will start at one odd-degree vertex and end at the other, ensuring every edge is traversed exactly once.
Such routes that visit every edge in a graph only once are called the Euler trail or Euler path.

NOTE: If there are more than two vertices of odd degree, there is no way to construct a trail that traverses every edge exactly once.

Next, we'll look at the second condition for an Euler trail.

~ Condition II: Each Vertex Has an Even Degree
All the vertices of the graph below have an even degree:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.2.8.png

In such cases, the starting and ending nodes are the same. Here,
    * Every time you enter a vertex along an edge, you must leave it along another edge to continue the trail.
    * If every vertex has an even degree, you can always pair up the edges, ensuring that for every entrance, there is an exit.
    * This allows you to traverse every edge once without getting stuck and return to the starting vertex, forming an Eulerian circuit.
Such routes that visit every edge in a graph only once forming a closed trail are called an Euler's circuit.

NOTE: If the Euler trail of a graph exists, then it gives the shortest path from one vertex to another.

~ Hamilton Path and Cycle
Similar to an Euler trail, a path that visits every node in the graph exactly once is called a Hamilton path. The closed version of such a path is called a Hamilton cycle.

A Hamilton cycle exists if the minimum degree of a vertex in a graph with n vertices is greater than or equal to n/2.

~ Equal Graph
Equal graphs are defined based on the equality of their vertex and edge sets.

Two graphs are said to be equal if and only if their corresponding vertex and edge set are identical. This concept is commonly used to compare the structure of graphs.

For example,
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.3.1.png
Here, only the graphs G1 and G2 are equal.

Equal Graph Using Only Graph Diagram
In common practice, we generally use graph diagrams to identify equal graphs without explicitly writing down their vertex sets and edge sets.

To confirm the equality of two graph diagrams, all we have to do is make sure:
    *They have the same number of vertices.
    *The vertices have the same names.
    *The graphs have the same adjacency structure.
For example,
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.3.2.png

Graph sets a and b are equal as they represent the same connections and share the same label name.

NOTE: If you are confused about the spiral nature of the edge connecting Q and P in the second image, don't be. Edges can take any shape, even curves.

Without ever creating a vertex or edge set, we can deduce the graphs are equal just by observing:
    * Both graphs have six vertices.
    * The vertices are labeled P, Q, R, S, T, and U.
    * In both graphs, P, Q, and R are interconnected to each other.
    * S and U are adjacent only to each other.
    * T is isolated.

~ Unequal Graphs
Two graphs are considered unequal if any or all of their vertex or edge sets are unequal.

Remember: Two graphs A and B are equal if and only if both A and B are subsets of each other.

To identify unequal graphs from their graph diagram alone, at least one of the following conditions must be met:
    * The adjacent structures don't match.
    * The labels are different.
For example,
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.3.3.png

The sets of graphs in a and b are not equal as vertices P and R are not connected in graph b.

Remember: Vertex adjacency is not transmitted through the intermediary vertex Q.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.3.4.png

Similarly, the given sets of graphs are also not equal as the labels don't match despite having the same adjacency structure.

~ Isomorphism
Two graphs are said to be isomorphic if they share the same adjacency structure.

Consider the same sets of graphs we previously said were unequal:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.3.5.png

Despite being unequal, the graphs share the same adjacency structure so they are isomorphic.

Similarly, consider these sets of graphs:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.3.6.png

They both share the same adjacency structure but different node names. So, they are also unequal but isomorphic.

~ Complementary Graphs
A complementary graph (G) is defined as a graph that contains the same vertices of the original graph (G) such that

    * if two vertices are connected in G, they are not connected in G.
    * if two vertices are not connected in G, they are connected in G.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.3.7.png

The above figure shows graph G and its complementary graph 
G.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.3.8.png

Complementary graphs are used to represent the inverse or missing relationships between vertices in a given graph.

~ Bipartite Graphs
A bipartite graph is a graph that can be divided into two distinct sets of vertices such that no two vertices within the same set are adjacent.

In other words, all edges in the graph connect a vertex from one set to a vertex in the other set.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.3.9.png

Here, the graph has been divided into two sets of vertices:
    * Red Set: [1, 2, 3, 4, 5]
    * Blue Set: [A, B, C, E]
They are connected in such a way that:
    * No two vertices of the same set are connected.
    * Edges exist only between vertices of different sets.

Bipartite graphs are used when nodes can be grouped into two categories, and connections only exist between nodes of different categories, not within the same category.

************************TYPES OF GRAPH*************************

~ Simple Graph
A simple graph is a graph with no loops or multiple edges.

Example: A railway track is the perfect example of a simple graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.1.png

Remember: In a simple graph with n vertices, the degree of each vertex is, at most, n-1.

~ Regular Graphs
A graph is regular if all the vertices have the same degree.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.2.png

~ Complete Graph
In a complete graph, every pair of vertices is directly connected by an edge. Consider the graph below:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.3.png

Here, vertex 0 and vertex 1 are connected by a distinct edge. Similarly, distinct edges connect vertex 0 to vertex 2 and vertex 3.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.4.png

The same applies to other vertices—each one is connected to another directly within the graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.5.png

Note: A complete graph with n vertices has n*(n-1)/2 edges.

~ Cyclic Graphs
If a graph has at least one cycle, then it's called a cyclic graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.6.png

Cyclic graphs are powerful tools that can be used for various purposes like
    * Detecting redundant loops in codes.
    * Detecting deadlocks in a computer system.
    * Locating routing loops in computer networks.
    * Detecting oscillations in circuits.

~ Acyclic Graphs
Graphs which are free from cycles are called acyclic graphs. Such graphs have no loops whatsoever.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.7.png

Trees are the best examples of acyclic graphs.

~ Planar Graphs
A graph is planar if it can be drawn without intersecting edges.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.8.png

NOTE: A planar graph can be drawn with intersecting edges, but there must exist a way to draw it without intersecting edges.

The above graph is generally drawn like this:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.9.png

Notice that the edges intersect above. However, it is still a planar graph because it can be redrawn without non-intersecting edges (as shown in the first figure we provided).

NOTE: Every planar graph has a vertex of degree at most five.

~ Non-Planar Graph
A graph is non-planar if it can't be drawn without intersecting edges.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.10.png

~ Colored Graphs
In a colored graph, each vertex is assigned a color in such a way that adjacent vertices have different colors.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.11.png

Colored graphs are used to avoid interference among components.

~ Multigraph
In a multigraph, multiple edges may connect the same pair of vertices i.e. multigraphs allow skeins but not self-loops.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.12.png

Directed multigraphs are referred to as multidigraphs.
NOTE: The set of edges that connect the same pair of vertices are called parallel edges.

~ Pseudographs
A multigraph that contains self-loops is called a pseudograph.

NOTE: A self-loop is an edge that connects a vertex to itself.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.13.png

~ Edge Set of a Multigraph
Generally, the edge set is represented as an ordered pair (starting vertex, ending vertex). However, using this in multigraphs isn't possible because in a multigraph two edges can have the same vertex set.

Since we cannot enter the same ordered pair twice, we introduce a new component (frequency) to the ordered pair.

So, an edge of a multigraph is represented using two elements:
    * The first element is an ordered pair denoting the edge.
    * The second element is an integer representing the frequency.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-14.4.14.png

Since the figure shows two edges joining x and z, that edge is represented as [e = ((x, z), 2)]

'''