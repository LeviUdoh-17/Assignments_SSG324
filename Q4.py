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
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def set(self, pos, data):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        count = 1
        if pos <= 0 or pos > self.length:
            print("Out of range")
        else:
            while count < pos:
                current = current.next
                count += 1
        current.data = data
newNode = LinkedList("1")
newNode = newNode.insert_at_end("2")
newNode.insert_at_end("3")
newNode.insert_at_end("4")
newNode.insert_at_end("5")
newNode.insert_at_end("6")
newNode.insert_at_end("7")
newNode.insert_at_end("8")
newNode.insert_at_end("9")
newNode.print()
newNode.set(6, "Six")
newNode.print()
