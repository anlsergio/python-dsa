class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value():
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def remove_all_matching_nodes(self, value_to_remove):
        # Remove matching head nodes
        while self.head_node and self.head_node.get_value() == value_to_remove:
            self.head_node = self.head_node.get_next_node()

        # initialize the current node variable
        # with the head node.
        current_node = self.get_head_node()

        # Traverse the list and remove matching nodes
        while current_node and current_node.get_next_node():
            next_node = current_node.get_next_node()
            if next_node.get_value() == value_to_remove:
                # if the next node's value matches the value to remove
                # update the link of the current node to the next node
                # but still using the same current node as the baseline
                # check, because there might be subsequent next nodes to be removed.
                current_node.set_next_node(next_node.get_next_node())
            else:
                # if it doesn't match, we can promote the next node as a valid node
                # and move on with the check using the next node as the new current
                # node as the baseline.
                current_node = current_node.get_next_node()

linked_list = LinkedList()
linked_list.insert_beginning(100)
linked_list.insert_beginning(20)
linked_list.insert_beginning(30)
linked_list.insert_beginning(100)
linked_list.insert_beginning(100)
linked_list.insert_beginning(30)
linked_list.insert_beginning(100)

print(linked_list.stringify_list())

# linked_list.remove_node(linked_list.get_head_node().get_value())
linked_list.remove_all_matching_nodes(100)

print(linked_list.stringify_list())
