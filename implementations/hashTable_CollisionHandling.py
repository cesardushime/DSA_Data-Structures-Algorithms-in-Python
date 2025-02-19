class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]  # Initialize the hash table with empty lists
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX # Returns the hash value of the key (big O(n) operation because we need to traverse the key)
    
    def __setitem__(self, key, val): # allows us to use the assignment operator to set the value of a key
        h = self.get_hash(key)
        
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key: # checks if a tuple exists at the hash index and if the key is the same
                self.arr[h][idx] = (key, val)
                found = True
                break
            
        if not found:
            self.arr[h].append((key,val)) # Stores the value at the hash index, big O(1) operation
            
            
    def __getitem__(self, key): # allows us to use the index operator to get the value of a key
        h = self.get_hash(key)
        return self.arr[h] # Returns the value at the hash index, big O(1) operation
    
    def del_item(self, key):
        h = self.get_hash(key)
        self.arr[h] = None # Deletes the value at the hash index, big O(1) operation
        
        
t = HashTable()

# print(t.get_hash('march 6')) # 9
# print(t.get_hash('march 12')) # 54
# print(t.get_hash('march 21')) # 54



t['march 6'] = 130 # 9
t['march 17'] = 459 # 63
t['march 21'] = 140 # 54
t['march 12'] = 440 # 54, same hash index as march 21


print(t['march 17']) 
print(t['march 21']) # will return a list of tuples [('march 21', 140), ('march 12', 440)], as both keys have the same hash index

