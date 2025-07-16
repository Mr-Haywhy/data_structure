'''
~ Introduction
A spanning tree is a subgraph of a connected graph, which includes all the vertices of the graph and forms a tree structure.

NOTE: Typically, we can remove both vertices and/or edges in subgraphs. But in spanning trees, we can only remove the edges.

Let us consider a graph as shown in figure below.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.6.1.png

Some spanning trees of the above graph are:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.6.2.png

Here, we converted a graph into a tree such that:
    * It is acyclic.
    * It is connected.
    * It has all the vertices from the graph.

The number of spanning trees that can be generated from a graph with n vertices is given by the formula n**(n-2).

For instance, when n is 4, the maximum count of potential spanning trees would be 4**2 = 16. So, from a complete graph with 4 vertices, it's possible to create 16 spanning trees.

~ Not a Spanning Tree
Not every subgraph can qualify as a spanning tree. So, let's look at some subgraphs that are not spanning trees.

Subgraph With Cyclic Graph
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.6.3.png

Subgraph With Isolated Vertices
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.6.4.png

Subgraph With Missing Vertices
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.6.5.png


~ Minimum Spanning Trees
A graph can have more than one spanning tree.

In the case of weighted graphs, a minimum spanning tree is a spanning tree with the lowest sum of weight of vertices in the spanning tree.

So, for an unweighted graph, any spanning tree is a minimum spanning tree as all of the edges have the same weight.

Let us consider the graph below.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.6.6.png

Some spanning trees of the above graph are:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.6.7.png

The tree with the minimum total weight is the minimum spanning tree of the graph as shown in figure below.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-15.6.8.png

~ Applications of Minimum Spanning Trees
Minimum spanning trees have two distinct features:

    * There are no loops.
    * They contain the minimum possible number (weight) of edges.
    
Some of the most common applications of spanning trees are:

1. Shortest Path
Spanning trees, especially the minimum spanning tree, can be used to design the shortest path for transportation networks, such as paths, railways, and airline routes.

2. Clustering
Spanning trees can be used in data clustering.

By removing the longest edges, or those above a certain threshold, the MST is divided into several disconnected subtrees, each representing a separate cluster.

3. Electrical Circuit Design
Spanning trees are used in the design of electrical circuits to ensure there are no loops, which can cause short circuits.
'''