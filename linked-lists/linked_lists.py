class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head
        if not temp:
            print("List is empty!")
            return
        limit = 0
        while temp and limit < 15:
            limit += 1
            print("value: " + str(temp.value) + " next: " + str(temp.next))
            temp = temp.next

    def prepend(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True

    def append(self, value):
        new_node = Node(value)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if not self.head:
            return None
        current_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return current_node
        previous_node = self.head
        while True:
            is_tail = current_node.next is None
            if is_tail:
                previous_node.next = None
                self.tail = previous_node
                self.length -= 1
                return current_node

            previous_node = current_node
            current_node = current_node.next

    def pop_first(self):
        original_head = self.head
        if self.length <= 1:
            self.head = None
            self.tail = None
            self.length = 0
            if original_head:
                return original_head
            return None
        self.head = self.head.next
        original_head.next = None
        self.length -= 1
        return original_head

    def get(self, index):
        counter = 0
        candidate = self.head
        while candidate and counter <= index:
            if counter == index:
                return candidate
            candidate = candidate.next
            counter += 1
        return None

    def set_value(self, index, value):
        candidate = self.get(index)
        if candidate:
            candidate.value = value
            return True
        return False

    def insert(self, index, value):
        # index is out of range
        if index < 0 or index > self.length:
            return False
        # index is head
        if index == 0:
            return self.prepend(value)
        # index is tail
        if index == self.length:
            return self.append(value)

        previous_node = self.get(index - 1)
        new_node = Node(value)
        new_node.next = previous_node.next
        previous_node.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        previous_node = self.get(index - 1)
        current_node = previous_node.next
        previous_node.next = current_node.next
        current_node.next = None
        self.length -= 1

        return current_node

    def reverse(self):
        if self.length == 0:
            return False
        current_node = self.head
        new_head = self.tail
        new_tail = self.head

        # reverse the head and tail pointers.
        self.head = new_head
        self.tail = new_tail

        previous_node = None

        for _ in range(self.length):
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return True

    def find_middle_node(self):
        # for each iteration of the loop
        # the fast cursor should move 2 nodes
        # at a time, but it's necessary to check
        # if the next immediate node is a dead end first.
        # which is used to know if the list is even or odd.

        # if the immediate node next to fast cursor is None
        # that means it's an ODD list and slow should be returned immediately.

        # 1. Initialize two pointers: 'slow' and 'fast',
        # both starting from the head.
        slow = self.head
        fast = self.head

        # 2. Iterate as long as 'fast' pointer and its next
        # node are not None.
        # This ensures we don't get an error trying to access
        # a non-existent node.
        while fast is not None and fast.next is not None:
            # 2.1. Move 'slow' one step ahead.
            # This covers half the distance that 'fast' covers.
            slow = slow.next

            # 2.2. Move 'fast' two steps ahead.
            # Thus, when 'fast' reaches the end, 'slow'
            # will be at the middle.
            fast = fast.next.next

        # 3. By now, 'fast' has reached or surpassed the end,
        # and 'slow' is positioned at the middle node.
        # Return the 'slow' pointer, which points to
        # the middle node.
        return slow

    def has_loop(self):
        # This algorithm uses Floyd's cycle-finding algorithm
        # (also known as the "tortoise and the hare" algorithm) to detect the loop by using two pointers:
        # a slow pointer and a fast pointer.
        # The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
        # If there is a loop in the linked list, the two pointers will eventually meet at some point.
        # If there is no loop, the fast pointer will reach the end of the list.

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def partition_list(self, x):
        if not self.head:
            return None

        current = self.head
        # the dummy nodes initialize their respective new linked lists
        # by holding the temporary head pointers to their respective lists.
        dummy_greater_node = Node(0)
        dummy_smaller_node = Node(0)

        # keeps track of the last greater and smaller nodes
        # added to their respective new lists.
        # They are initialized with the dummy nodes
        # because they are the first (and last) nodes of the corresponding
        # temporary lists.
        last_greater_node = dummy_greater_node
        last_smaller_node = dummy_smaller_node

        while current:
            if current.value < x:
                last_smaller_node.next = current
                last_smaller_node = current
            else:
                last_greater_node.next = current
                last_greater_node = current
            # walks the original list
            current = current.next

        # Disconnects the last nodes from their respective next nodes,
        # ensuring that both temporary lists are ended properly
        last_greater_node.next = None
        last_smaller_node.next = None

        # Merges both temporary lists together
        # (If the smaller list is empty, the last_smaller_node is in fact the dummy node
        # which will now point directly to the greater nodes list, and if it's the other way around
        # it will point to "None", given it will be the next value of dummy_greater_node).
        last_smaller_node.next = dummy_greater_node.next
        # Points the original Linked List head to the smaller nodes' list head.
        self.head = dummy_smaller_node.next

    def remove_duplicates(self):
        previous = None
        current = self.head
        # We're using a set (seen_values) because checking membership in a set is typically O(1),
        # making it efficient for this operation. As we traverse the list,
        # we'll add each encountered node's value to this set.
        seen_values = set()

        while current:
            next_node = current.next
            if current.value in seen_values:
                previous.next = next_node
                current.next = None
                self.length -= 1
            else:
                previous = current
            seen_values.add(current.value)
            current = next_node

    def binary_to_decimal(self):
        total = 0
        current = self.head

        # Use the "Double-Dabble" method to convert
        # without having to use positions.
        # Ref.: https://www.binaryhexconverter.com/binary-to-decimal-converter
        while current:
            total = total * 2 + current.value
            current = current.next

        return total

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        if self.length <= 1:
            return None

        # dummy node works as a helper node to help keep
        # the reference to the lists head dynamically during the
        # reversal process in case the first node is also affected by the reverse window.
        dummy_node = Node(0)
        dummy_node.next = self.head
        # initializing previous as a dummy node
        # will ensure that previous.next work for the first iteration.
        previous = dummy_node

        # this loop will exit leaving the previous cursor in the
        # node the precedes the sub-list's starting node.
        for _ in range(start_index):
            previous = previous.next

        # initialize sub_list_starting_node with the sub-list's starting node
        sub_list_starting_node = previous.next

        sub_list_window_size = end_index - start_index
        for _ in range(sub_list_window_size):
            # this logic works by iteratively shifting the
            # previous.next cursor to the right-most nodes of the sub-list,
            # where "previous" is fixed to the node that precedes the sub-list
            # its next pointer is moved one node at a time to the right, adjusting
            # the references to the node next to the moved node as well.
            node_to_move = sub_list_starting_node.next
            sub_list_starting_node.next = node_to_move.next
            # Reverse the link between the previous node and the node_to_move,
            # by moving the node next to the previous node to the right of the node_to_move
            # and finally linking the previous node to the node_to_move
            node_to_move.next = previous.next
            previous.next = node_to_move

        self.head = dummy_node.next

    def merge(self, other_list):
        # dummy will hold the reference to the start of the
        # new list.
        dummy = Node(0)
        # current_merged represents the cursor of the combined list
        current_merged = dummy
        # current_self is the cursor of the original list
        current_self = self.head
        # current_other is the cursor of the other list
        current_other = other_list.head

        while current_self and current_other:
            # link the smallest value node to the temp linked list
            if current_self.value < current_other.value:
                current_merged.next = current_self
                # move the cursor of the self list
                current_self = current_self.next
            else:
                current_merged.next = current_other
                # move the cursor of the another list
                current_other = current_other.next
            # move the cursor of the temp list
            current_merged = current_merged.next

        # considering it's a linked list and that only 1 list contains
        # leftovers at this point, it's just a matter of linking the end
        # of the temp list to the start of the list that has leftovers.
        if current_self:
            current_merged.next = current_self
        else:
            current_merged.next = current_other
            # it's only necessary to adjust the tail if the new list
            # will end with nodes from another list. Otherwise, the reference
            # remains as originally is.
            self.tail = other_list.tail

        self.head = dummy.next
        self.length += other_list.length

    def bubble_sort(self):
        # if the list has only 1 element or less, it's sorted by design.
        if self.length < 2:
            return
        # Initialize 'sorted_cursor' to None. This cursor will
        # indicate the boundary between the sorted part of
        # the list and the part that still needs sorting.
        # Until it's defined as anything but None, it's still useful
        # to mark the end of the list, since the tail node will point to None as well.
        sorted_cursor = None

        # The outer loop will continue
        # running until the sorted section of the list
        # includes the second node, meaning the whole
        # list is sorted.
        while self.head.next != sorted_cursor:
            current = self.head
            # Begin the inner loop. It runs until 'current'
            # reaches the 'sorted_until' node. This loop is
            # where the actual comparison and sorting happen.
            while current.next != sorted_cursor:
                next_node = current.next
                if current.value > next_node.value:
                    current.value, next_node.value = next_node.value, current.value
                current = current.next
            # Update 'sorted_cursor' after each full pass of
            # the inner loop. This moves the boundary of the
            # sorted section one node forward, shrinking the
            # unsorted section accordingly.
            sorted_cursor = current

    def selection_sort(self):
        if self.length < 2:
            return
        current = self.head
        # run the loop up traversing the list, excluding the last node
        # because there's no reason to go up to the last node considering inner_current
        # will be compared to min_node, which goes up to the end of the list.
        # And the same is for the other way around. "inner_current" starts at the current's next node, because
        # it will be compared to current anyway.
        while current.next:
            min_node = current
            inner_current = current.next
            while inner_current:
                if inner_current.value < min_node.value:
                    min_node = inner_current
                inner_current = inner_current.next
            if min_node != current:
                current.value, min_node.value = min_node.value, current.value

            current = current.next


def find_kth_from_end(ll: LinkedList, k: int):
    # This function uses the two-pointer technique to efficiently find the kth node from the end of a linked list.
    # By first positioning the fast pointer k nodes ahead of the slow pointer and then moving both pointers
    # at the same speed, we ensure that when the fast pointer reaches the end, the slow pointer is at the
    # desired kth node from the end
    if not k:
        return None

    slow = ll.head
    fast = ll.head

    for _ in range(k):
        # If the fast pointer becomes None before moving k nodes
        # the list is shorter than k nodes and the kth node is out of bounds.
        if not fast:
            return None
        fast = fast.next

    while fast:
        # by keeping the gap of "k" nodes between the two cursors
        # whenever fast hits the end of the list the slow cursor
        # will be pointing at ("the end of the list" - k)
        slow = slow.next
        fast = fast.next

    return slow


linked_list = LinkedList(10)
print(linked_list.print())

print("\nappend:")
linked_list.append(12)
print(linked_list.print())

print("\npop:")
linked_list.pop()
print(linked_list.print())

print("\npop it all:")
linked_list.pop()
print(linked_list.print())

print("\nprepend:")
linked_list.prepend(30)
linked_list.prepend(29)
linked_list.append(31)
print(linked_list.print())

print("\npop first:")
linked_list.pop_first()
print(linked_list.print())

print("\nget:")
got = linked_list.get(1)
if got:
    print(got.value)
else:
    print(got)

print("\nset value:")
print("got:")
print(linked_list.set_value(1, 999))
print("print all:")
print(linked_list.print())

print("\ninsert:")
print(linked_list.insert(1, 111))
print("print all:")
print(linked_list.print())

print("\nremove:")
print(linked_list.remove(1))
print("print all:")
print(linked_list.print())

##################################
# Reverse Algorithm
##################################

print("\nreverse:")
print(linked_list.reverse())
print("print all:")
print(linked_list.print())

##################################
# Find Middle Algorithm
##################################

middle_linked_list = LinkedList(1)
middle_linked_list.append(2)
middle_linked_list.append(3)
middle_linked_list.append(4)
middle_linked_list.append(5)
middle_linked_list.append(6)

print(middle_linked_list.find_middle_node().value)

##################################
# Has Loop Algorithm
##################################

print("\nHas loop true:")
loop_detection_list1 = LinkedList(1)
loop_detection_list1.append(2)
loop_detection_list1.append(3)
loop_detection_list1.append(4)
loop_detection_list1.tail.next = loop_detection_list1.head
print(loop_detection_list1.has_loop())  # Returns True

print("\nHas loop false:")
loop_detection_list2 = LinkedList(1)
loop_detection_list2.append(2)
loop_detection_list2.append(3)
loop_detection_list2.append(4)
print(loop_detection_list2.has_loop())  # Returns False

##################################
# Find Kth node from end Algorithm
##################################

print("\nFind kth node from end:")
find_kth_node_list = LinkedList(1)
find_kth_node_list.append(2)
find_kth_node_list.append(3)
find_kth_node_list.append(4)
find_kth_node_list.append(5)

k = 2
result = find_kth_from_end(find_kth_node_list, k)

print(result.value)  # Output: 4

##################################
# Partition List Algorithm
##################################

print("\nPartition List:")


# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result


# Function to test partition_list
def test_partition_list():
    test_cases_passed = 0

    print("-----------------------")

    # Test 1: Normal Case
    print("Test 1: Normal Case")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    if ll.has_loop():
        print("FAIL: list has loop")
        return
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 2: All Equal Values
    print("Test 2: All Equal Values")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(3)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    if ll.has_loop():
        print("FAIL: list has loop")
        return
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 3: Single Element
    print("Test 3: Single Element")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    if ll.has_loop():
        print("FAIL: list has loop")
        return
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 4: Already Sorted
    print("Test 4: Already Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    if ll.has_loop():
        print("FAIL: list has loop")
        return
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 5: Reverse Sorted
    print("Test 5: Reverse Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    if ll.has_loop():
        print("FAIL: list has loop")
        return
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 3, 2]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 6: All Smaller Values
    print("Test 6: All Smaller Values")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    if ll.has_loop():
        print("FAIL: list has loop")
        return
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 1, 1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 7: Single Element, Equal to Partition
    print("Test 7: Single Element, Equal to Partition")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    if ll.has_loop():
        print("FAIL: list has loop")
        return
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Summary
    print(f"{test_cases_passed} out of 7 tests passed.")


# Run the test function
test_partition_list()

##################################
# Remove Duplicates Algorithm
##################################

print("\nDe-dup:")


def test_remove_duplicates(linked_list, expected_values):
    print("Before: ", end="")
    linked_list.print()
    linked_list.remove_duplicates()
    print("After:  ", end="")
    linked_list.print()

    # Collect values from linked list after removal
    result_values = []
    node = linked_list.head
    while node:
        result_values.append(node.value)
        node = node.next

    # Determine if the test passes
    if result_values == expected_values:
        print("Test PASS\n")
    else:
        print("Test FAIL\n")


# Test 1: List with no duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 2: List with some duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
test_remove_duplicates(ll, [1, 2, 3])

# Test 3: List with all duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(1)
test_remove_duplicates(ll, [1])

# Test 4: List with consecutive duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 5: List with non-consecutive duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
ll.append(4)
test_remove_duplicates(ll, [1, 2, 3, 4])

# Test 6: List with duplicates at the end
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 7: Empty list
ll = LinkedList(None)
ll.head = None  # Directly setting the head to None
ll.length = 0  # Adjusting the length to reflect an empty list
test_remove_duplicates(ll, [])

##################################
# Binary to Decimal Algorithm
##################################

print("\nBinary to decimal:")

# Create a linked list for binary number 101
linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(1)

# Convert binary to decimal
print(linked_list.binary_to_decimal())  # Output: 5

# Create a linked list for binary number 1101
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
linked_list.append(1)

# Convert binary to decimal
print(linked_list.binary_to_decimal())  # Output: 13

# Create a linked list for binary number 0000
linked_list = LinkedList(0)
linked_list.append(0)
linked_list.append(0)
linked_list.append(0)

# Convert binary to decimal
print(linked_list.binary_to_decimal())  # Output: 0

# Create a linked list for binary number 1
linked_list = LinkedList(1)

# Convert binary to decimal
print(linked_list.binary_to_decimal())  # Output: 1

##################################
# Reverse between
##################################

print("\nReverse between:")

print("Reverse a sublist within the linked list:")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
print("Original linked list: ")
linked_list.print()
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
if linked_list.has_loop():
    print("FAIL: list has loop")
    exit(1)
linked_list.print()

print("Reverse a sublist starting at index 0:")
print("Original linked list: ")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print()
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
# if linked_list.has_loop():
#     print("FAIL: list has loop")
#     exit(1)
linked_list.print()

print("Reverse a sublist of length 1 within the linked list:")
print("Original linked list: ")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print()
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
if linked_list.has_loop():
    print("FAIL: list has loop")
    exit(1)
linked_list.print()

print("Reverse an empty linked list:")
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
if linked_list.has_loop():
    print("FAIL: list has loop")
    exit(1)
empty_list.print()

#########################################
# Merge Two Sorted Linked Lists Algorithm
#########################################

print("\nMerge two sorted linked lists:")

l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)

l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print()

##########################################
# Bubble Sort Linked List Algorithm
##########################################

print("\nBubble sort:")

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print()

##########################################
# Selection Sort Linked List Algorithm
##########################################

print("\nSelection sort:")

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print()
