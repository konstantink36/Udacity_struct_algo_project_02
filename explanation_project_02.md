Problem 1 - LRU Cache

The LRU cache is implemented as a queue with arrays. The queue is a F.I.F.O. structure, i.e. first in, first out. 
The oldest element is in the head, the newest element in the tail.
Arrays are well suited for this because elements can be accessed in constant time.

Efficiency:
Accessing elements in arrays (with append, pop etc.) takes constant time O(1). I.e. Time complexity is O(1)
Space complexity is O(n), n is the number of elements in the cache.



Problem 2 - Find files

The search of directories is implemented with a recursive function, the search function calls itself recursively to search sub-directories.
The directory structure is equivalent to a tree, where the nodes are directories and files are leaves. Trees can be efficiently traversed 
with a recursive function.

Efficiency
The recursive function visits each node (directory or file) once, and the work done per node is O(1). 
Therefore the time complexity is O(n), n is the number of directories plus the number of files.

The recursion has to visit all n nodes before getting a result, this creates a memory stack of n stages . 
I.e. the space complexity is O(n).




Problem 3 - Huffman Encoding

Huffmann encoding involves creating a binary tree, which is traversed for encoding and decoding.
The tree is created by means of a priority queue, which is implemented with the python heapq algorithm.
Tree traversal for encoding is implemented with a recursive function, traversal for decoding is done with a simple loop.

Efficiency:
The bottleneck is the priority queue which is implemented with heapq.
Heapq has a time complexity of n log n. Therefore the overall time complexity is O(n log n), n is the number of letters to be encoded.

Space complexity for the binary tree is O(k), k is the number of Nodes in the tree. And O(n) for the decoded text.




Problem 4 - User in group 

The algorithm explores groups and with a recursive function to find users. The function recursively calls itself to search sub groups.
The search structure is equivalent to a tree, where the nodes are groups and users are leaves. Trees can be efficiently traversed 
with a recursive function.

Efficiency:
The recursive function visits each node (group or user) once, the work done per node is O(1). 
The time complexity is O(n), n is the sum of all groups and users.

The recursion has to visit all n nodes before getting a result, this creates a memory stack of n stages . 
Therefore the space complexity is O(n).




Problem 5 - Blockchain

A Blockchain is a sequential chain of records. Each block has a pointer to the previous block, thus it can be implemented as a singly linked list. 
When a block is created is also gets a reference value from the previous block's hash.

Efficiency:
Inserting a block has constant time complexity O(1), as it is simply appended to the head.
Being a linked linked list the space complexity is O(n).




Problem 6 - List union & intersection

The intersection of two linked list is found by following these steps:
Create an empty hash table. Iterate through the first linked list and mark all the element frequency as 1 in the hash table. This step takes O(m) time. 
Iterate through the second linked list and if current element frequency is 1 in hash table mark it as 2. This step takes O(n) time. 
Now iterate though the hash table to check the frequency of elements. Elements with frequency of two are present in the intersection of the two linked lists.
The union of two linked lists is found in a similar way, except that all elements of the hash table represent the union of the two lists.

Efficiency:
Time complexity of this method is O(m + n ), m and n the number of elements in list 1 and 2 respectively.
Space complexity is also O(m + n), i.e. the elements of the two lists all have to be placed in memory.
