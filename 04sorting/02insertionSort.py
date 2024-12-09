"""
Insertion sort usefull for the link list O(n)
For Array Insertion Sort O(n^2)
Idea : Add the num from last num of array.
"""

a = [12,233,34,3] 
for i in range(1,len(a)):
    key = a[i]
    j = i-1
    # swift if the key is grater then element to be inserted 
    while j >= 0 and a[j]>key:
        a[j+1] = a[j]
        j-=1
    
    a[j+1] = key


print(a)