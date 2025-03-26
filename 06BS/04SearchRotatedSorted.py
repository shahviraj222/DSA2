# problem: search the element in the rotated sorted  (unique element)
def searchElement(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high) // 2
        if arr[mid] == target:
            return mid
        # finding which side is sorted
        
        # left side is sorted
        if arr[low]<=arr[mid]:
            # element lies on left side
            if arr[low] <= target and target <= arr[mid]:
                high = mid - 1
            # element lies on right 
            else:
                low = mid + 1   

        # right side is sorted  
        else:
            # element lies on right 
            if arr[mid] <= target and target <= arr[high]:
                low = mid + 1
            # element lies on left side
            else:
                high = mid - 1    
    return -1

print(searchElement([4,5,6,7,0,1,2],0))            

# problem : search target element in the rotated array (duplicates allowed)

def searchElementDuplicate(arr,target):
    n = len(arr)
    low = 0
    high = n-1

    while low<=high:
        mid = (low+high) //2
        if arr[mid] == target:
            return True
        # extra code
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low = low + 1
            high = high -1

        if arr[low]<=arr[mid]:
            if arr[low]<= target and target<=arr[mid]:
                high = mid - 1
            else:
                low = mid + 1    

        else:
            if arr[mid]<= target and target<= arr[high]:
                low = mid + 1
            else:
                high = mid - 1            

        return False

print(searchElementDuplicate([2,5,6,0,0,1,2],0))
