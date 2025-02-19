class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]  # Initialize the hash table with None values
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX # Returns the hash value of the key
    
    def __setitem__(self, key, val): # allows us to use the assignment operator to set the value of a key
        h = self.get_hash(key)
        self.arr[h] = val # Overwrite the value if the key already exists, stores the value at the hash index

    def __getitem__(self, key): # allows us to use the index operator to get the value of a key
        h = self.get_hash(key)
        return self.arr[h] # Returns the value at the hash index
    
    
t = HashTable()

print(t.get_hash('march 12')) # 54
print(t.get_hash('march 6')) # 9
t['march 6'] = 130
t['march 12'] = 140

print(t['march 6']) # 130
print(t['march 12']) # 140