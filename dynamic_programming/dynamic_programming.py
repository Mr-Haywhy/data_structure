'''
~ What is Dynamic Programming?
Dynamic Programming (DP) is a method for solving complex problems by breaking them into smaller overlapping subproblems.

By solving each subproblem only once and storing its result, DP avoids redundant computations, making it highly efficient for specific types of problems.

Real-Life Analogy
Imagine you're planning a road trip and want to visit several cities with the least cost. You might:

Calculate the cost of all routes from your starting city to the next city.
Store the cheapest cost to each city.
Reuse this information as you calculate costs to subsequent cities.
This approach mirrors DP — solve small parts (subproblems), store their results, and reuse them.

~ Why Dynamic Programming?
Dynamic programming is essential for solving problems with:

1. Overlapping Subproblems
These are problems where the same problem is solved multiple times.

2. Optimal Substructure
In such problems, the optimal solution of the problem can be constructed from the optimal solutions of its subproblems.

Since we've already dealt with these concepts in the Greedy Algorithms chapter, we'll only do a short recap to refresh your memory.

~ Overlapping Subproblems Property
Sometimes, the same subproblem occurs multiple times during the computation of a larger problem. Such problems are known as overlapping subproblems.

Dynamic programming frees us from the need of solving these subproblems each and every time. Instead, you can just save the solution and reuse it when you face the subproblem again.

By reusing previously computed results, you reduce the redundancy and enhance performance.

Real-Life Analogy
Imagine preparing dinner, where multiple dishes in your menu require chopped onions.

Instead of chopping onions separately each time you prepare a dish, you prepare a batch in advance and use them whenever needed.

As a result, you save a lot of time and effort, which is just like reusing computed results.

~ Optimal Substructure Property
Optimal substructure refers to the principle that the solution to a problem can be constructed efficiently from the solutions to its subproblems.

In dynamic programming, the optimal substructure property guides us to break down complex problems into manageable subproblems, allowing us to build up a solution efficiently by combining smaller solutions.

Real-Life Analogy
Think of constructing a complex Lego structure. Each small Lego piece represents a solution to a subproblem. By efficiently assembling these pieces, you create the entire intricate structure.

Now that you have some idea about dynamic programming, let's see how we can implement it.

But first, take some quizzes!

~ Practice Challenge: Pairs That Add Up to a Target
Let's begin with a simple problem to get accustomed to the ways of dynamic programming.

Problem: Given an array of integers and a target sum, find all pairs that add up to the target.

For example, suppose you need to find the first number pair in [0, 2, 5, 7, 8, 9, 10] that add up to 11.

The simplest way to approach this problem would be to use two loops and check the sum of each pair of numbers.

def find_pair_of_numbers(list1, target):
    for i in list1:
        for j in list1:
                if i != j and i + j == target:
                    return i, j

list1 = [0, 2, 5, 7, 8, 9, 10]
target = 11

n1, n2 = find_pair_of_numbers(list1, target)
print(n1, n2)

Output:
    2 9
'''
    
def find_pair_of_numbers(list1, target):
    for i in list1:
        for j in list1:
                if i != j and i + j == target:
                    return i, j

list1 = [0, 2, 5, 7, 8, 9, 10]
target = 11

n1, n2 = find_pair_of_numbers(list1, target)
print(n1, n2)

'''
While we get our required output, we can see that we perform many redundant operations. For example,
    * The algorithm first checks if 0 + 2 equals 11 (it doesn't).
    * Later, it checks if 2 + 0 equals 11, which again isn't the case.

This redundancy grows with the size of the list, making the approach computationally expensive for larger datasets.

Let's see how we can solve this using a dynamic programming approach called memoization.

~ Memoization
Memoization focuses on avoiding redundant calculations by storing previously computed results.

Real-Life Analogy
Think of memoization as having a notebook to jot down answers to math problems you've already solved.

When faced with the same problem again, you can simply check your notebook instead of redoing the math.

We'll learn this concept by making certain changes to the code we wrote on the previous page.

~ Thought Process: Memoization
We'll modify the previous program by using a set to store numbers we've already seen. Here's the step-by-step breakdown of the program:

1. First, we'll define an empty set for numbers that have already been seen or observed.

        seen = set()

2. Next, we'll store each number i in the list to the seen set.

        seen.add(i)

3. Finally, for each number i , we'll check if target - i is in the seen set.

        if target - i in seen:
            return target - i, i

If target - i is in seen, we don't need to check any further since we simply know i and target - i add up to the target.
'''

def find_pair_of_numbers(list1, target):
    # initialize an empty set
    seen = set()

    for i in list1:
        if target - i in seen:
            return target - i, i
        seen.add(i)

list1 = [0, 2, 5, 7, 8, 9, 10]
target = 11

n1, n2 = find_pair_of_numbers(list1, target)
print(n1, n2)

'''
Output:
    2 9

Starting with an empty set seen, here's how the program iterates through the list:

i	 |   target - i	 |   Action
0	 |   11 - 0 = 11 zzzzzzz|   Since 11 isn't in seen, add 0 to seen.
2	 |   11 - 2 = 9	 |   Since 9 isn't in seen, add 2 to seen.
5	 |   11 - 5 = 6	 |   Since 6 isn't in seen, add 5 to seen.
7	 |   11 - 7 = 4	 |   Since 4 isn't in seen, add 7 to seen.
8	 |   11 - 8 = 3	 |   Since 3 isn't in seen, add 8 to seen.
9	 |   11 - 9 = 2	 |   Since 2 is in seen, return (2, 9).

~ Pros and Cons of the Optimized Approach
Advantage: Reduced Time Complexity
The optimized approach eliminates the need for nested loops. Instead, it processes the list in a single pass, making the time complexity O(n).

Acceptable Disadvantage: Increased Space Complexity
The seen set requires additional space proportional to the size of the list. However, this tradeoff is often acceptable for the gain in performance.

In the next lesson, we'll reinforce the concepts we've just learned using the Fibonacci series.
'''