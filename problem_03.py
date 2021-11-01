import sys
import heapq

def huffman_encoding(data):
# function reads a string, returns Huffmann encdoded string and the Huffmann tree

# create Node object for Huffmann tree
    class Node(object):
        def __init__(self, left=None, right=None, freq=None, char=None):
            self.left = left
            self.right = right
            self.freq = freq
            self.char = char
        def __lt__(self, other):		# replace < with self.freq < other.freq; thus priority queue will sort nodes based on lowest freq
            return self.freq < other.freq

# create list of freq, character tuples (frequency of each character in "data")
    list = []
    for x in data:
        freq = data.count(x)	
        if (freq, x) not in list:
           list.append((freq, x))

# create priority queue with heapq module; push a node into the queue for each list item 
    queue = []				# priority queue
    for y in list:				
         node = Node(None, None, y[0], y[1])    # create a node with frequency and character initialization
         heapq.heappush(queue, node) 		 # push the node into queue
       

# Build the Huffmann tree    
    while len(queue) > 1:			                      # continue looping until there is only one node (the full tree)
        leftchild = heapq.heappop(queue)  	                      # remove lowest frequency node from queue 
        rightchild = heapq.heappop(queue) 			      # remove next lowest frequency node from queue
        node = Node(leftchild, rightchild, leftchild.freq + rightchild.freq, None )    # create new node that has freq equal to sum of its two childrens's freq
        heapq.heappush(queue, node)   				      # add that node to queue 
      
# Recursively traverse the tree, assign 0 (left) or 1 (right) to each node. Return dictionary with code for each char
    dict = {}					  # dictionary with key = char and value = code
    def createcode(code, node):
        if node.char: 			          # if node is leaf node ( i.e. char = true)
            if not code:			  # if code is empty 
                dict[node.char] = "0"             # add "0" to dictionary
            else: 				  # if code is not empty
                dict[node.char] = code            # add code to dictionary
        else:                                     # if node is not a leaf node
            createcode(code + "0", node.left)     # add 0 to code and recursively walk down left child
            createcode(code + "1", node.right)    # add 1 to code and recursively walk down right child

    root = queue[0]        # root node of tree
    createcode("", root) # create the dictionary
    encoded = "".join([dict[x] for x in data])  # create the code for input data
    
    return  encoded, root



def huffman_decoding(data,tree):
# function reads encoded string and the Huffmann tree, returns decoded string

    decoded = ""
    curr = tree      # set current node to root node

    for x in data:
        if x == "0" and curr.char == None:
            curr = curr.left
        elif x == "1" and curr.char == None:
            curr = curr.right     
        if curr.char:		# if current node is a leaf node (char = true)
            decoded += curr.char    # add character to decoded string
            curr = tree         
   
    return decoded


def printtest(string):
    a_great_sentence = "string"

    print ("The size of the data is: {}\n".format(sys.getsizeof(string)))
    print ("The content of the data is: {}\n".format(string))

    encoded_data, tree = huffman_encoding(string)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))




print("Test 1")

a_great_sentence = "The bird is the word"
printtest(a_great_sentence)


print("Test 2")

a_great_sentence = "banthafodder"
printtest(a_great_sentence)


print("Edge Test 3")

a_great_sentence = "b"
printtest(a_great_sentence)

print("Edge Test 4")

a_great_sentence = " "
printtest(a_great_sentence)
