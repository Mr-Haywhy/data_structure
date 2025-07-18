'''
~ Problem Statement
This scenario is the same as the fractional knapsack problem where you're in a MrBeast video, and he will buy you all the items you can fit into a knapsack.

The only difference is that instead of items that can be taken at a fraction, like wheat, oil, and gold bars, we have the following set of items.

        Item	    Weight	    Total Value
        TV	        30 units	$3000
        Laptop	    20 units	$2000
        Weight	    15 units	$1500

The capacity of the knapsack is 35 units.

~ Solving the Problem
If we try solving the problem with the same logic as before, we will find that every item has the same value per weight, which is $100/units.

So, our greedy approach here will simply be:
    1. Pick the most expensive thing that will fit in your knapsack.
    2. Pick the next most expensive thing that will fit in your knapsack. And so on.
This means we will start with the $3000 TV that weighs 30 units and will be left with 5 units in our knapsack.

Since no other items will fit inside the knapsack, our solution brings us goods worth $3000.

~ Optimal Greedy Solution
Now, we will learn when to use greedy algorithms and when not to.

The greedy approach will provide optimal solution if the problem has these properties:
    1. Greedy Choice Property
    2. Optimal Substructure

If a problem has both of these properties, we know for sure that the greedy approach will result in optimal solution.

1. Greedy Choice Property
In a greedy algorithm, we always choose the optimal solution at the moment without considering the consequences of that choice on further steps.

Despite not accounting for future choices, this approach may lead to an optimal solution for some problems.

In other words, optimal solutions can be obtained by making greedy choices. This is known as greedy choice property.

Here's the example from the fractional knapsack problem:

We have a knapsack of capacity 25 units.

        Items	Available Weight	Total Value
        Gold	10 units	        $5000
        Wheat	20 units	        $1000
        Oil	    14 units	        $1400

To fill the knapsack, we use 10 units of Gold with a value of $500 each and 14 units of Oil with a value of $100 and 1 unit of Wheat with a value of $50.

As can be seen here, despite making greedy choices, we are making the optimal choice in each step. So, the fractional knapsack problem satisfies the greedy choice property.

2. Optimal Substructure
Suppose we have a problem that can be divided into subproblems.

There are situations where the optimal solution to these subproblems lead to optimal solutions of the whole problem.

In other words, an optimal solution to a problem can be constructed from the optimal solutions to its smaller subproblems. This is known as optimal substructure.

For example, consider the fractional knapsack problem again.

        Items	Available Weight	Total Value
        Gold	10 units	        $5000
        Wheat	20 units	        $1000
        Oil	    14 units	        $1400

After we have taken 10 units of Gold, we now approach the rest of the problem like a fractional knapsack problem of capacity 15 units and only Wheat and Oil as the available loot.

This means that the subproblem is itself a fractional knapsack problem. So, if we construct an optimal solution to each of the subproblems, we'll get the optimal solution to the problem.

~ 1 Knapsack Problem
Now we have to address why we didn't get the optimal solution to the 0-1 knapsack with our greedy approach.

        Item	    Weight	    Total Value
        TV	        30 units	$3000
        Laptop	    20 units	$2000
        Weight	    15 units	$1500

Here, The capacity of the knapsack is 35 units.

Here, choosing TV with the highest value early on prevents you from fitting in multiple items with a slightly lower value-to-weight ratio but a higher combined value later.

So, to get the optimal solution, we had to consider the impacts your current choice will have on future choices. Hence, the 0-1 knapsack problem doesn't satisfy the greedy choice property.

This is why we didn't get the optimal solution through a greedy approach for the 0-1 knapsack problem.

However, it's worth noting that every subproblem for 0-1 knapsack is itself a 0-1 knapsack problem.

So 0-1 knapsack also has the optimal substructure.

'"'Greedy Choice Property is about making a 'best' choice in each step without reconsidering it later. In the 0-1 knapsack problem, choosing items based only on high value-to-weight ratio in the initial stages can prevent from making better choices later.'"'

'"'Greedy Choice Property is satisfied when each decision can be made independently, without having to reconsider previous choices. In the fractional knapsack problem, we can take any fraction of items, thus making the choices independent.'"'

'"' Once an item has been chosen and some capacity filled, the remaining capacity must be filled optimally as well, hence forming a subproblem of the same type, be it 0-1 or fractional knapsack.'"'

~ Takeaway
In conclusion, a greedy approach can yield optimal solutions to only those problems that possess greedy choice properties and exhibit optimal substructure.

The first three problems satisfied them both, whereas the 0-1 knapsack problem didn't.

However, there is a silver lining to this—the 0-1 knapsack has an optimal substructure, which can be exploited by dynamic programming to yield an optimal solution.

In practice, the greedy approach is ideal for quick, simple solutions, but it doesn't guarantee optimal results in all cases. For optimal outcomes, dynamic programming (DP) and backtracking are often used.

But that is a topic for another day. For now, let's focus on the positives and then discuss popular algorithms that provide optimal solutions to problems using a greedy approach.

~ Advantages of Greedy Algorithms
In spite of their glaring flaw, greedy algorithms are still one of the most preferred classes of algorithms in computer science thanks to the multiple advantages they provide. Some of these advantages are:

- Simplicity
Greedy algorithms are often straightforward to design and implement, making them a practical choice for solving many problems.

- Time Efficiency
Greedy algorithms are generally efficient in terms of time complexity, often providing fast solutions to problems.

- Space Efficiency
Greedy algorithms typically require minimal memory usage, making them suitable for situations with limited memory resources.

- Intuitive Approach
Greedy algorithms follow a natural, intuitive approach by making locally optimal choices at each step. This makes it easy to understand and analyze.

- Heuristic Solutions
The greedy approach is heuristic, which means it advances toward a solution through trial and error or following loosely defined rules.

Even when not guaranteed to find the optimal solution, greedy algorithms often provide good solutions that are close to the optimal solution.

~ Examples of Greedy Algorithms
Several popular and powerful algorithms provide the optimal solution using a greedy approach, most of them being widely used with graph data structure.

Some of the most common ones are:
    * Dijkstra's Algorithm
    * Prim's Algorithm
    * Kruskal's Algorithm
    * Ford Fulkerson Algorithm

We have already discussed all these algorithms in detail in our lesson on Graph-Based Algorithms, so there's no need to elaborate further.
'''