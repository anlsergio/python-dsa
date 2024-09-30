class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class Stack:
    def __init__(self, value):
        self.top = Node(value)
        self.height = 1

    def print(self):
        current = self.top
        if not current:
            print("Stack is empty!")
            return
        while current:
            print(current.value)
            current = current.next

    def push(self, value):
        new_node = Node(value)
        if not self.height:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if not self.height:
            return None
        node_to_pop = self.top
        self.top = node_to_pop.next
        node_to_pop.next = None
        self.height -= 1
        return node_to_pop

print("push")
stack = Stack(1)
stack.push(2)
stack.print()

print("\npop")
stack = Stack(1)
stack.push(2)
print(stack.pop().value, "\n")
stack.print()
