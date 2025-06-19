# .......................Introduction.....................
# Huffman coding is an algorithm designed for data compression. This technique uses binary trees to reduce the size of data.

# It's the underlying mechanism in popular compression formats like GZIP and BZIP2.

# .......Why is compression necessary?

# When transmitting or storing large files, the absence of compression can lead to high costs and inefficiencies.

# Suppose we have a string with some repeated characters.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.1.png

# Each character in the string uses 8 bits.

# For 15 characters, that's 120 bits total which is a lot of space.

# As there are recurring characters in the string, we can reduce the size based on the frequency of each character. This can be accomplished using Huffman coding.

# Next, we will implement Huffman coding to compress a string.

# ...............Working of Huffman Coding.................
# Suppose we have the string BCAADDDCCACACAC.
# The string contains 15 characters, which is 120-bit.

# We'll use Huffman coding to shrink the string in a few steps:

# 1. Find the occurrence of each character.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.2.png

# 2. Sort the characters by frequencies.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.3.png

# 3. Update Huffman Tree
# Now, we will update a tree where the first two elements (elements with the lowest frequencies) are the child nodes and the sum of their frequency is the root node.

# Example: For elements B and D with frequencies 1 and 3 respectively, the sum is 4.

# While creating the tree, we'll keep the character with the lower frequency to the left and the one with higher frequency to the right.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.4.png

# NOTE: The root node of each subtree will have no key, only a value.

# 4. Repeat steps 2 and 3 till every element is integrated into a tree.

# Let's add the character A to the tree.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.5.png

# Finally, we'll add C to the tree.

# Since the frequency of C (i.e 6) is less than 9, we'll add this character to the left of the tree.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.6.png

# We now have a single connected tree structure. Thus, our Huffman tree is created.

# ....................Encoding the Message..............
# To encode the message using the Huffman tree we just created, we assign the right edges with a weight of 1 and the left edges with the weight of 0.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.7.png

# Now we'll find the Huffman code of each character.

# For that, we need to traverse from the root to the leaf node with the character as the key.

# For example,

# If we wanted to get the Huffman code for A, we must traverse from root node to the leaf node with the key A.
    
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.8.png

# Since we took two right edges to reach the node, our Huffman code for A is 11.

# The code of each character and total size is given by the table below.

# Character	Frequency	Code
#     A	        5       11
#     B	        1	    100
#     C	        6	    0
#     D	        3	    101

# Message: BCAADDDCCACACAC

# Huffman Code: 1000111110110110100110110110

# Before encoding, the total size of the string was 120 bits. After encoding, the size is reduced to 28 bits.


# .....................Decoding the Code.....................
# If we refer to the previous page, we have:

# Message: BCAADDDCCACACAC

# Huffman Code: 1000111110110110100110110110

# The Huffman code of each character was:

# Character	Frequency	Code
#     A	        5	    11
#     B	        1	    100
#     C	        6	    0
#     D	        3	    101

# Now, let's decode the first six bits of the code, 100011, for ease.

# Step I

# We start from the root node, 15.

# Since the first Huffman code is 1, we reach 9. Since it's not a character, we go to the next bit.

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.9.png

# Step II
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.10.png

# As our next character is 0, we move to the left and reach 4.

# Since this is not a character, we go to the next bit.

# Step III

# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.11.png

# Again, the next character is 0, we move left again and reach B.

# Since we have found a character, we'll decode the weights. Meaning, 100 code is the character B.

# Step IV
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.12.png

# After finding a character, we return to the root and begin our process again.

# As the next code to be decoded is 0, we move left and arrive at C our first go.

# So now we decode 0 as C.

# Step V
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.13.png

# After retrieving C, we return back to the root and restart the process.
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-11.6.14.png

# We repeat this process again from the root and the next time we have arrived at a A, we will with the weights 11.

# So, we recover A and return back to the root.

# If we repeat this process for the entire coded string, we will regain our original string.

# Now you have a proper understanding of Huffman coding. Next, we will see how we can implement it with code.


# .....................Thought Process: Building the Huffman Tree...............
# The first step in Huffman coding is to build our Huffman tree.

# As you might have noticed, our final Huffman tree was a full binary tree. So, we can get our Huffman tree with additions to our code from a binary tree in the following steps.

# We will create the HuffmanTreeNode class. This is similar to the BinaryTreeNode class from the previous lesson.

#         class HuffmanTreeNode:
#             def __init__(self, data, freq):
#                 self.data = data
#                 self.freq = freq
#                 self.left = None
#                 self.right = None

#             def add_left_child(self, node):
#                 self.left = node

#             def add_right_child(self, node):
#                 self.right = node

# As we need to store their characters and their frequency of repetition as well, we have added an additional attribute freq to our node.

# So in our code:
# *data: stores the character
# *freq: stores the frequency of repetition of the character

# We'll now create another class HuffmanTree to handle all our tree operations

# 1. Create the Huffman Tree
# Let's create a method named build_huffman_tree() to create a Huffman tree. This method will:
# * Count the frequency of each character.
# * Sort the nodes in the list.
# * Combine the first two nodes to form a tree .
# * Repeat 2 and 3 till the list has a single Huffman tree.

#             def build_huffman_tree(self, s):
#                 # count the frequency of each character
#                 freq_map = {char:s.count(char) for char in s}
                    
#                 huffman_tree = [HuffmanTreeNode(char, freq) for char, freq in freq_map.items()]
                    
#                 # build Huffman Tree 
#                 while len(huffman_tree) > 1:
#                     # sort characters based on their frequencies in ascending order
#                     huffman_tree = sorted(huffman_tree, key=lambda x: x.freq)
                        
#                     # pop the first two nodes 
#                     left = huffman_tree.pop(0)
#                     right = huffman_tree.pop(0)
                        
#                     # merge the nodes
#                     merged_freq = left.freq + right.freq
#                     merged_node = HuffmanTreeNode(None, merged_freq)
#                     merged_node.add_left_child(left)
#                     merged_node.add_right_child(right)
                        
#                     # add the merge node to the tree
#                     huffman_tree.append(merged_node)

#                 self.root = huffman_tree[0]


# This entire process is repeated until our complete Huffman tree is obtained.

# ........................Thought Process: Generating Huffman Codes............
# Now that we have our Huffman tree ready, we can now generate the Huffman codes for characters of a given string.

# We begin generating Huffman codes from the root of the tree. During traversal, we use two main variables to track each character's Huffman code.
# * code: A string tracking the Huffman code during root-to-node traversal, starting empty and appending 0 for every left or 1 for every right traversal.
# * huffman_code_map: A dictionary linking characters to their Huffman codes, updated when leaf nodes are identified.

# We will no recursively traverse from the root node to the particular leaf node where:
# * Every time we move right from a node we add 1 to the code.
# *And every time we move left from a node, we add 0 to the code.

# We'll do this until we reach the leaf node.

#         def generate_codes(self, node=None, code="", huffman_code_map={}):
#             if not node:
#                 node = self.root

#             # if it's a leaf node, store the code
#             if node.data:
#                 huffman_code_map[node.data] = code
#                 return huffman_code_map

#             # traverse left and right
#             self.generate_codes(node.left, code + "0", huffman_code_map)
#             self.generate_codes(node.right, code + "1", huffman_code_map)

#             return huffman_code_map


# Once we have obtained the Huffman codes, we can simply replace the characters with their respective code.

#         def encode(self, s, huffman_codes):
#             return ''.join([huffman_codes[char] for char in s])
        



# .............................Source Code: Generating Huffman Codes............................
class HuffmanTreeNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def add_left_child(self, node):
        self.left = node

    def add_right_child(self, node):
        self.right = node

class HuffmanTree:
    def __init__(self, root=None):
        self.root = root

    def build_huffman_tree(self, s):
        # count the frequency of each character
        freq_map = {char:s.count(char) for char in s}
        
        huffman_tree = [HuffmanTreeNode(char, freq) for char, freq in freq_map.items()]
        
        # build Huffman Tree 
        while len(huffman_tree) > 1:
            # sort characters based on their frequencies in ascending order
            huffman_tree = sorted(huffman_tree, key=lambda x: x.freq)
            
            # pop the first two nodes 
            left = huffman_tree.pop(0)
            right = huffman_tree.pop(0)
            
            # merge the nodes
            merged_freq = left.freq + right.freq
            merged_node = HuffmanTreeNode(None, merged_freq)
            merged_node.add_left_child(left)
            merged_node.add_right_child(right)
            
            # add the merge node to the tree
            huffman_tree.append(merged_node)

        self.root = huffman_tree[0]

    def generate_codes(self, node=None, code="", huffman_code_map={}):
        if not node:
            node = self.root

        # if it's a leaf node, store the code
        if node.data:
            huffman_code_map[node.data] = code
            return huffman_code_map

        # traverse left and right
        self.generate_codes(node.left, code + "0", huffman_code_map)
        self.generate_codes(node.right, code + "1", huffman_code_map)

        return huffman_code_map
    
    def encode(self, s, huffman_codes):
        return ''.join([huffman_codes[char] for char in s])


# test huffman tree
s = "BCAADDDCCACACAC"
tree = HuffmanTree()
tree.build_huffman_tree(s)

# test huffman code
huffman_codes = tree.generate_codes()
for char, code in huffman_codes.items():
    print(f"{char}: {code}")

# test encoding
encoded_string = tree.encode(s,huffman_codes)
print(f"Encoded string for '{s}': {encoded_string}")



# Output:
    # C: 0
    # B: 100
    # D: 101
    # A: 11
# Encoded string for 'BCAADDDCCACACAC': 1000111110110110100110110

# We generated the code of each character in the string BCAADDDCCACACAC using Huffman coding.


# .................Complexity Analysis of Huffman Coding.......................
# The time complexity of using Huffman coding to compress a given string is: 
# O(n+m^2 logm), where:
#     n is the number of characters in the input text.
#     m is the number of unique characters in the input text.