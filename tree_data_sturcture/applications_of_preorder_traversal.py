#..............Applications of Preorder Traversal.............
# Preorder traversal is useful for tasks requiring parent node action before processing the children. Therefore, it's used in:

# 1. Cloning a Tree
# Preorder traversal is the go-to method for cloning a tree. When we print a node right after visiting it, we get an instant copy of the given tree.

# The primary purpose of cloning a tree is to help in backup systems and security.

# 2. Serialization
# Trees can be serialized (converted into a string) and deserialized (converted back to a tree) using preorder traversal, allowing them to be stored in databases or sent across networks.

# It allows us to recreate the same tree structure at a later point in time or in a different computing environment.