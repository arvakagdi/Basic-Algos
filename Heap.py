class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        """
        Insert `data` into the heap
        """
        self.cbt[self.next_index] = data
        self.up_heapify(self.next_index)
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        if self.size() == 0:
            return None
        last_index = self.next_index - 1
        removed = self.cbt[0]
        self.cbt[0] = self.cbt[last_index]
        self.cbt[last_index] = None
        self.next_index -= 1
        self.down_heapify(0)
        return removed

    def up_heapify(self,child_index):

        if child_index == 0:
            return

        parent_index = (child_index-1)//2

        if self.cbt[parent_index] <= self.cbt[child_index]:
            return
        else:
            swapdata = self.cbt[child_index]
            self.cbt[child_index] = self.cbt[parent_index]
            self.cbt[parent_index] = swapdata

        if parent_index != 0:
            self.up_heapify(parent_index)
        else:
            return

    def down_heapify(self,parent_node):

        child_node1 = 2*parent_node + 1
        child_node2 = 2*parent_node + 2

        if child_node1 < self.next_index and child_node2 < self.next_index:
            if self.cbt[child_node1] <= self.cbt[child_node2]:
                swap_index = child_node1
            else:
                swap_index = child_node2
        if child_node1 >= self.next_index and child_node2 >= self.next_index:
            return

        elif self.cbt[child_node2] is not None and self.cbt[child_node1] is None:
            swap_index = child_node2
        elif self.cbt[child_node1] is not None and self.cbt[child_node2] is None:
            swap_index = child_node1

        if self.cbt[parent_node] <= self.cbt[swap_index]:
            return
        else:
            swapdata = self.cbt[swap_index]
            self.cbt[swap_index] = self.cbt[parent_node]
            self.cbt[parent_node] = swapdata

        if parent_node < self.next_index:
            self.down_heapify(swap_index)

    def size(self):
        return self.next_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]

    def is_empty(self):
        return self.size() == 0


heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
print('Inserted elements: {}'.format(elements))

print('size of heap: {}'.format(heap.size()))

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))

print('Call get_minimum: {}'.format(heap.get_minimum()))

for _ in range(2):
    print('Call remove: {}'.format(heap.remove()))

print('size of heap: {}'.format(heap.size()))
print('Call remove: {}'.format(heap.remove()))
print('Call is_empty: {}'.format(heap.is_empty()))