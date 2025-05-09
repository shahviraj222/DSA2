# problem : find the loop in the linked list

# methode 1: add all the linked in map and check the node is alredy in map or not if it is present return true else return false

# methode 2 : using tortoise algorithm
def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:  #why we have both 
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

# if we have odd numbers of linked list then fast stand to last node
# if we have even numbers of linkedlist then fast stand on the null node
