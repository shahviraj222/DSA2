# finding the correct index for the pivot element (sorting pivot element)

# idea is all the left side element smaller and all the right side element grater

def partition(arr, l, h):
    i = l + 1
    j = h

    while True:
        while i <= j and arr[i] <= arr[l]:
            i += 1
        while i <= j and arr[j] > arr[l]:
            j -= 1
        
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[l], arr[j] = arr[j], arr[l]
    return j


def quicksort(arr, l, h):
    if l < h:
        p = partition(arr, l, h)
        quicksort(arr, l, p - 1)
        quicksort(arr, p + 1, h)
    return arr


print(quicksort([2, 3, 1, 0], 0, 3))

# O(nlogn)