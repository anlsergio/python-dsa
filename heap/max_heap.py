class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current_index = len(self.heap) - 1

        while current_index > 0 and self.heap[current_index] > self.heap[self._parent(current_index)]:
            self._swap(current_index, self._parent(current_index))
            current_index = self._parent(current_index)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        # move the last item of the heap to the top.
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            # for each iteration, if the corresponding left and right indexes are not out of bounds,
            # find the greatest value amongst the left and right children.
            if (left_index < len(self.heap) and
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
            if (right_index < len(self.heap) and
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            # if the greatest value is not pointing at the index
            # they need to switch places.
            if max_index != index:
                self._swap(index, max_index)
                # move the cursor down to the new greatest value index.
                index = max_index
            else:
                # if the cursor is pointing to the greatest value, there's nothing else to do.
                # This means, that the value is sunk down to the right place already and the heap is valid.
                return


my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)

print(my_heap.heap)

my_heap.insert(100)

print(my_heap.heap)

my_heap.insert(75)

print(my_heap.heap)

print("\nRemove:")
my_heap = MaxHeap()
my_heap.insert(95)
my_heap.insert(75)
my_heap.insert(80)
my_heap.insert(55)
my_heap.insert(60)
my_heap.insert(50)
my_heap.insert(65)

print(my_heap.heap)

my_heap.remove()
print(my_heap.heap)

my_heap.remove()
print(my_heap.heap)


##################################
# Find Kth Smallest Algorithm
##################################

def find_kth_smallest(nums, k):
    nums_heap = MaxHeap()
    for num in nums:
        nums_heap.insert(num)
        # keep removing all values that bubble up above the
        # kth element, which will cause the kth smallest value to
        # be at the root of the heap naturally when all nums were eventually processed in the heap,
        # considering that for every insert, the values are organized so that the root contains the
        # greatest number, which in this case, will be the kth smallest value.
        if len(nums_heap.heap) > k:
            nums_heap.remove()
    return nums_heap.heap[0]


print("\nFind kth smallest:")

# want 3
print(find_kth_smallest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
