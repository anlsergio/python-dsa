class MinHeap:
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

        while current_index > 0 and self.heap[current_index] < self.heap[self._parent(current_index)]:
            self._swap(current_index, self._parent(current_index))
            current_index = self._parent(current_index)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        # move the last item of the heap to the top.
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return min_value

    def _sink_down(self, index):
        min_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            # for each iteration, if the corresponding left and right indexes are not out of bounds,
            # find the smallest value amongst the left and right children.
            if (left_index < len(self.heap) and
                    self.heap[left_index] < self.heap[min_index]):
                min_index = left_index
            if (right_index < len(self.heap) and
                    self.heap[right_index] < self.heap[min_index]):
                min_index = right_index
            # if the smallest value is not pointing at the index
            # they need to switch places.
            if min_index != index:
                self._swap(index, min_index)
                # move the cursor down to the new greatest value index.
                index = min_index
            else:
                # if the cursor is pointing to the greatest value, there's nothing else to do.
                # This means, that the value is sunk down to the right place already and the heap is valid.
                return
