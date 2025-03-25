# problem: Floor Ceil
# floor largest no in array <=  x
# ceil smallest no in array >= x

def floorAndceil(arr, x):
    n = len(arr)
    
    # Initialize ceil and floor
    ceil = -1
    floor = -1

    # Finding ceil (smallest number >= x)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ceil = arr[mid]  # Update ceil
            high = mid - 1   # Move left
        else:
            low = mid + 1

    # Finding floor (largest number <= x)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            floor = arr[mid]  # Update floor
            low = mid + 1     # Move right
        else:
            high = mid - 1

    return floor, ceil  # Return both values

# Testing the function
arr = [1, 2, 8, 10, 10, 12, 19]
x = 9
print("Floor and Ceil:", floorAndceil(arr, x))  # Output: (8, 10)


