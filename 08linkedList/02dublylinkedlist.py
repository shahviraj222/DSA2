class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
       self.head = None

    def append(self,data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        newNode.prev = curr      

    def prepend(self,data):
        newNode = Node(data)
        if self.head:
            newNode.next = self.head
            self.head.prev = newNode 
        self.head = newNode
    
    def delete(self,data):
        curr = self.head
        while curr:
            if curr.data == data:
                if curr.prev:
                    curr.next.prev = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr = curr.next            

    def printForward(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

    def printBackward(self):
        curr = self.head
        if not curr:
            print("None")
            return
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.data,end=" <-> ")
            curr = curr.prev 
        print("None")       

    def reverse(self):
        current = self.head
        temp = None

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp:
            self.head = temp.prev
            
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)

dll.printForward()
dll.printBackward()