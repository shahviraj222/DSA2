"""
Selection Sort  : Algo take minimum swapping is done O(n). Time Complexity is O(n^2).
Idea: Find the element for the given index.
Each pass you got the minimum element of array.
It is not adaptive and also not stable.
"""

a = [8,6,3,2,5,4,1]

for i in range(0,len(a)-1):
    j = i
    k = i
    while j<len(a):
        if a[k] > a[j]:
            k = j
        j += 1 
    temp = a[i]    
    a[i] = a[k]
    a[k] = temp

print(a)    
