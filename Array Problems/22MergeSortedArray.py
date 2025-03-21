#problem: merge the two array without using extra space 

# method1: here we are usign an extra space
def merge1(arr1,arr2,m,n):
    left = 0
    right = 0
    arr3 = []
    while left<m and right<n:
        if arr1[left]>arr2[right]:
            arr3.append(arr2[right])
            right+=1

        else:
            arr3.append(arr1[left])
            left+=1

    while left<m:
        arr3.append(arr1[left])
        left+=1

    while right<n:
        arr3.append(arr2[right])
        right+=1

    for i in range(m+n):
        if i<n:
            arr1[i] = arr3[i]

        else:
            arr2[i-n] = arr3[i]

    print(arr1,arr2)


merge1([1,2,3],[2,5,6],3,3)
# time complexity O(min(m,n))  
# space complexity O(m+n)

# method2 : here we are swaping the element from one to other arrays.
def merge2(arr1,arr2,n,m):
    left = n-1
    right = 0
    while left>=0 and right<m:
        if arr1[left]>arr2[right]:
            arr1[left],arr2[right] =  arr2[right],arr1[left]
        else:
            break

    arr1.sort()        
    arr2.sort()
    
    print(arr1,arr2)

merge2([1,2,3],[2,5,6],3,3)  

# time complexity O(nlog(n))
# space complexity O(1)

def merge3(arr1,arr2,m,n):
    pass
