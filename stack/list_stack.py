# A Stack implemented using a simple list
class Stack:
    def __init__(self):
        self.stack_list = []
    def print(self):
        for s in self.stack_list:
            print(s)
    def push(self, value):
        self.stack_list.append(value)
    def is_empty(self):
        return not len(self.stack_list)
    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()

print("push")
stack = Stack()
stack.push(1)
stack.push(2)
stack.print()

print("\npop")
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop(), "\n")
print(stack.pop(), "\n")
stack.print()
