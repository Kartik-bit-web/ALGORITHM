# ALGORITHM

# Single Linked List 

# create the Node class, and entered the data and the place of next define None becouse  single Node has None in the end.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# here we again use class for initial head with set None becouse there is None Nodes from stating.
# then using method which we make variable name temp and print 

class PrintI:
    def __init__(self):
        self.head = None
         
# Now Print the vlaues of linked list:-
# printStat, now we make variable who assign the value of self.head.
# Using Itration if temp found then print(it's data).
# Now make data.next  which is variable is temp = temp.next

    def printStat(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

# after this we should take Object of PrintI and PrintI has Constructor name called head. 
# In head variable we stored the Node class and gave the constuctor value of data variable.
# now make obj.head first Node and next going to pointer the second one or none value using obj.head.next is second Node data.

obj = PrintI()
obj.head = Node(1)
second = Node(2)

#here we gave address to second data else it will be None

obj.head.next = second

# here we call the method of obj object which on gave us the LinkedList Result.

obj.printStat()