# problem: Find the length of loop in linked list

# method 1: add all the linked in map and check the node is alredy in map (with timer) or not if it is present 
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def find_loop_length_with_hash(head):
    visited = set()
    current = head

    while current:
        if current in visited:
            # Loop detected; now count the loop length
            loop_node = current
            count = 1
            current = current.next
            while current != loop_node:
                count += 1
                current = current.next
            return count
        visited.add(current)
        current = current.next
    return 0  # No loop

# Helper to create a loop for testing
def create_loop(head, pos):
    if pos == -1:
        return
    loop_start = head
    for _ in range(pos):
        loop_start = loop_start.next
    end = head
    while end.next:
        end = end.next
    end.next = loop_start

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

create_loop(head, 2)  # Loop starting at node 3

length = find_loop_length_with_hash(head)
print("Length of loop:", length)


# method 2: using tortoise algorithm
# when the both pointer colied take counter from there and take pointer and complete entire loop with one pointer as refrence







