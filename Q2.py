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
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
    
    def unshift(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            temp = self.head
            self.head = newNode
            newNode.next = temp
        self.length += 1
newNode = LinkedList("1")
newNode = newNode.insert_at_end("2")
newNode.insert_at_end("3")
newNode.insert_at_end("4")
newNode.insert_at_end("5")
newNode.insert_at_end("6")
newNode.print()
newNode.unshift("0")
newNode.print()
