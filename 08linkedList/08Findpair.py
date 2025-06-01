# Problem : find the pair that gives sum equal to given in sorted doubly linked list 

# sample variables
head = 1
tail_of_linked_list = 2
pair = 2
Key =0

# methode 1: using nested loops
temp1 = head
ds = []
while temp1:
    temp2 = temp1.next
    while temp2:
        if temp1.value + temp2.value == Key:
            ds.add(temp1.value,temp2.value)
        temp2 = temp2.next    
    temp1 = temp1.next





# methode 2: using two pointer left and right

left = head
right = tail_of_linked_list

while left.value < right.value:
    if left.value + right.value == sum:
        ds.add(pair)
        left = left.next
        right = right.prev
    elif left.value + right.value>sum:    
        right = right.prev 
    else:
        left = left.next

 