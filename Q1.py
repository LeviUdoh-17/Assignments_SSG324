class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def insert_at_end(self, data):
        """Adds data at the end, takes parameter data"""
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        print(newNode.data)
        return self
    
    def print(self):
        """Utility Print function, takes no parameter"""
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
    
    def shift(self):
        """Remove data from the beginning"""
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        next = temp.next
        self.head = next
        self.length -= 1

newNode = LinkedList("1")
newNode = newNode.insert_at_end("2")
newNode.insert_at_end("3")
newNode.insert_at_end("4")
newNode.insert_at_end("5")
newNode.insert_at_end("6")
newNode.print()
newNode.shift()
newNode.print()
