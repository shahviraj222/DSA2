class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Create buckets

    def _hash(self, key):
        """Hash function to calculate the index for a given key."""
        return hash(key) % self.size

        # self.table = [[], []]
        # The list at self.table[0] is empty ([]).
        
    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        # as a pair we get list so that's why 0 and 1
        for pair in self.table[index]:   
            if pair[0] == key:
                pair[1] = value  # Update value if key exists
                return
        self.table[index].append([key, value])
        print(self.table[index])

    def search(self, key):
        """Search for a key in the hash table and return its value."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        """Remove a key-value pair from the hash table."""
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return
        print("Key not found")

# Example usage
hash_table = HashTable(10)
hash_table.insert("name", "Viraj")
hash_table.insert("age", 25)
print(hash_table.search("name"))  # Output: Viraj
hash_table.delete("age")
print(hash_table.search("age"))  # Output: None
