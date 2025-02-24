# problem1 : say array is sorted or not?
def arrayIsSorted(arr):
    for i in range(0,len(arr)-1):
        if not arr[i+1] >= arr[i]:
            return False

    return True


print(arrayIsSorted([34,4445,54454,5554]))

# problem2 : remove duplicate and return number of unique element 

# method 1
def removeduplicate(arr):
    mySet = set()
    for i in  range(0,len(arr)):
        mySet.add(arr[i])

    return len(mySet)     

# method 2 error
def removeduplicate2(arr):
    i = 0
    for j in range(1,len(arr)):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i +=1
    print(arr)         
    return i+1


print(removeduplicate([1,2,3,1,1,2,3]))
print(removeduplicate2([1,2,3,1,1,2,3]))
