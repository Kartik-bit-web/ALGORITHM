# ALGORITHM

# Single Linked List 

class Node:
    def intialIt(self,data):
        self.data = data
        self.next = None

class PrintI:
    def intialIt(self):
        self.head = None
        
    def printStat(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

obj = PrintI()
obj.head = Node(1)
second = Node(2)

obj.head.next = second

obj.printStat()