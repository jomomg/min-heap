class Heap:
    """An implementation of a minimum heap"""

    heap = []

    def _sift_up(self, pos):
        while pos > 0:
            parent_pos = (pos - 1) // 2
            if self.heap[pos] < self.heap[parent_pos]:
                self.heap[pos], self.heap[parent_pos] = self.heap[parent_pos], self.heap[pos]
            pos = parent_pos

    def _sift_down(self, pos):
        end_pos = len(self.heap) - 1
        while 2 * pos + 1 <= end_pos:
            l_child_pos = 2 * pos + 1
            r_child_pos = 2 * pos + 2

            if r_child_pos > end_pos:
                r_child_pos = l_child_pos
            if self.heap[l_child_pos] < self.heap[r_child_pos]:
                min_child_pos = l_child_pos
            else:
                min_child_pos = r_child_pos

            if self.heap[pos] < self.heap[min_child_pos]:
                break
            else:
                self.heap[pos], self.heap[min_child_pos] = self.heap[min_child_pos], self.heap[pos]

            pos = min_child_pos

    def push(self, item):
        """Put an item on to the heap"""
        self.heap.append(item)
        end_pos = len(self.heap) - 1
        self._sift_up(end_pos)

    def pop(self):
        """Remove and return the item at the top of the heap"""
        ret = self.heap[0]
        end_pos = len(self.heap) - 1
        self.heap[0] = self.heap[end_pos]
        self.heap.pop()
        self._sift_down(0)
        return ret

    def peek(self):
        """Return the item at the top of the heap without removing it"""
        return self.heap[0]

    def heapify(self, target: list) -> None:
        """Convert a list into a """
        self.heap = target
        for i in range((len(self.heap)-1) // 2, -1, -1):
            self._sift_down(i)

    @staticmethod
    def is_valid_min_heap(heap: list) -> bool:
        """Check if a given list is a valid min heap"""
        n = len(heap)
        for i in range(n):
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if left_child < n and heap[left_child] < heap[i]:
                return False
            if right_child < n and heap[right_child] < heap[i]:
                return False
        return True


bh = Heap()
bh.heapify([x for x in range(9, -1, -1)])
print(bh.heap)
print(Heap.is_valid_min_heap(bh.heap))


def test_pushing_onto_heap_produces_valid_min_heap(heap: Heap) -> bool:
    inp = [x for x in range(9, -1, -1)]
    for i in inp:
        heap.push(i)
    print(heap.heap)
    return Heap.is_valid_min_heap(heap.heap)


def test_heap_invariant_is_maintained_after_popping(heap: Heap) -> bool:
    for _ in range(len(heap.heap)):
        heap.pop()
        if not Heap.is_valid_min_heap(heap.heap):
            return False
    return True

# print('pushing produces valid heap --> ', test_pushing_onto_heap_produces_valid_min_heap(bh))
# print('popping maintains heap invariant --> ', test_heap_invariant_is_maintained_after_popping(bh))
