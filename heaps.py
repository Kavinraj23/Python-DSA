class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
    
        min_val = self.heap[0]

        if len(self.heap) == 1:
            return self.heap.pop()
        
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_val

    def peek(self):
        return self.heap[0] if self.heap else None

    def heapify_up(self, index):
        # start at index, compare with parent, if smaller than parent swap
        # repeat process until its no longer smaller than parent or reaches root of heap
        while index > 0 and self.heap[index] < self.heap[(index - 1) // 2]:
            parent_index = (index - 1) // 2
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

    def heapify_down(self, index):
        # compare the value at the given index with its children
        # if larger than smaller child, swap and repeat until heap property is resotred
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)
        

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

class PriorityQueue:
    def __init__(self):
        self.pq = MinHeap()
    
    def enqueue(self, value, priority):
        self.pq.insert((priority, value))
    
    def dequeue(self):
        return self.pq.extract_min()
    
    def peek(self):
        return self.pq.peek()

    def is_empty(self):
        return self.pq.is_empty()

# Create the priority queue
pq = PriorityQueue()

# Enqueue items with different priorities
pq.enqueue("clean room", 3)
pq.enqueue("do homework", 1)
pq.enqueue("walk dog", 2)

# Peek at the highest priority task
print("Peek:", pq.peek())  # Expected: (1, "do homework")

# Dequeue all items in order
print("Dequeued:", pq.dequeue())  # Expected: (1, "do homework")
print("Dequeued:", pq.dequeue())  # Expected: (2, "walk dog")
print("Dequeued:", pq.dequeue())  # Expected: (3, "clean room")

# Check if queue is empty
print("Is empty:", pq.is_empty())  # Expected: True


