"""
Types Of Sorting
    1)Comparision Sort  = bubble, insertion
    2)IndexBased Sort   = count sort , bucket/bin sort

Insertion sort usefull for the link list O(n)
For Array Insertion Sort O(n^2)


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