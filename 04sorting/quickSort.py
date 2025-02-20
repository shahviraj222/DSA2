# finding the correct index for the pivot element (sorting pivot element)

# idea is all the left side element smaller and all the right side element grater

def partition(arr,low,high)->int:
    pivot = low
    i = low
    j = high
    while (i<j):
        while (arr[i]<=arr[pivot] and i<=high-1):
            i+=1
        while (arr[j]>arr[pivot] and j>=low+1):
            j-=1
        if i<j:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

    temp = arr[pivot]
    arr[pivot] = arr[j]
    arr[j] = temp
    return j


def quicksort(arr,low,high):
    if low < high:
        pivot = partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)



a = [3,4,56,43]
quicksort(a,0,3)
print(a)


# O(nlogn)