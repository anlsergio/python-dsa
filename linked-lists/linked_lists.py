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
        while temp:
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

    #   +===================================================+
    #   |               WRITE YOUR CODE HERE                |
    #   | Description:                                      |
    #   | - This method partitions a linked list around a   |
    #   |   value `x`.                                      |
    #   | - It rearranges the nodes so that all nodes less  |
    #   |   than `x` come before all nodes greater or equal |
    #   |   to `x`.                                         |
    #   |                                                   |
    #   | Tips:                                             |
    #   | - We use two dummy nodes, `dummy1` and `dummy2`,  |
    #   |   to build two separate lists: one for elements   |
    #   |   smaller than `x` and one for elements greater   |
    #   |   or equal to `x`.                                |
    #   | - `prev1` and `prev2` help us keep track of the   |
    #   |   last nodes in these lists.                      |
    #   | - Finally, we merge these two lists by setting    |
    #   |   `prev1.next = dummy2.next`.                     |
    #   | - The head of the resulting list becomes          |
    #   |   `dummy1.next`.                                  |
    #   +===================================================+
    def partition_list(self, x):
        if not self.head:
            return False

        # If it's a single element list return immediately because there's nothing to rearrange.
        if not self.head.next:
            return True

        temp = self.head
        # keeps track of the last greater and smaller nodes
        # added to their respective new lists.
        last_greater_node = None
        last_smaller_node = None

        # the dummy nodes initialize their respective new linked lists
        # by holding the temporary head pointers to their respective lists.
        dummy_greater_node = Node(0)
        dummy_smaller_node = Node(0)

        while temp:
            if temp.value < x:
                # if last_smaller_node is not null, then there's a previous node
                # to link to the current one.
                if last_smaller_node:
                    last_smaller_node.next = temp
                # If it's null, initialize the smaller linked list
                # by setting the dummy node's next pointer which will work as the head of the new list.
                else:
                    dummy_smaller_node.next = temp
                # update the last smaller node.
                last_smaller_node = temp
            else:
                if last_greater_node:
                    last_greater_node.next = temp
                else:
                    dummy_greater_node.next = temp
                last_greater_node = temp
            # walk the original list.
            temp = temp.next

        # merge the two lists in case the smaller list is populated.
        # - in case there's no corresponding head of the greater list,
        # the last smaller node will point to None, which ends the list anyway;
        # - in case there's no smaller list, that means all nodes are equal or greater
        # than "x", and therefore, the list is left unchanged.
        if last_smaller_node:
            last_smaller_node.next = dummy_greater_node.next
            self.head = dummy_smaller_node.next

        # set the end of the list to prevent a loop.
        if last_greater_node:
            last_greater_node.next = None
        else:
            last_smaller_node.next = None

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

# Reverse Algorithm

print("\nreverse:")
print(linked_list.reverse())
print("print all:")
print(linked_list.print())

# Find Middle Algorithm

middle_linked_list = LinkedList(1)
middle_linked_list.append(2)
middle_linked_list.append(3)
middle_linked_list.append(4)
middle_linked_list.append(5)
middle_linked_list.append(6)

print( middle_linked_list.find_middle_node().value )

# Has Loop Algorithm

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

# Find Kth node from end Algorithm

print("\nFind kth node from end:")
find_kth_node_list = LinkedList(1)
find_kth_node_list.append(2)
find_kth_node_list.append(3)
find_kth_node_list.append(4)
find_kth_node_list.append(5)

k = 2
result = find_kth_from_end(find_kth_node_list, k)

print(result.value)  # Output: 4

# Partition List Algorithm

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
