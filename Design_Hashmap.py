class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    
    def __init__(self):
        self.size = 1000  # Choose a reasonable size for the hashmap
        self.buckets = [None] * self.size  # Initialize the buckets

    def _hash(self, key: int) -> int:
        """Hash function to compute bucket index"""
        return key % self.size

    def put(self, key: int, value: int) -> None:
        """Insert (key, value) or update if key exists"""
        index = self._hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = ListNode(key, value)  # Create a new node if bucket is empty
        else:
            curr = self.buckets[index]
            while curr:
                if curr.key == key:
                    curr.value = value  # Update value if key exists
                    return
                if curr.next is None:
                    break
                curr = curr.next
            curr.next = ListNode(key, value)  # Insert new node at the end

    def get(self, key: int) -> int:
        """Return value associated with key, or -1 if not found"""
        index = self._hash(key)
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1  # Key not found

    def remove(self, key: int) -> None:
        """Remove key-value pair if key exists"""
        index = self._hash(key)
        curr = self.buckets[index]
        prev = None
        
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next  # Remove node from chain
                else:
                    self.buckets[index] = curr.next  # Remove first node
                return
            prev, curr = curr, curr.next
