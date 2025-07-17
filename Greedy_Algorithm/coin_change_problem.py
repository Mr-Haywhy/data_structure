'''
~ Problem Statement
Suppose you are given an infinite supply of coins of values $1, $5, $10, and $25.

Now, you have to give $62 to a friend using the fewest number of coins possible.

So, how do we solve this problem greedily?

~ Defining the Greedy Logic
The greedy approach to solving this problem has the following steps involved.
    * Start by choosing the largest coin denomination that can be used without exceeding the amount needed.
    * Now, update the amount to be paid by subtracting the value of the coin just used.
    * Repeat this process until the amount becomes zero.

~ Solving the Problem
Here, the amount to be paid is

        Total = 62

In order to solve the problem, let's use the following table:

        Coins       Count
        $25	        0
        $10	        0
        $5	        0
        $1	        0

Now let's choose the coin with the highest value that is less than or equal to this amount, which is $25.

So, we can use two $25 coins, and our remaining amount is

        Total = 62 - (2 * 25) = 12

So, our updated table is

        Coins	    Count
        $25	        2
        $10	        0
        $5	        0
        $1	        0

Now, the coin with the highest value less than or equal to the remaining amount is $10.

        Total = 12 - 10 = 2

        Coins	    Count
        $25	        2
        $10	        1
        $5	        0
        $1	        0

Now, the coin we choose is $1, and since we are $2 down the amount, we take two of these.

        Coins	    Count
        $25	        2
        $10	        1
        $5	        0
        $1	        2

Thus, we ended up using a total of five coins in order to collect $62.

Now, let's try implementing this in Python.
'''

"""
~ Thought Process
We can implement the solution to the coin change problem in the following steps.

1. Get the coins and target value.

        # define the coin denominations and the target value
        coins_denomination = [1, 5, 10, 25]
        target_value = 62

2. Define the function to get the coins.

        def coin_change(coins_denomination, target_value):

3. Sort the coins in descending order.

        coins_denomination.sort(reverse=True)

4. Choose the coin of the highest denomination less than or equal to the target.

        for coin in coins_denomination:

            # check if coin is less than or equal to remaining target value
            if target_value >= coin:

                # determine the number of coins of this denomination.
                count = target_value // coin

                # update the remaining target value.
                target_value =  target_value % coin

            # store the coin and its count
            coin_count.append((coin, count))
                
We first choose the coin with the highest value that is less than or equal to the target value and count how many coins of this denomination we need.

We update the remaining target value for every coin we select.

5. Iterate until we reach the target value.

        # see if the coins sum up to the desired target value
        if target_value == 0:
            return coin_count
        return None

We repeat the above process until the value reaches zero, which means we have obtained our target.
"""

# Source Code

# define the coin denominations and the target value
coins_denomination = [1, 5, 10, 25]
target_value = 62

def coin_change(coins_denomination, target_value):
    
    # sort the coins in descending order
    coins_denomination.sort(reverse=True)
    
    # initialize variables.
    coin_count = []
    
    
    for coin in coins_denomination:

        # check if coin is less than or equal to remaining target value
        if target_value >= coin:

            # determine the number of coins of this denomination
            count = target_value // coin

            # update the remaining target value.
            target_value =  target_value % coin

            # store the coin and its count.
            coin_count.append((coin, count))
            
    # see if the coins sum up to the desired target value
    if target_value == 0:
        return coin_count
    return None

# target_value = int(input())   # If we want to take the target value from the user
coin_count = coin_change(coins_denomination, target_value)

if coin_count:
    for coin, count in coin_count:
        print(f"Use {count} coins of ${coin}")


'''
Output:
    Use 2 coins of $25
    Use 1 coins of $10
    Use 2 coins of $1
'''

'''
~ Time Complexity
The code's time complexity mainly comes from sorting the coin denominations at the start, which is O(nlogn), where n represents the number of different coins.

Although there's also a loop that adds O(m) complexity (where m is the count of coin types), it's usually less significant than the sorting step, particularly if there aren't many coin types.

Time Complexity: O(nlogn)
'''