'''
Hashing Concept of distributing key  & Find in the constant time O(1).
Loading Factor is important it is always tend to <= 0.5 so give best result 

Solution For Collision:

1)Open Hashing :
    Chaining Concept Collision Occur Use Link List 
    Use Hash Function in batter way

2)Closed Hashing :
    Open For Addressing
    i)Liner 
    ii)Quadratic 
    iii)Double  
        In Stop Condition Searching : 1)empty place 2)detect the cycle (i == size table) 3)get the match

        
Python : Set,Dictionary internally uses hash 
[Nearly every operations take  O(1) Operations by key]       

Practical Use Case

1000+ user data and want to do search [1000+ job post user is view and doing operations]

json_data = """
    {
         "101": {"name": "Alice", "age": 25, "email": "alice@example.com"} ,
         "102": {"name": "Bob", "age": 30, "email": "bob@example.com"} 
    }
"""

data = json.load(json_data)
so try to get the data into dictinary it is suitable for next thing .

here data it self convert it into the dictinary and set
'''

class SingleHashTable:
    def __init__(self,size) -> None:
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self,key) -> int:
        return hash(key)%self.size

    def insert(self,value):
        index = self._hash(value)
        if self.table[index]:
            self.table[index] = value
            return     
        self.table[index].append(value)

    def search(self,value):
        index = self._hash(value)   
        if self.table[index]:
            return value
        return False
    
    def delete(self,value):
        index = self._hash(value) 
        if self.table[index]:
            self.table[index].pop()  # problem : if collision happen, at one index: multiple values there pop remove last one so use enumarate... 
            return True        
        return False
    
    def display(self):
        print(self.table)
        


h1 = SingleHashTable(10)
h1.insert(123)
h1.delete(123)
h1.insert(1232)
h1.display()



class ValuePairHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]                   # Create buckets

    def _hash(self, key):
        """Hash function to calculate the index for a given key."""
        return hash(key) % self.size

        # self.table = [[], []]
        # The list at self.table[0] is empty ([]).
        
    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        # as a pair we get list so that's why 0 and 1  [[]] 
        # [[[k,v]], []]
        for pair in self.table[index]:   
            if pair[0] == key:
                pair[1] = value                                # Update value if key exists
                return
        self.table[index].append([key, value])

    def search(self, key):
        """Search for a key in the hash table and return its value."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None                                            # Key not found

    def delete(self, key):
        """Remove a key-value pair from the hash table."""
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return
        print("Key not found")

# Example usage
hash_table = ValuePairHashTable(10)
hash_table.insert("name", "Viraj")
hash_table.insert("age", 25)
print(hash_table.search("name"))                   # Output: Viraj
hash_table.delete("age")
print(hash_table.search("age") ,"Key not found")   # Output: None



'''
Delete Function 
self.table[index].pop() 
pop() remove value of last element of sub list

a = [[],[],[],[234]]
a[3].pop()

a[3] sublist at index 3 in the list a. In this case, a[3] refers to the sublist [234].
.pop() on a[3] operates sublist [234]. It removes and returns the last element
It does not modify the outer list a in terms of structure; it only changes the contents of the sublist at a[3].


a = [[],[],[],[234,23,24]]
a[3].pop()

after execution
a = [[],[],[],[234,23]]

delete function implementation is important
'''
