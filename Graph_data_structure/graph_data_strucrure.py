"""
~ Introduction
A graph is a collection of nodes (vertices) that are interconnected with other nodes with the help of links (also called connections or edges).

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.1.1.png

~ Real-Life Analogy
Consider the following air route of a certain airline.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.1.2.png

In the above figure, the vertices represent cities, and the edges show how they are linked.

This graph helps us see which cities are connected by air routes.

Now, let's look at the formal definition of a graph.

~ Formal Definition of a Graph
A graph is an object consisting of two sets:
    * Vertex set (V)
    * Edge set (E)

Mathematically, a graph is defined as G(V, E) where
    1 V - set of vertices
    2 E - set of edges

For example,
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.1.3.png

Here,
    Vertex Set(V):  1, 2, 3, 4
    Edge Set(E): (1, 2), (1, 3), (2, 3), (3, 4)

NOTE: A graph must consist of at least a single vertex, but it is allowed to have no edges.

Now, let's learn about some graph terminologies to better understand the data structure.

~ Introduction to Graph Terminologies
In this lesson, we will learn about the following graph terminologies:
    * Edge
    * Undirected Graph
    * Directed Graph
    * Relationship Between Vertices and Edges
    * Degree of a Vertex in an Undirected Graph
    * Degree of a Vertex in a Directed Graph
    * Weighted Graph
    * Skeins
    * Graph Representation

These terminologies are fairly simple, so we will just breeze through them.

~ Edge
The link between any two vertices is called an edge. There are two types of edges:
    * Undirected edge
    * Directed edge

~* Undirected Edge
An undirected edge represents a bidirectional relationship between two vertices.

It means that there's no specific direction or order between the two connected vertices. So, undirected edges are represented using lines with no arrowheads.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.1.png

In the above graph, we can traverse from A to B and B to A.

A real-life example would be two-way streets where you can travel in both directions.

~* Directed Edge
It represents a one-directional relationship between two vertices.

It has a starting vertex and an ending vertex. So, they are represented using arrowheads pointing from the starting vertex to the end vertex.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.2.png

In the above graph, we can traverse from A to B but not from B to A.

For example, a one-way route that only allows you to travel in a single direction.

NOTE: Edges needn't always be straight lines. For example, when representing maps with graphs, we use curved lines as edges to better illustrate the nature of the path.


~* Undirected Graphs
An undirected graph is a type of graph where all the edges are undirected.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.3.png

~* Directed Graph
If all the edges of a graph are directed, it is called a directed graph.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.4.png

NOTE: A directed graph is also called a digraph.

~ Relationships Between Vertices and Edges
The relationship between vertices and edges can be defined as one of the following:
    * Incident Edge
    * Adjacent Edge
    * Adjacent Vertex

~ Incident Edge
An edge is incident to a vertex if the edge is connected to the vertex.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.5.png

In the figure:
    * e1 is incident on x and y
    * e2 is incident on y and z
    * e3 is a self-loop and is incident on z only

~ Incident Edge on Directed Graph
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.6.png

In the figure:
    * e1 is incident on y and incident from x
    * e2 is incident on y and incident from z
    * e3 is a self-loop. So, it is incident on z from z

~ Adjacent Vertex
Two vertices sharing a common edge are called adjacent vertices.

Adjacent Vertex in an Undirected Graph
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.7.png

In the figure, the adjacent vertices are
    * x and y (connected by e1)
    * y and z (connected by e2)

Adjacent Vertex in a Directed Graph
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.8.png

In the figure:
    * x is adjacent to y and y is adjacent from x
    * z is adjacent to y and y is adjacent from z

~ Adjacent Edges
Two edges with a common vertex are called adjacent edges.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.9.png

In the figure, e1 and e2 are adjacent edges as they are both incident on y.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.10.png

Similarly, e1 and e2 are adjacent edges in directed graphs because they are both incident on y.

NOTE: Two edges that are incident from the same vertex are also adjacent.

~ Isolated Vertex
If no edge is incident on a vertex, then the vertex is called an isolated vertex.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.11.png

In the figure, p is an isolated vertex.

Similarly, if no edge is incident to or incident from a vertex in a directed graph, it is called an isolated vertex.

~ Degree of a Vertex in an Undirected Graph
The degree of a vertex is the number of edges connected to it.

Consider the graph below:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.12.png

Here, the degree of vertex 1 is 2 because two edges are connected to it.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.13.png

Similarly,
    * the degree of vertex 2 is 2
    * the degree of vertex 3 is 3
    * the degree of vertex 4 is 1
    * the degree of vertex 5 is 0


~ Degree of a Vertex in a Directed Graph
In a directed graph, the degree of a vertex is divided into two types:
    *Indegree: Represents the number of incoming edges to a vertex.
    * Outdegree: Represents the number of outgoing edges from a vertex.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.14.png

Vertex	Indegree	Outdegree
    1	    1	    1
    2	    1	    1
    3	    1	    2
    4	    1	    0
    5	    0	    0

    
~ Weighted Graph
A weighted graph is a type of graph in which each edge is associated with a numerical value called weight.

The weight represents a cost, distance, or some other metric that quantifies the relationship between the connected vertices. For example,
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.15.png

The graph above is a weighted graph where each edge is assigned a weight.

~ Skeins
A skein is a graph consisting of two vertices connected by two or more edges.

The first five skeins are shown in the figure below:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-13.2.16.png

~ Graph Representation
Let's take a moment to revise what we have learned until now.

We started by defining graphs as a collection of interconnected vertices and also came up with a formal definition of a graph as G(V, E).

We've understood them through diagrams, learned about their directed, undirected, and weighted types, and delved into the relationships between their elements.

However, we cannot rely on diagrams in programming. Instead, we need mathematical models to represent graphs. In our Python course, we will focus on two primary representations:
    * Adjacency Matrix
    * Adjacency List
    
In the next lesson, we'll look at adjacency matrices and see how we can implement them in Python.
"""