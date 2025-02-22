def getSecondLargest(arr):  
        #1 sort the array.
    sortedArr = sorted(arr)
    n = len(arr)
    largest = sortedArr[n-1]
    secondlargest = -1
        
        #2 if any duplicate then finding other largest.
    for i in range(n-2,-1,-1):
        if sortedArr[i] != largest:
            secondlargest = sortedArr[i]
            break
            
    return secondlargest

def getSecondLargest2(arr):
    largest = max(arr)
    secondLargest = -1
    for i in range(0,len(arr)):
        if secondLargest < arr[i] and arr[i]!=largest:
            secondLargest = arr[i]
    return secondLargest
        
print(getSecondLargest([343,453,543,543,4,3,5,2,34,3,234]))
print(getSecondLargest2([343,453,543,543,4,3,5,2,34,3,234]))