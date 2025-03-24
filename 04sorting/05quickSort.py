# finding the correct index for the pivot element (sorting pivot element)

# idea is all the left side element smaller and all the right side element grater

def partition(arr,low,high)->int:
    pivot = low
    i = low+1
    j = high
    while True:
        # here i = high so never goes index out of range error.
        while (arr[i]<=arr[pivot] and i<=high):
            i+=1
        while (arr[j]>arr[pivot] and j>=low):
            j-=1
        if i<j:
            arr[i],arr[j]  = arr[j],arr[i]

        else:
            break    
        
    arr[pivot],arr[j] = arr[j],arr[pivot]        
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