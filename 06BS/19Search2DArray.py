# Problem: Find the Target Element in the 2D Array  (array is sorted)

# method1: We can pass each and every row to binary search function and check weather it is there or not. ( m * n )
# Time Complexity = O( m * log n )

# method2 : We imagine the array is flat Deriving Formula For converting ( 1d index to 2d cordinate) 
# Formula : row = index // (no of column)  col = index % (no of column) 

def conver1dto2d(a,n):
    row = a//n
    col = a%n
    return row,col

def searchIn2D(arr,target):
    m = len(arr)
    n = len(arr[0])
    low = 0
    high = (m*n) -1 
    while low<=high:
        mid = (low+high)//2
        i,j = conver1dto2d(mid,n)
        if arr[i][j]==target:
            return True
        elif arr[i][j]>target:
            high = mid-1
        else:
            low = mid+1
    return False

print(searchIn2D([[1,2,3,4],[5,6,7,8],[9,10,11,12]],13))        
