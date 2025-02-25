#Problem1: Find the missing number in array from 1 to N

def misssingNumber(arr):
    N = max(arr)
    n = len(arr)
    for i in range(1,N):
        flag = 0
        for j in range(0,n):
            if arr[j] == i:
                flag = 1
                break
        if flag == 0:
            return i
        

print(misssingNumber([1,2,3,6,4]))       
#Time Complexity O(n^2)

# method 2
def missingNumberHash(arr):
    N = max(arr)
    hash = [0 for i in range(0,N+1)]
    for i in range(0,len(arr)):
        hash[arr[i]] = 1

    for i in range(1,len(hash)):
        if hash[i] == 0:
            return i
    

print(missingNumberHash([1,2,3,6,4]))       
# Time Complexity O(n)
# Space Complexity O(n)

# method 3 Sum Methode
def missingNmberSum(arr):
    N = max(arr)
    sum = (N * (N+1)) // 2
    sum2 = 0
    for i in range(0,len(arr)):
        sum2+=arr[i]

    return sum - sum2

print(missingNmberSum([1,2,3,6,4]))    
# Time Complexity O(n)
# Space Complexity O(1) 


# Problem2: Return the maximum consecutive of 1.

def maximumConsecutive1(arr):
    temp = 0
    consecutive = 0
    for i in range(0,len(arr)):
        if arr[i]!=1:
            temp = 0
        else:
            temp+=1
            if consecutive<temp:
                consecutive = temp
    return consecutive

print(maximumConsecutive1([1,1,0,1,1,1]))
            


# Problem3 : Find the single appearance of number

# methode 1 :Only work for positive numbers
def singleApperanceHash(arr):
     hash = [ 0 for i in range(max(arr)+1)]
     for i in arr:
         hash[i]+=1

     for i in range(0,len(hash)):
         if hash[i] == 1:
             return i

print(singleApperanceHash([0,0,1,1,2,3,4,4,3,2,5,5,6]))


# method 2 : Using MapData Structure

def singleApperanceMap(arr):
    count={}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for i in arr:
        if count[i] == 1:
            return i            

print(singleApperanceMap([0,0,1,1,2,3,4,4,3,2,5,5,6]))        