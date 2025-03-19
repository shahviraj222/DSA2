# problem: return element that occur more then ⌊n/2⌋


# method1:
def majorityBruteForce(arr):
    for i in range(0,len(arr)):
        count = 0
        for j in range(0,len(arr)):
            if arr[i]==arr[j]:
                count+=1  
        if count > (len(arr)//2):
            return arr[i]
print(majorityBruteForce([23,23,42,34,34,34,34]))

# method2:Hashing
def majority(arr):
    n = len(arr)
    m = n//2
    map={}
    for i in arr:
        if i in map:
            map[i]+=1
        else:
            map[i]=1
    
    for i in arr:
        if map[i]>m:
            return i
        
print(majority([23,23,42,34,34,34,34]))


# method3 : mooones voting algorithm
def majorityMoonesAlgo(arr):
    element = 0
    count = 0
    for i in range(0,len(arr)):
        if count == 0:
            count = 1
            element = arr[i]
        elif arr[i]==element:
            count+=1
        else:
            count-=1

# checking number apper n//2 times or not
    count = 0
    for i in range(len(arr)):
        if arr[i] == element:
            count+=1

    if count>len(arr)//2:
        return element                            
print(majorityMoonesAlgo([23,42,34,34,34,34,34,34]))
