from lutris.database.sql import cursor_execute


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            print("++++++++++++++++++++++++++++++++++++++++++++" +
                  "\nvalue: "+ str(temp.value) +
                  "\nnext: "+ str(temp.next)+
                  "\nprevious: "+ str(temp.prev))
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.head:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        if not self.head:
            return None

        node_to_pop = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # set the new tail to the node that precedes the current tail.
            self.tail = node_to_pop.prev
            # disconnect the original tail from the list
            self.tail.next = None
            node_to_pop.prev = None
        self.length -= 1
        return node_to_pop

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if not self.head:
            return None
        node_to_pop = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = node_to_pop.next
            self.head.prev = None
            node_to_pop.next = None
        self.length -= 1
        return node_to_pop

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            candidate = self.head
            for _ in range(index):
                candidate = candidate.next
        else:
            candidate = self.tail
            # get the number of hops necessary to hit
            # the node starting from the tail moving backwards.
            # (self.length - 1) because length doesn't count from 0 as the index does
            # so we need to balance the difference of the 2 units.
            hops = (self.length - 1) - index
            for _ in range(hops):
                candidate = candidate.prev
        return candidate

    def set_value(self, index, value):
        node_to_be_set = self.get(index)
        if not node_to_be_set:
            return False
        node_to_be_set.value = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        node_before = self.get(index -1)
        node_after = node_before.next

        new_node.next = node_after
        new_node.prev = node_before
        node_before.next = new_node
        node_after.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()

        node_to_remove = self.get(index)
        node_before = node_to_remove.prev
        node_after = node_to_remove.next

        # update the surrounding nodes' links
        node_before.next = node_after
        node_after.prev = node_before

        # disconnect the node from the list
        node_to_remove.next = None
        node_to_remove.prev = None

        self.length -= 1
        return node_to_remove

    def swap_first_last(self):
        if self.length <= 1:
            return False
        self.head.value, self.tail.value = self.tail.value, self.head.value
        return True

    def reverse(self):
        current = self.head
        if not current:
            return False

        while current:
            next_node = current.next
            current.next, current.prev = current.prev, current.next
            current = next_node

        self.head, self.tail = self.tail, self.head

        return True

    def is_palindrome(self):
        if self.length <= 1:
            return True

        # initialize 2 cursors one starting from the head,
        # and the other, starting from tail.
        # for each iteration, both corresponding values should match.
        # To optimize the time complexity, there's no reason for the script
        # to run all the way to the end of the list, because each cursor
        # covers its own half of the list and 2 nodes are being compared at a time.
        forward_cursor = self.head
        backward_cursor = self.tail

        for _ in range(self.length // 2):
            if forward_cursor.value != backward_cursor.value:
                return False
            forward_cursor = forward_cursor.next
            backward_cursor = backward_cursor.prev

        return True

    def swap_pairs(self):
        if self.length <= 1:
            return True
        current = self.head
        # Since we know for sure that the list has
        # at least 2 valid nodes at this point,
        # the second node should become the new head, because it's
        # going to be swapped with the first node.
        self.head = self.head.next
        while current:
            node_before = current.prev
            node_after = current.next

            # this swapping strategy takes in consideration the node next
            # to the current one to swap. Considering it will swap in pairs,
            # it will only swap if there's a node next to it.
            if node_after:
                # next_node represents the node next to the pair
                # which is not directly involved in the current pair swap
                # but is part of the node_after original link reference.
                next_node = node_after.next
                current.next = next_node
                current.prev = node_after
                if next_node:
                    next_node.prev = current
                node_after.next = current
                node_after.prev = node_before

                # if there's a node that is preceding the current pair being swapped
                # its link to the new next node must be updated.
                if node_before:
                    node_before.next = node_after

            current = current.next

linked_list = DoublyLinkedList(1)
print(linked_list.print())

print("\nappend:")
linked_list.append(2)
linked_list.append(3)
print(linked_list.print())

print("\npop:")
linked_list.pop()
print(linked_list.print())

print("\nprepend:")
linked_list.prepend(-1)
linked_list.print()

print("\npop first:")
linked_list.pop_first()
linked_list.print()

print("\nget:")
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
print(linked_list.get(3).value)

print("\nset value:")
print("\noriginal list:")
linked_list.print()
linked_list.set_value(3, 555)
print("\nupdated list:")
linked_list.print()
linked_list.set_value(3, 4)

print("\ninsert:")
print(linked_list.insert(4, 111))
print("print all:")
print(linked_list.print())

print("\nremove:")
print(linked_list.remove(4))
print("print all:")
print(linked_list.print())

##################################
# Swap first and Last Algorithm
##################################

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)

print('DLL before swap_first_last():')
my_doubly_linked_list.print()

my_doubly_linked_list.swap_first_last()

print('\nDLL after swap_first_last():')
my_doubly_linked_list.print()

##################################
# Reverse Algorithm
##################################

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before reverse():')
my_doubly_linked_list.print()

my_doubly_linked_list.reverse()

print('\nDLL after reverse():')
my_doubly_linked_list.print()

##################################
# Is Palindrome Algorithm
##################################

my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome (True):')
print( my_dll_1.is_palindrome() )

my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome (False):')
print( my_dll_2.is_palindrome() )

my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)

print('\nmy_dll_3 is_palindrome (False):')
print( my_dll_2.is_palindrome() )

##################################
# Is Palindrome Algorithm
##################################

my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)

print('my_dll before swap_pairs:')
my_dll.print()

my_dll.swap_pairs()

print('my_dll after swap_pairs:')
my_dll.print()
