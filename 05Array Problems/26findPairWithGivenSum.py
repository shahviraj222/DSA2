# find pair with given sum unsorted array a+b = k

# method 1 : loops O(n^2) simple 
# if duplicates are there then remove duplicate and then start with same (save computation)

# method 2: Hashing
def pairfind(arr,k):
    hash = [None] * ( max(arr)+1)
    for i in range(0,len(arr)):
        hash[arr[i]] = 1

    for i in range(0,len(arr)):
        if k-arr[i] > max(arr):
            continue
        if hash[k-arr[i]] == 1:
            return (k-arr[i],arr[i])   
        
print(pairfind([1,2,3,4,6],10))     


# method3 best work with all cases also with neagative numbers

def pairfinder(arr,k):
    seen = set()
    for num in arr:
        if (k-num) in seen:
            return (num,k-num)
        seen.add(num)

    return None

print(pairfind([1,2,3,4,6],10))    


# we can do one more thing if array is sorted think !! not find then see (video chapter 7 / 35 no)