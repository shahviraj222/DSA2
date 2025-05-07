# Problem: Reverese a linked list 

# methode1 : changing data 
# take a stack and store all the data into it and then take all element one by one and re store into the the linkedlist.
# Timecomplexity O(n)
# SpaceComplexity O(n)

# methode2 : Reverse links
# with the help of three pointer reverse linked list
# prev temp front
def reverse():
    head = 1
    temp = head
    prev = None
    while temp != None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev    