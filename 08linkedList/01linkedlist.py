# problem: create a link list 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_Node = Node(data)
        if not self.head:
            self.head = new_Node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_Node

    def prepend(self,data):
        # adding at begining
        new_Node = Node(data)
        new_Node.next = self.head  
        self.head = new_Node

    def print_list(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print("None")    

    def delete_node(self,key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if not current:
            return         

        prev.next = current.next
        current = None


        