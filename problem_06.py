class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    hash = dict()  			# create empty hash table
    union_list = LinkedList()


    a = llist_1.head
    while (a != None):
        hash[a.__repr__()] = 1      # put elements from list1 in hash table
        a = a.next

    b = llist_2.head
    while (b != None):
        if (b.__repr__()) not in hash:  
            hash[b.__repr__()] = 2     # put elements from list2 in hash table, if they do not exist
        b = b.next

    for x in hash.keys():
        union_list.append(x)         # create linked list with union of the two lists

    return union_list



def intersection(llist_1, llist_2):
    hash1 = dict()  			# create empty hash table
    intersection_list = LinkedList()
    
    a = llist_1.head
    while (a != None):
        hash1[a.__repr__()] = 1      # set frequency to 1
        a = a.next

    b = llist_2.head
    while (b != None):
        if (b.__repr__()) in hash1:
            hash1[b.__repr__()] = 2     # if element already exists, set frequency to 2
        b = b.next
        
    for x in hash1.keys():
        if hash1[x] == 2:			# if frequency is 2 it means the element is common
            intersection_list.append(x)         

    return intersection_list
print("Test case 1")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print(intersection(linked_list_1,linked_list_2))
print(union(linked_list_1,linked_list_2))

# This prints in first row a list of intersecting elements: 4 -> 6 -> 21 ->
# and in second row a list of union elements: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->


print("Test case 2")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# This prints in first row a list of union elements: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
# Second row is empty as there are no intersecting elements

print("Test case 3")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1,2,33,6,9,10]
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# This prints in first row a list of union elements: 1 -> 2 -> 33 -> 6 -> 9 -> 10 ->
#  Second row is empty as there are no intersecting elements, since one list is empty 

print("Test case 4")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1,2,33,6,9,10,"b"]
element_2 = ["a", "b", 33]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


# This prints in first row a list of intersecting elements: 1 -> 2 -> 33 -> 6 -> 9 -> 10 -> b -> a ->
# and in second row a list of union elements: 33 -> b ->

print("Test case 5")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
 
# This prints no lists of union or intersection elements, as both lists are empty
