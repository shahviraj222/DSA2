"""
Selection Sort  :  minimum swapping O(n). swap only coorect value found.
Idea: Find the element for the given index.
Each pass you got the minimum element of array.
It is not adaptive and also not stable.
Time Complexity is O(n^2).
"""

a = [8,6,3,2,5,4,1]

for i in range(0,len(a)-1):
    j = i
    k = i
    while j<len(a):
        if a[k] > a[j]:
            k = j
        j += 1 
    if k != i:    
        temp = a[i]    
        a[i] = a[k]
        a[k] = temp

print(a)    
