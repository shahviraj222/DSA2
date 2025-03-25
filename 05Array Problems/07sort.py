# Problem1:  sort array that contain 0,1,2.


# methode 1:

a = sorted([0,1,2,0,1,2,0,2,2,2,2])
print(a)
# timsort is used by python  (mergesort + selectionsort)
# bestcase O(n)
# averagecase O(nlog(n))



# method 2:
def sort(arr):
    count0,count1 = 0,0
    for i in range(0,len(arr)):
        if arr[i] == 0:
            count0 += 1
        if arr[i] == 1:
            count1 += 1

    for i in range(0,count0):
        arr[i] = 0

    for i in range(count0,count0+count1):
        arr[i] = 1

    for i in range(count0+count1,len(arr)):
        arr[i] = 2

    print(arr)

sort([0,1,2,0,1,2,0,2,2,2,2])
# Time Complexity  O(n)

# method 3: Dutch National Flag Algorithm
# idea : three pointer low , mid , high

def sortalgo(arr):
    low , mid = 0, 0
    high = len(arr)-1
    while(mid <= high):
        if arr[mid] == 0:
            arr[mid],arr[low] = arr[low],arr[mid]
            mid+=1
            low+=1
        elif arr[mid] == 1:
            mid+=1

        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1
    print(arr)                

sortalgo([2,0,2,1,1,0])    
# Time Complexity O(n)