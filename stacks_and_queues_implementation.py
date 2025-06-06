class Stack:
    def __init__(self):
        self.stk = []

    def push(self, value):
        self.stk.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stk.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stk[-1]

    def is_empty(self):
        return not self.stk

    def size(self):
        return len(self.stk)

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def enqueue(self, value):
        new_node = Node(value)

        prev = self.tail.prev
        prev.next = new_node
        new_node.prev = prev
        new_node.next = self.tail
        self.tail.prev = new_node
        

    def dequeue(self):
        if self.is_empty():
            return None
        
        remove_node = self.head.next
        next_node = remove_node.next
        
        self.head.next = next_node
        next_node.prev = self.head
        return remove_node.value

    def front(self):
        if self.head.next == self.tail:
            return None
        return self.head.next.value

    def is_empty(self):
        return self.head.next == self.tail

    def size(self):
        num = 0
        curr = self.head.next
        while curr != self.tail:
            num += 1
            curr = curr.next
        return num 


s = Stack()
s.push(5)
s.push(10)
print(s.pop())      # 10
print(s.peek())     # 5
print(s.is_empty()) # False

q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print(q.dequeue())
print(q.is_empty())
print(q.size())