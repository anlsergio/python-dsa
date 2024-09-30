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

##################################
# Balanced Parenthesis Algorithm
##################################

def is_balanced_parentheses(ss):
    p_stack = Stack()
    for s in ss:
        # if it's an opening parenthesis, push it to the stack.
        if s == '(':
            p_stack.push(s)
        # if it's a closing one, there must be a  valid opening parenthesis
        # on the stack corresponding to the closing counterpart.
        elif s == ')':
            if p_stack.is_empty() or p_stack.pop() != '(':
                return False

    # at the end of the iteration, all corresponding opening
    # parenthesis added to the stack must be popped out by
    # their closing counterparts.
    return p_stack.is_empty()

print("is balanced (False): ", is_balanced_parentheses("((())"))
print("is balanced (True): ", is_balanced_parentheses("((()))"))
