class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        curr = self.head
        while(curr.next):
            curr = curr.next
        curr.next = newnode
    
    def prepend(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        newnode.next = self.head
        self.head = newnode
    
    def print_list(self):
        currnode = self.head
        while(currnode):
            print(currnode.data, end=" ")
            currnode = currnode.next
        print()

    def delete_by_value(self, data):
        if self.head is None:
            return
    
        if self.head.data == data:
            self.head = self.head.next

        prev = self.head
        curr = self.head.next

        while(curr):
            if(curr == data):
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
    
    def search(self, data):
        currnode = self.head
        
        while(currnode):
            if currnode.data == data:
                return True
            currnode = currnode.next
        
        return False
    
    def length(self):
        if self.head == None:
            return 0
        len = 00
        currnode = self.head
        while(currnode):
            currnode = currnode.next
            len += 1
        
        return len

    def insert_after(self, prev_data, new_data):
        curr = self.head
        while(curr):
            if curr.data == prev_data:
                newnode = Node(new_data)
                newnode.next = curr.next
                curr.next = newnode
                return
            curr = curr.next

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        
        self.head = prev
    
    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
ll = LinkedList()
ll.append(4)
ll.append(5)
ll.append(6)
ll.prepend(3)
ll.print_list()
ll.reverse()
print()
ll.append(2)
ll.append(1)
ll.append(0)
ll.print_list()
print("middle:",ll.find_middle().data)
