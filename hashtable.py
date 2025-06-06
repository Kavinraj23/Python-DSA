class MyHashTable:
    def __init__(self, initial_capacity=8):
        self.table = [[] for _ in range(initial_capacity)]
        self.capacity = initial_capacity
        self.size = 0

    def put(self, key, value):
        i = self._hash(key)
        bucket = self.table[i]
        
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                bucket[idx] = (key, value)
                return
        
        bucket.append((key, value))
        self.size += 1

        if self.size / self.capacity > 0.75:
            self._resize()
            
    def get(self, key): 
        i = self._hash(key)
        bucket = self.table[i]

        for k, v in bucket:
            if k == key:
                return v
        
        return None

    def remove(self, key):
        i = self._hash(key)
        bucket = self.table[i]

        for indx, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[indx]
                self.size -= 1
                return
            
    def contains(self, key):
        return self.get(key) is not None

    def keys(self):
        keys = []
        for bucket in self.table:
            for k, _ in bucket:
                keys.append(k)
        return keys

    def _hash(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.capacity
        return hash_value

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]

        for bucket in old_table:
            for k, v in bucket:
                self.put(k, v)

ht = MyHashTable()
ht.put("apple", 5)
ht.put("banana", 8)
ht.put("grape", 10)
print(ht.get("banana"))   # 8
print(ht.contains("grape"))  # True
ht.remove("banana")
print(ht.get("banana"))   # None
print(ht.keys())