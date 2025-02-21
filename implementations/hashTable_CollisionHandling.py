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
        for element in self.arr[h]:
            if element[0] == key: # resolves the issue of collision handling by checking if the key is the same
                return element[1] # returns the value of the key, big O(n) operation because we need to traverse the list at the hash index
        return self.arr[h] 
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index] # deletes the key-value pair at the hash index, big O(n) operation because we need to traverse the list at the hash index
        
t = HashTable()

# print(t.get_hash('march 6')) # 9
# print(t.get_hash('march 12')) # 54
# print(t.get_hash('march 21')) # 54


t['march 17'] = 459 # 63
t['march 21'] = 140 # 54
t['march 12'] = 440 # 54, same hash index as march 21
del t['march 12']
del t['march 21']

print(t['march 17']) 
print(t['march 21'])
print("Now:", t['march 12']) # returns 440 because it was the last value stored at the hash index

