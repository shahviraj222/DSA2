# rotating matrix(n*n) to 90 degree

# methode 1:
def bruteRotate(arr):
    n = len(arr)
    ans = [[0 for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        for j in range(n):
            ans[j][(n-1)-i] = arr[i][j]

    print(ans)

bruteRotate([[1,2,3],[4,5,6],[7,8,9]])

# method 2: 
# step 1 : Transpose the matrix
# step 2 : Reverse the row

def optimalRotate(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]  #swaping arr[i][j] , arr[j][i]

    for i in range(n):
        arr[i].reverse()

    print(arr)


optimalRotate([[1,2,3],[4,5,6],[7,8,9]])    
            