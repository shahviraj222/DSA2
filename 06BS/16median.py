# problem : Find the median of two sorted array

def median(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i,j = 0,0
    arr3 = []

    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1

    while i<n1:
        arr3.append(arr1[i])
        i+=1
    while j<n2:
        arr3.append(arr2[j])
        j+=1

    n3 = len(arr3)
    if n3%2 == 1:
        return arr3[n3//2]
    else:
        return (arr3[n3//2]+arr3[n3//2-1])/2

print("Even Median:",median([1,2],[3,4]))
print("Odd Medain:",median([1,2],[2]))


# no need to store the merged array we find out the element that requried and store.
def median2(arr1,arr2):
    i,j = 0,0
    n1 = len(arr1)
    n2 = len(arr2) 
    n = n1+n2
    index1 = n//2
    index2 = index1-1
    count = 0
    element1 = -1
    element2 = -1

    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            if count == index1:
                element1 = arr1[i]
            if count == index2:
                element2 = arr1[i]
            count+=1    
            i+=1    
        else:
            if count == index1:
                element1 = arr2[j]
            if count == index2:
                element2 = arr2[j]
            count+=1    
            j+=1
    
    while i<n1:
        if count == index1:
            element1 = arr1[i]
        if count == index2:
            element2 = arr1[i]    
        i+=1
        count+=1
    while j<n2:
        if count == index1:
            element1 = arr2[j]
        if count == index2:
            element2 = arr2[j]
        j+=1
        count+=1

    if n%2 == 1:
        return element1

    return (element1+element2)/2


print("Even Median:",median2([1,2],[3,4]))
print("Odd Medain:",median2([1,2],[2]))

# watch the video 2 applying binary search to take element form the arrays that we have 
def median3(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    n = n1+n2
    if n1>n2:
        return median2(arr2,arr1)   # we always peform binary search on sorter side
    low = 0
    high = n1
    left = (n1+n2+1)//2            # formula
    while low<=high:
        mid1 = (low+high)//2
        mid2 = left - mid1      # how many element from second array
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')
        if mid1 <n1:
            r1 = arr1[mid1]
        if mid2<n2:
            r2 = arr2[mid2]

        if mid1-1>=0:
            l1 = arr1[mid1-1]

        if mid2-1>=0:
            l2 = arr2[mid2-1]    

        if l1<=r2 and l2<=r1:
            if n%2==1:
                return max(l1,l2)
            return (max(l1,l2)+min(r2,r1))/2
        else:
            if l1>r2:
                high = mid1 -1
            else:
                low = mid1+1    

print("Even Median:",median3([1,2],[3,4]))
print("Odd Medain:",median3([1,2],[2]))             