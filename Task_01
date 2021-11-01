# Cache is implemented as queue with arrays. 
# One array for keys, another array for values
# FIFO, first in first out. Enqueue last element (newest), dequeue front element (oldest) if cache is full

class LRU_Cache(object): 

    def __init__(self, capacity):
        # Initialize class variables
        if isinstance(capacity,type(None)):
            print("error: capacity must not be None")
            return
        if type(capacity) is not type(None) and capacity <= 0:
            print("error: capacity must be > 0")
            return
        self.cap = capacity   
        self.arr_keys = [0 for _ in range(self.cap)]       # array for keys
        self.arr_values = [0 for _ in range(self.cap)]     # array for values
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0
        
    def get(self, key):
        # Retrieve element from provided key. Return -1 if nonexistent. 
        # If existent, the element is removed and then appended to end of array, to mark it as most recently used
        if key in self.arr_keys:
            index = self.arr_keys.index(key)
            tmp =  self.arr_values[index]
            self.arr_keys.pop(index)            
            self.arr_keys.append(key)           
            self.arr_values.pop(index)          
            self.arr_values.append(tmp)        
            return tmp				
        else:
            return -1

    def set(self, key, value): 
        # if key is not present and cache is full, remove oldest element
        if key not in self.arr_keys and self.queue_size == self.cap:		
            self.handle_cache_capacity_full()

        # Set the value if the key is not present in the cache
        if key not in self.arr_keys:
            self.arr_keys[self.next_index] = key
            self.arr_values[self.next_index] = value
            self.queue_size += 1
            self.next_index += 1
            if self.front_index == -1:
                self.front_index = 0
        # if key is present in cache, replace its value 
        elif key in self.arr_keys:
            index = self.arr_keys.index(key)
            self.arr_values[index] = value

    def handle_cache_capacity_full(self):
        # dequeue front element (oldest), then append a last (zero) element 
        self.arr_keys.pop(0)
        self.arr_values.pop(0)
        self.arr_keys.append(0)
        self.arr_values.append(0)
        self.next_index -= 1
        self.queue_size -= 1


print("Test case 1")

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


print("Test case 2")

our_cache2 = LRU_Cache(5)
our_cache2.set(3, 3)
our_cache2.set(6, 4)
our_cache2.set(6, 0)	     # overwrite an existing key
our_cache2.set(99, None)     # edge case: Value is None
print(our_cache2.get(6))      # returns 0
print(our_cache2.get(99))     # returns None


print("Test case 3")
our_cache3 = LRU_Cache(-1)   # edge case: returns error: capacity must be > 0


print("Test case 4")
our_cache3 = LRU_Cache(0)   # edge case: returns error: capacity must be > 0

print("Test case 5")
our_cache4 = LRU_Cache(None)   # edge case: returns error: capacity must not be None
