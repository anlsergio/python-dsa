class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    # the recursive approach favors code readability over
    # space complexity because of all the methods being added
    # to the call stack.
    # Space complexity: O(log n)
    def recursive_insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        return self.traverse_and_insert(new_node, self.root)
    def traverse_and_insert(self, insert_node: Node, current_node: Node):
        # duplicates are not allowed in BSTs.
        if insert_node.value == current_node.value:
            return False
        # If the value being inserted in less than the current node's value
        # it walk left of the current node.
        if insert_node.value < current_node.value:
            # if there's a current node already on the left, go to this process again
            # to keep walking the tree. Otherwise, insert the node on the left of the
            # current node.
            if current_node.left:
                return self.traverse_and_insert(insert_node, current_node.left)
            current_node.left = insert_node
        else:
            if current_node.right:
                return self.traverse_and_insert(insert_node, current_node.right)
            current_node.right = insert_node
        return True

my_tree = BinarySearchTree()
my_tree.recursive_insert(2)
my_tree.recursive_insert(1)
my_tree.recursive_insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

print(my_tree.recursive_insert(3))
print(my_tree.recursive_insert(3))
