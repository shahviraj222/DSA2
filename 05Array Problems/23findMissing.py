#Problem: find the missing and repating number from the array

# hashmap[arr[i]] = hashmap.get(arr[i],0)+1 get method is used to get arr[i] if not present return 0 and +1 means increament by 1 


# method1: Brute Force
def missingAndRepeating(arr):
    missing = -1
    repating = -1
    for i in range(1,len(arr)):
        count=0
        for j in range(len(arr)):
            if i == arr[j]:
                count+=1
        if count == 2:
            repating = i
        if count == 0:
            missing = i
    return [missing,repating]

print(missingAndRepeating([4, 3, 6, 2, 1, 1]))
# TimeComplexity O(n^2)

# method2:Hashing method
def missingAndRepeating2(arr):
    hashmap = {}
    repeating = 0
    missing = 0
    for i in range(len(arr)):
        hashmap[arr[i]] = hashmap.get(arr[i],0)+1  #get method is used to get arr[i] if not present return 0 and +1 means increament by 1

        # if arr[i] in hashmap:
        #     hashmap[arr[i]]+=1
        # else:
        #     hashmap[arr[i]]=1

    for i in range(1,len(arr)+1):
        if i in hashmap:
            if hashmap[i]==2:
                repeating = i
        else:
            missing = i
        if repeating and missing:
            break            

    return [missing,repeating] 

print(missingAndRepeating2([4, 3, 6, 2, 1, 1]))  
# time complexity O(n)
# space complexity O(n) 


# method3: using maths behind this

# x = repeating element , y = missing element , s = [given array sum] , sn = [sum of n natural number]
# s2 = [given array sequare sum] , s2n = [sum of sequare of n natural number]
# x-y = s -sn , (x+y) * (x-y) = s2 - s2n
def missingAndRepeating3(arr):
    n = len(arr)
    s1n = (n* (n+1))/2
    s2n = (n*(n+1)*(2*n+1))/6
    s1 = 0
    s2 =0
    for num in arr:
        s1+=num
        s2+=num*num
    val1 = s1-s1n
    val2 = (s2-s2n)/val1
    x = (val1+val2) / 2
    y = val2 - x
    return [int(y),int(x)]

print(missingAndRepeating3([4, 3, 6, 2, 1, 1]))
