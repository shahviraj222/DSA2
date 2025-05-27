# Problem : Remove the duplicate values from the sorted doubly linkedlist.

def removeduplicate(head):
    temp = head
    while temp and temp.next:
        nextNode = temp.next
        while nextNode and nextNode.value == temp.value:
            nextNode = nextNode.next

        temp.next = nextNode
        if nextNode:
            nextNode.prev = temp

