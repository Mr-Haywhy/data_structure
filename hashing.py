#.......................Hashing.............................#
Hashing is the process of transforming data, such as text, numbers, and files, into a unique string of characters and numbers.
The data we are trying to convert is referred to as a key.
The string we get after hashing is known as a hash value or hash code.

.........................Hash function........................
The function used to convert keys into hash values is called a hash function.

Let's start with a simple example of a hash function:

        H(x) = x mod 5
Here:
    1. x is the key
    2. H(x) is the hash function, which gives the remainder when x is divided by 5.

Suppose we have these keys: 2, 9, 10.
    * The hash value of 2 will be 2.
    * The hash value of 9 will be 4.
    * The hash value of 10 will be 0.

In hashing, we create a hash table (a data structure) to store keys and their respective hash values.

........................Hash Table...........................
Here's what a hash table looks like for the previous example.

            Hash Value  | Key
                0       | 10
                1       |
                2       | 2
                3       |
                4       | 9

Our function H(x) = x mod 5 creates unique hash values for 10, 2, and 9 keys.

However, it might not create unique hash values for a different set of keys. We will learn to handle this problem later in this chapter.

For now, let's examine another example of hashing.
