class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Space complexity: O(1)
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        current = self.root
        while True:
            if new_node.value == current.value:
                return False
            if new_node.value < current.value:
                if not current.left:
                    current.left = new_node
                    return True
                current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    return True
                current = current.right

    # the recursive approach favors code readability over
    # space complexity because of all the methods being added
    # to the call stack.
    # Space complexity: O(log n)
    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_insert(self, current_node: Node, value):
        if current_node is None:
            return Node(value)
        # If the value being inserted in smaller than the current node's value
        # it walks left of the current node.
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def contains(self, value):
        current = self.root
        while current:
            if current.value == value:
                return True
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def __r_contains(self, current_node: Node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __delete_node(self, current_node: Node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if not current_node.right and not current_node.left:
                return None
            elif not current_node.right:
                current_node = current_node.left
            elif not current_node.left:
                current_node = current_node.right
            else:
                # if there are nodes both in the right and the left of the
                # node to be deleted, we need to get the minimum value
                # of the subtree in the right (that represents a group of nodes
                # containing values greater than the current node by definition).
                # The node with the smallest value from the subtree in the right
                # should take the void left by the node being deleted, which will
                # keep the tree balanced (greater values to the right, smallest to the left).
                sub_tree_min = self.min_value(current_node.right)
                # We do that by copying the smallest value of the subtree in the right
                current_node.value = sub_tree_min
                # then we have to delete the now duplicate value in the subtree, so that
                # no duplicates are left.
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)

    def min_value(self, current_node):
        # running to the left indefinitely will get us
        # to the minimum value of the tree.
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, node: Node):
        if not node:
            return None
        node.right, node.left = self.__invert_tree(node.left), self.__invert_tree(node.right)
        return node


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

# should print False, since it's a duplicate.
print(my_tree.insert(3))

print("\nContains:")
# Expects "True"
print(my_tree.contains(2))
# Expects "False"
print(my_tree.contains(5))

print("\nRecursive Contains:")
# Expects "True"
print(my_tree.contains(2))
# Expects "False"
print(my_tree.contains(5))

print("\nRecursive insert:")

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)


#######################################
# Invert BST Algorithm
#######################################

def tree_to_list(node):
    """Helper function to convert tree to list level-wise for easy comparison"""
    if not node:
        return []
    queue = [node]
    result = []
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.value)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    while result and result[-1] is None:  # Clean up trailing None values
        result.pop()
    return result


def test_invert_binary_search_tree():
    print("\n--- Testing Inversion of Binary Search Tree ---")
    # Define test scenarios
    scenarios = [
        ("Empty Tree", [], []),
        ("Single Node", [1], [1]),
        ("Tree with Left Child", [2, 1], [2, None, 1]),
        ("Tree with Right Child", [1, 2], [1, 2]),
        ("Multi-Level Tree", [3, 1, 5, 2], [3, 5, 1, None, None, 2]),
        ("Invert Twice", [4, 2, 6, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]),
    ]

    for description, setup, expected in scenarios:
        bst = BinarySearchTree()
        for num in setup:
            bst.r_insert(num)
        if description == "Invert Twice":
            bst.invert()  # First inversion
        bst.invert()  # Perform inversion (or second inversion for the specific case)
        result = tree_to_list(bst.root)
        print(f"\n{description}: {'Pass' if result == expected else 'Fail'}")
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")


test_invert_binary_search_tree()
