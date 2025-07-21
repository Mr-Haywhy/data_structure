'''
~ Introduction
In a Fibonacci series, each number is the sum of the previous two numbers. Also, the first two numbers are always 0 and 1.

The Fibonacci series containing the first six terms is given below:

        0, 1, 1, 2, 3, 5

Mathematically,

        Fibonacci(n) = Fibonacci(n - 1) + Fibonacci(n - 2)

Additionally, Fibonacci(0) = 0 and Fibonacci(1) = 1.

Let's see how we can calculate the 5th term of the Fibonacci series using different methods.

~ Fibonacci Series Using Recursion
You probably know the recursive implementation of the Fibonacci series. Consider the code below, which prints the nth term of the Fibonacci series:

        def Fibonacci(n):
            if n == 0 or n == 1:
                return n
            else:
                return Fibonacci(n - 1) + Fibonacci(n - 2)


        # Get the 5th Fibonacci term
        result = Fibonacci(4)
        print(result)

Here's how this program works:

    * First, Fibonacci(4) calls Fibonacci(3) and Fibonacci(2).
    * Fibonacci(3) requires two values: Fibonacci(2) and Fibonacci(1).
    * Similarly, Fibonacci(2) requires Fibonacci(1) and Fibonacci(0).
    * Since Fibonacci(1) and Fibonacci(0) are the base cases, they return 1 and 0 respectively.

Once the base conditions return their values, each preceding call also starts returning values as shown in the figure below.
        Fibonacci(4)
        ├── Fibonacci(3)
        │   ├── Fibonacci(2)
        │   │   ├── Fibonacci(1) = 1
        │   │   └── Fibonacci(0) = 0
        │   └── Fibonacci(1) = 1
        └── Fibonacci(2)
            ├── Fibonacci(1) = 1
            └── Fibonacci(0) = 0
The final result is 3, which is the 5th term of the Fibonacci series.

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.2.1.png

Here,
    * FIbonacci(2) is called twice.
    * Fibonacci(1) is called thrice.
    * Fibonacci(0) is called twice.

As you can see, this method does a lot of repeated work. Let's see how dynamic programming addresses this issue.


~ Fibonacci Series Using Memoization
Dynamic programming solves the redundancy issue by storing results of previously computed subproblems.

Here's how it works:
    1. Store Previous Results: Use a dictionary to store Fibonacci numbers that have already been computed.
    2. Check Before Computing: Before performing any calculation, check if the result is already available in the storage.
    3. Compute Only Once: If the result isn't available, compute it and store it for future use.

This approach ensures each subproblem is solved only once.

~ Fibonacci Series Using Memoization
Here's how we can generate the Fibonacci series using memoization.

        def Fibonacci(n):
            # If we already have the result, just use it
            if n in fib:
                return fib[n]
            # Otherwise compute
            fib[n] =  Fibonacci(n - 1) + Fibonacci(n - 2)
            return fib[n]
            
        # Initialize a dictionary to store different results
        fib = {0:0, 1:1}

        result = Fibonacci(4)
        print(result)

Next, we'll see how this code works.

~ Working: Fibonacci Series Using Memoization
Here's how the previous code works:

1. The dictionary fib is initialized with the base cases.

        # Fibonacci(0) = 0
        # Fibonacci(1) = 1
        fib = {0:0, 1:1}

2. Fibonacci(4) is called.
When we call Fibonacci(4), it first checks if key 4 is in the fib dictionary.

Since key 4 is not present, its value (fib[4]) is calculated as:

        fib[4] = Fibonacci(3) + Fibonacci(2)

As a result, Fibonacci(4) ends up calling Fibonacci(3).
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.2.2.png

Remember: In each recursive call of Fibonacci(n-1) + Fibonacci(n-2), the function call on the left, i.e., Fibonacci(n-1), is always called first.

3. Fibonacci(3) is called.

Again, the code checks if key 3 is in fib. Since it's not, fib[3] is calculated it as

        fib[3] = Fibonacci(2) + Fibonacci(1)

Then, Fibonacci(2) is called.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.2.3.png

4. Fibonacci(2) is called.

Since key 2 is not in fib, the value fib[2] is calculated it as

        fib[2] = Fibonacci(1) + Fibonacci(0)

Then, Fibonacci(1) is called.
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.2.4.png

5. The base cases are reached.

Since Fibonacci(1) is a base case whose value is stored in fib, it returns 1 (i.e. fib[1]) to Fibonacci(2).
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.2.5.png

Then, Fibonacci(2) calls Fibonacci(0), which is another base case. As a result, it returns 0 to Fibonacci(2).

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.2.6.png

6. The return value of Fibonacci(2) is stored in the dictionary.

Now, Fibonacci(2) finally calculates the dictionary value fib[2]:

        fib[2] = Fibonacci(1) + Fibonacci(0)
        fib[2] = 1 + 0
        fib[2] = 1

This value is then returned to Fibonacci(3).

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.2.7.png

7. Return to Fibonacci(3) and repeat the process.

Now, we return to Fibonacci(3), which finally calls Fibonacci(1).

But Fibonacci(1) is a base case, so its value is directly returned to Fibonacci(3).

Thus, Fibonacci(3) now calculates (and stores) the dictionary value fib[3] and returns it to Fibonacci(4).

        fib[3] = Fibonacci(2) + Fibonacci(1)
        fib[3] = 1 + 1
        fib[3] = 2

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.2.8.png

8. Return to Fibonacci(4) and repeat the process.

The program then returns to Fibonacci(4), which finally calls Fibonacci(2).

But the return value of Fibonacci(2) is already stored in the dictionary. So we use that value directly to calculate fib[4]:

        fib[4] = Fibonacci(3) + Fibonacci(2)
        fib[4] = 2 + 1
        fib[4] = 3

https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.2.9.png

This return value of Fibonacci(4) is then printed to the screen.

~ Memoization vs. Basic Recursion
If we compare our optimized program to the recursive call tree, the following function calls are omitted:
https://cdn.programiz.pro/course-images/dsa-with-python/dsa-20.2.10.png

Thus, memoization has a clear edge over the recursion-only approach.

~ Issues with Fibonacci Series Using Memoization
In memoization, we store the answers we find so we don't have to redo unnecessary work. This is an improvement over our recursive approach.

However, we have to remember that the code stores each result in a dictionary, which may not seem significant when we are computing only the fifth Fibonacci number. After all, it's just five key-value pairs.

But what if you wanted to find the 1000th Fibonacci number? Would you create a dictionary of size 1001?

Another dynamic programming approach, particularly well-suited to this problem, involves reusing a limited set of variables to update the results iteratively.

This technique is known as tabulation and it optimizes space by maintaining only the most recent values needed for computation. We'll discuss this next.

~ Tabulation
Tabulation involves creating a table and filling it with solutions to smaller problems. These solutions will help you solve bigger problems step by step. It's like climbing up a ladder, or solving simpler puzzles before conquering the bigger one.

Hence, it's referred to as the bottom-up approach.

Let's see how we can use this to solve the Fibonacci Series.

~ Fibonacci Series Using Tabulation
In the Fibonacci series, each number is the sum of the last two numbers. So, we just need two variables to calculate any Fibonacci number.

For this, instead of starting with n, we start with the first two Fibonacci numbers and build up the solution.

def Fibonacci(n):

    # Start with first two numbers
    fib1, fib2 = 0, 1

    # Build up the solution
    for i in range(n):
        # Next number is sum of the last two     
        fib1, fib2 = fib2, fib1 + fib2
    return fib1

for i in range(5):
    print(Fibonacci(i))


Here's how the variables update across each iteration.

Iteration (i)	fib1 (Output)	    fib2 
    0	            0	            1
    1	            1	            1
    2	            1	            2
    3	            2	            3
    4	            3	            5
Here, we used only two variables to get the next term in the Fibonacci sequence by updating them in each iteration.

It's super efficient and only needs a small amount of memory.

NOTE: Tabulation usually involves filling a table to store the results of all subproblems, which are then combined to solve the main problem. Don't worry if you can't fully grasp this concept; we'll cover it in detail in the 0-1 Knapsack section.

~ Comparing the Approaches
Let's break down the time and space complexities for each of the three approaches:

Approach/Complexity	    Time Complexity	    Space Complexity
General Recursive Approach	O(2^n)	            O(n)
Memoization Approach	    O(n)	            O(n)
Tabulation Approach	        O(n)	            O(1)

As can be seen, tabulation works best when tackling the Fibonacci series. However, this doesn't mean tabulation works best every time.

The choice between tabulation and memoization depends on the problem at hand. Let's create some guidelines to see where each method can be preferred.

~ Tabulation vs. Memoization
Going off on the previous example alone, it might seem tabulation outperforms memoization in all cases. But that's not true.

When to use memoization?
Memoization (top-down approach) is used when solving problems recursively, storing results of subproblems as needed to avoid redundant calculations.

It works well when only a few subproblems need to be computed.

When to use tabulation?
Tabulation (bottom-up approach) is used when solving problems iteratively, building solutions for all subproblems systematically.

It is more efficient for problems where all subproblems need to be solved, as it avoids recursion overhead.

NOTE: Recursion overhead refers to the additional computational and memory costs incurred when using recursion instead of iteration. It arises because the system maintains a separate stack frame for each recursive call.

~ Thinking Dynamically
Before proceeding further, it's important to remember that dynamic programming is a way of thinking and is not limited to a particular algorithm. All of these concepts will make sense as you practice multiple problems.

But an in-depth exploration of such problems is not within the scope of this course. As such, we'll include dedicated courses for dynamic programming in the near future.

For now, we'll conclude this chapter by finally finding the optimal solution to the 0-1 Knapsack problem we discussed in Greedy Algorithms.
'''
