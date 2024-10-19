class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # The 'is_balanced' and 'inorder_traversal' methods will
    # be used to test your code
    def is_balanced(self, node=None):
        def check_balance(node):
            if node is None:
                return True, -1
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height

        balanced, _ = check_balance(self.root if node is None else node)
        return balanced

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        result = []
        self._inorder_helper(node, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)

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

    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums)

    def __sorted_list_to_bst(self, nums):
        # base cases
        if len(nums) == 1:
            return Node(nums[0])
        if len(nums) < 1:
            return None
        # get the root of the current subtree, which is the
        # node sitting in the middle of the current sublist.
        mid_index = len(nums) // 2
        root_node = Node(nums[mid_index])

        # find the root nodes of the corresponding sub-lists to the left and
        # to the right of the current root node, and assign the corresponding
        # left and right pointers.
        root_node.left = self.__sorted_list_to_bst(nums[:mid_index])
        root_node.right = self.__sorted_list_to_bst(nums[mid_index + 1:])
        return root_node

    def sorted_list_to_bst_alt(self, nums):
        self.root = self.__sorted_list_to_bst_alt(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst_alt(self, nums, left, right):
        # if left is greater than the right index, this means that
        # the current segment is empty and cannot be further processed.
        if left > right:
            return None
        mid_index = (left + right) // 2
        root_node = Node(nums[mid_index])
        root_node.left = self.__sorted_list_to_bst_alt(nums, left, mid_index - 1)
        root_node.right = self.__sorted_list_to_bst_alt(nums, mid_index + 1, right)
        return root_node

    def BFS(self):
        current = self.root
        # queue stores the nodes being traversed
        queue = []
        # results stores the corresponding values of the nodes seen.
        results = []
        # initialize the queue so that the while loop can start
        queue.append(current)

        while queue:
            current = queue.pop(0)
            results.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current: Node):
            results.append(current.value)
            if current.left:
                traverse(current.left)
            if current.right:
                traverse(current.right)

        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []

        def traverse(current: Node):
            if current.left:
                traverse(current.left)
            if current.right:
                traverse(current.right)
            results.append(current.value)

        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(current: Node):
            if current.left:
                traverse(current.left)
            results.append(current.value)
            if current.right:
                traverse(current.right)

        traverse(self.root)
        return results

    def is_valid_bst(self):
        result = self.dfs_in_order()
        for i in range(1, len(result)):
            if result[i] < result[i - 1]:
                return False

        return True


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


####################################
# Convert Sorted List to BST
####################################

def check_balanced_and_correct_traversal(bst, expected_traversal):
    is_balanced = bst.is_balanced()
    inorder = bst.inorder_traversal()
    print("Is balanced:", is_balanced)
    print("Inorder traversal:", inorder)
    print("Expected traversal:", expected_traversal)
    if is_balanced and inorder == expected_traversal:
        print("PASS: Tree is balanced and inorder traversal is correct.\n")
    else:
        print("FAIL: Tree is either not balanced or inorder traversal is incorrect.\n")


# Test: Convert a sorted list with odd number of elements
# Test: Convert an empty list
print("\n----- Test: Convert Empty List -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([])
check_balanced_and_correct_traversal(bst, [])

# Test: Convert a list with one element
print("\n----- Test: Convert Single Element List -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([10])
check_balanced_and_correct_traversal(bst, [10])

# Test: Convert a sorted list with odd number of elements
print("\n----- Test: Convert Sorted List with Odd Number of Elements -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5])
check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5])

# Test: Convert a sorted list with even number of elements
print("\n----- Test: Convert Sorted List with Even Number of Elements -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6])
check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5, 6])

# Test: Convert a large sorted list
print("\n----- Test: Convert Large Sorted List -----\n")
bst = BinarySearchTree()
large_sorted_list = list(range(1, 16))  # A list from 1 to 15
bst.sorted_list_to_bst(large_sorted_list)
check_balanced_and_correct_traversal(bst, large_sorted_list)

####################################
# Breadth First Search (BFS)
####################################

print("\nBFS:")

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())

####################################
# Pre-order Depth First Search (DFS)
####################################

print("\nPre-order DFS:")
print(my_tree.dfs_pre_order())

####################################
# Post-order Depth First Search (DFS)
####################################

print("\nPost-order DFS:")
print(my_tree.dfs_post_order())

####################################
# In-order Depth First Search (DFS)
####################################

print("\nPost-order DFS:")
print(my_tree.dfs_in_order())

####################################
# Is Valid BST algorithm
####################################

print("\nIs valid BST:")


# this function represents how the is_valid_bst method operates in the BST,
# since a proper implemented BST is always valid by design.
def is_valid_bst(result: list):
    # result = self.dfs_in_order()
    for i in range(1, len(result)):
        if result[i] < result[i - 1]:
            return False

    return True


print("want True: ", is_valid_bst([1, 2, 3]))
print("want True: ", is_valid_bst([1]))
print("want False: ", is_valid_bst([1, 3, 2]))
