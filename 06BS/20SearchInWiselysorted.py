# Problem: Searching in matrix that is wisely sorted. (left to right && top to bottom sorted)

def findElement(arr,target):
    m = len(arr)
    n = len(arr[0])
    row = 0
    col = n-1
    while row<m and col>=0:

        if arr[row][col] == target:
            return row,col
    
        elif arr[row][col]<target:
            row+=1

        else:
            col-=1    
    return -1,-1        

