class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print(self):
        current = self.first
        if not self.length:
            print("Queue empty!")
            return
        while current:
            print(current.value)
            current = current.next

    def enqueue(self, value):
        new_node = Node(value)
        if not self.length:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if not self.length:
            return None
        node_to_dequeue = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            node_to_dequeue.next = None
        self.length -= 1
        return node_to_dequeue

print("enqueue:")
queue = Queue(1)
queue.enqueue(2)
queue.print()

print("dequeue:")
queue = Queue(1)
queue.enqueue(2)
print(queue.dequeue().value, "\n")
queue.print()
