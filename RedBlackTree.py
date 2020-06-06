'''
Insertion in Red Black Tree

Rules for a RBT:

All nodes have a color
All nodes have two children (use NULL nodes)
All NULL nodes are colored black
If a node is red, its children must be black
The root node must be black (optional)    (not implemented in this code)
We'll go ahead and implement without this for now
Every path to its descendant NULL nodes must contain the same number of black nodes
'''


class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

    def __repr__(self):
        print_color = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, print_color)

def grandparent(node):
    if node.parent == None:
        return None
    return node.parent.parent

# Helper for finding the node's parent's sibling
def uncle(node):
    p = node.parent
    gp = grandparent(node)
    if gp == None:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left


class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def __iter__(self):
        yield from self.root.__iter__()

    def insert(self, new_val):
        newnode = self.insert_helper(self.root, new_val)
        self.rebalance(newnode)

    def insert_helper(self, curr_node, new_val):       #Basic BST insertion
        if new_val < curr_node.value:                  # if new node is less than current node go left and search till you reach empty child
            if curr_node.left:
                return self.insert_helper(curr_node.left, new_val)
            else:
                curr_node.left = Node(new_val, curr_node, 'red')
                return curr_node.left

        else:
            if new_val > curr_node.value:       # if new node is greater than current node go right and search till you reach empty child
                if curr_node.right:
                    return self.insert_helper(curr_node.right, new_val)
                else:
                    curr_node.right = Node(new_val, curr_node, 'red')
                    return curr_node.right


    def rebalance(self,node):
        # Case 1: if inserted node is a root node
        if node.parent is None:
            return

        # Case 2:  If parent of an inserted node is black no change required
        if node.parent.color == 'black':
            return

        # if it did not pass previous if we know parent is red
        # Case 3: if parent and uncle both are red

        if uncle(node) and uncle(node).color == 'red':
            uncle(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            return self.rebalance(grandparent(node))

        gp = grandparent(node)
        if gp is None:
            return

        # Case 4: The newly inserted node has a red parent, but that parent has a black sibling
        # Also, both the parent of node and node parent are on different sides (LR and RL violations)
        if gp.left and node == gp.left.right:      # ensuring it is an LR violation
            self.rotate_left(node.parent)
            node = node.left
        elif gp.right and node == gp.right.left:    # RL violation
            self.rotate_right(node.parent)
            node = node.right

        # Case 5: The newly inserted node has a red parent, but that parent has a black sibling
        # when parent and node are  in same direction  (RR and LL violations). Also change the colors of parent and gp
        p = node.parent
        gp = grandparent(node)
        if gp.left and node == gp.left.left:
            self.rotate_right(gp)
        if gp.right and node == gp.right.right:
            self.rotate_left(gp)

        p.color = "black"
        gp.color = "red"


    # Rotations

    def rotate_left(self, node):
        # storing the parent node
        parentnode = node.parent

        # node that will replace previous node
        newnode = node.right

        # if any left child of newnode exists move it to right of node
        node.right = newnode.left

        # move node to left of new node
        newnode.left = node
        node.parent = newnode

        # finally place the newnode as child of original parent
        if parentnode != None:
            if node == parentnode.left:
                parentnode.left = newnode
            else:
                parentnode.right = newnode
        newnode.parent = parentnode


    def rotate_right(self, node):
        # storing the parent node
        parentnode = node.parent

        # node that will replace previous node
        newnode = node.left

        # if any right child of newnode exists move it to left   of node
        node.left = newnode.right

        # move node to right of new node
        newnode.right = node
        node.parent = newnode

        if parentnode != None:
            if node == parentnode.left:
                parentnode.left = newnode
            else:
                parentnode.right = newnode
        newnode.parent = parentnode

# print function to print different test cases
def print_tree(node, level=0):
    print('   ' * (level - 1) + '+--' * (level > 0) + '%s' % node)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)

tree = RedBlackTree(9)
tree.insert(6)
tree.insert(19)

print_tree(tree.root)

tree.insert(13)
print_tree(tree.root)

tree.insert(16)
print_tree(tree.root)
