#.............Example: Generating Table of Contents
# A table of contents makes navigating through a textbook so much easier. Did you know trees were used to create such TOC in computers?

# Let's see how it's done.

# First of all, we need to create a tree containing all the chapters, sections, and sub-sections in an organized manner.

# In our tree,
#     *Chapters will be the children of the entire book.
#     *Sections will be the children of chapters.
#     *Sub-sections will be the children of sections.

# The child nodes will carry the numbers of all of their ancestors as suffixes in their names.

# For example, a sub-section will be named 1.1.2 to denote it's the second child of section 1, which, in turn, is the first child of chapter 1.

# So our tree will look like this:
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.10.png

# Now what if we applied preorder traversal to this tree? The elements will appear in the following order:
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.11.png

# This already looks like a TOC but doesn't look the part visually: it's lacking the proper indentation for the sections and sub-sections.

# So, how can we add them?

# Remember the concept of levels we studied earlier? We can get the appropriate indentation by adding spaces proportional to the level of the elements in the tree.

# Since Book is the root node at level 0, no indentation will be added. For chapters at level 1, one indentation will be added.

# Similarly, the sections at level 2 will have 2 indentations added to them, and finally, the subsections at level 3 will have 3 indentations added to them.

# This will give us something like this:
# https://cdn.programiz.pro/course-images/dsa-with-python/dsa-10.4.12.png


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root = None):
        self.root = root

    def get_toc(self, node = None, level = 0):
        if not node:
            node = self.root
        print(level)
        print(' ' * level, node.data)
        for child in node.children:
            self.get_toc(child, level + 1)
        

# create the root node
root = TreeNode("Book")

# creating the children of root
child1 = TreeNode("Chapter 1")
child2 = TreeNode("Chapter 2")

# creating sections
child1_1 = TreeNode("Section 1.1")
child1_2 = TreeNode("Section 1.2")
child2_1 = TreeNode("Section 2.1")
child2_2 = TreeNode("Section 2.2")

# create the sub-sections
child1_1_1 = TreeNode("Sub-Section 1.1.1")
child1_1_2 = TreeNode("Sub-Section 1.1.2")
child1_2_1 = TreeNode("Sub-Section 1.2.1")
child1_2_2 = TreeNode("Sub-Section 1.2.2")

child2_1_1 = TreeNode("Sub-Section 2.1.1")
child2_1_2 = TreeNode("Sub-Section 2.1.2")
child2_2_1 = TreeNode("Sub-Section 2.2.1")
child2_2_2 = TreeNode("Sub-Section 2.2.2")


# add chapters to the root node
root.add_child(child1)
root.add_child(child2)

# add sections to chapter1
child1.add_child(child1_1)
child1.add_child(child1_2)

# add sections to chapter2
child2.add_child(child2_1)
child2.add_child(child2_2)

# add subsections to section 1_1
child1_1.add_child(child1_1_1)
child1_1.add_child(child1_1_2)

# add subsections to section1_2
child1_2.add_child(child1_2_1)
child1_2.add_child(child1_2_2)

# add subsection to section2_1
child2_1.add_child(child2_1_1)
child2_1.add_child(child2_1_2)

# add subsection to section2_2
child2_2.add_child(child2_2_1)
child2_2.add_child(child2_2_2)
# creating our tree
tree = Tree(root)

# print the TOC
tree.get_toc()