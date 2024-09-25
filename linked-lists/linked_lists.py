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
            print("value: "+ str(temp.value) + " next: "+ str(temp.next))
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

        previous_node = self.get(index-1)
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
        if index == self.length-1:
            return self.pop()

        previous_node = self.get(index-1)
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
        # +1 because it must exclude the 1st iteration from the loop count.
        sub_list_window_size = (end_index - start_index) + 1

        # bail out if the list is empty or if it has only 1 node.
        # it also bails out if the reverse window size is below 2 nodes, since there's
        # nothing to be reversed in that case.
        if not self.head or not self.head.next or sub_list_window_size < 2:
            return None

        current = self.head
        # keeps track of the node that precedes the first node of the sub-list.
        general_list_previous_node = None
        counter = 0

        # traverse the list until the node matching the start index is found
        while current:
            if counter == start_index:
                # The "sub_list_previous" cursor is initialized by pointing to the node that originally
                # precedes the sub-list, if there's any. If the sub-list starts from the first node
                # of the original list, sub_list_previous would be set to "None" at this point, meaning that
                # there's no sub_list_previous node originally.
                sub_list_previous = general_list_previous_node
                sub_list_next_node = None
                sub_list_last_node = current

                # reverse the sub-list starting by where the current pointer left off
                # up to the amount of nodes next to it according to the window size.
                # It uses a 3 cursor approach, to keep track of current node, its corresponding
                # sub_list_previous and next nodes to interchange the "next" pointers accordingly.
                # Important: it assumes that the index would never be out of bounds.

                # This inner loop updates the "current" cursor affecting the outer loop behavior,
                # which ensures that no nodes are revisited, keeping it within the bounds of O(n) time complexity.
                for _ in range(sub_list_window_size):
                    # keeps track of the original next node before the pointer is lost
                    sub_list_next_node = current.next
                    # sets the next pointer of the current node being traversed to its sub_list_previous node
                    # reversing the link direction to the "left".
                    current.next = sub_list_previous
                    # moves the "sub_list_previous" cursor to the "right".
                    sub_list_previous = current
                    # moves the "current" cursor to the right
                    current = sub_list_next_node

                # adjusts the loose end of the sub-list, linking the now last node of the sub-list
                # to the node that was next to the original sub-list last node (before the sub-list was reversed)
                sub_list_last_node.next = sub_list_next_node
                # if there's no general_list_previous_node set it means that the
                # reversing window started by the first node, so the "head" must be reset accordingly.
                # Otherwise, keep the head pointer as is, since the first node of the original list
                # hasn't been impacted.
                if not general_list_previous_node:
                    self.head = sub_list_previous
                else:
                    # adjust the loose end of the original sub_list_previous node
                    # so that it points to the new next node of the reversed sub-list
                    general_list_previous_node.next = sub_list_previous
            else:
                # keeps on updating the general_list_previous_node cursor until it hits the sub-list starting node.
                general_list_previous_node = current
                counter += 1
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

print( middle_linked_list.find_middle_node().value )

##################################
# Has Loop Algorithm
##################################

print("\nHas loop true:")
loop_detection_list1 = LinkedList(1)
loop_detection_list1.append(2)
loop_detection_list1.append(3)
loop_detection_list1.append(4)
loop_detection_list1.tail.next = loop_detection_list1.head
print(loop_detection_list1.has_loop()) # Returns True

print("\nHas loop false:")
loop_detection_list2 = LinkedList(1)
loop_detection_list2.append(2)
loop_detection_list2.append(3)
loop_detection_list2.append(4)
print(loop_detection_list2.has_loop()) # Returns False

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
ll.length = 0   # Adjusting the length to reflect an empty list
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