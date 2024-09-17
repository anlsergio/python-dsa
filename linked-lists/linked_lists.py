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
        if not self.head:
            return None
        slow_cursor = self.head
        fast_cursor = self.head
        candidate = self.head

        while fast_cursor:
            # for each iteration of the loop
            # the fast cursor should move 2 nodes
            # at a time, but it's necessary to check
            # if the next immediate node is a dead end first.
            # which is used to know if the list is even or odd.

            # if the immediate node next to fast cursor is None
            # that means it's an ODD list and candidate should be returned.
            if not fast_cursor.next:
                break
            fast_cursor = fast_cursor.next

            # if fast cursor only hits a dead end in its
            # 2nd hop, it's an even list, so the middle node
            # should the first node of the 2nd half of the list,
            # which in this case, is the node next to the slow cursor.
            if not fast_cursor.next:
                candidate = slow_cursor.next
                break
            fast_cursor = fast_cursor.next
            slow_cursor = slow_cursor.next
            candidate = slow_cursor

        return candidate


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

print("\nreverse:")
print(linked_list.reverse())
print("print all:")
print(linked_list.print())

middle_linked_list = LinkedList(1)
middle_linked_list.append(2)
middle_linked_list.append(3)
middle_linked_list.append(4)
middle_linked_list.append(5)
middle_linked_list.append(6)

print( middle_linked_list.find_middle_node().value )
