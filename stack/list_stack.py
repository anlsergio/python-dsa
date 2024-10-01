# A Stack implemented using a simple list
class Stack:
    def __init__(self):
        self.stack_list = []
    def print(self):
        for s in self.stack_list:
            print(s)
    def is_empty(self):
        return not len(self.stack_list)
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]
    def push(self, value):
        self.stack_list.append(value)
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

##################################
# Reverse String Algorithm
##################################

def reverse_string(ss):
    r_stack = Stack()
    for s in ss:
        r_stack.push(s)

    reversed_ss = ""
    while not r_stack.is_empty():
        reversed_ss += r_stack.pop()
    return reversed_ss

print(reverse_string("abcde"))
print(reverse_string(""))

##################################
# Sort Stack Algorithm
##################################

# Overall, this implementation has a time complexity of O(n^2),
# where n is the number of elements in the original stack, because
# the function performs nested loops to compare all the elements with each other.
# However, it has the advantage of using only one additional stack, which could be
# useful in certain situations where memory is limited.

def sort_stack(input_stack: Stack):
    sorted_stack = Stack()

    while not input_stack.is_empty():
        temp = input_stack.pop()
        # temp is compared with the elements in the sorted stack
        # ensuring that the smallest number is enforced to be at the bottom of the stack
        # in descending order.
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            # all values bigger than temp are moved back to the input stack
            # so that temp is properly ordered in the sorted stack.
            # Considering that sorted_stack is expected to be always properly sorted
            # in the universe of the values present in it, it's safe to assume that
            # if the next peek is a smaller number than temp, then temp could be
            # pushed to the stack and the descending order is kept.
            input_stack.push(sorted_stack.pop())
        # only when all elements currently in sorted_stack are ensured
        # to be smaller than temp, temp is allowed to be pushed to the sorted stack.
        sorted_stack.push(temp)

    while not sorted_stack.is_empty():
        input_stack.push(sorted_stack.pop())

my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print()
