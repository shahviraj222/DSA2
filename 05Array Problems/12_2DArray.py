def makerow(i,arr):
    for j in range(len(arr[0])): #number column
        if arr[i][j] != 0:
            arr[i][j] = -1

def makecolum(j,arr):
    for i in range(0,len(arr)): #number row
        if arr[i][j] != 0:
            arr[i][j] = -1

def Brute_2dmatrix(arr):
    n = len(arr)  #number of rows
    m = len(arr[0]) #nummber of column
    for i in range(0,n):
        for j in range(0,m):
            if arr[i][j] == 0:
                makerow(i,arr)
                makecolum(j,arr)

    for i in range(0,n):
        for j in range(0,m):
            if arr[i][j] == -1:
                arr[i][j] = 0

    print(arr)

Brute_2dmatrix([[1,1,1],[1,0,1],[1,1,1]])


# method 2 : better solution marking the row and column who has zero
def better_2dmatrix(arr):
    n = len(arr)
    m = len(arr[0])
    row = [0] * n
    col = [0] * m
    for i in range(0,n):
        for j in range(0,m):
            if arr[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for i in range(0,n):
        for j in range(0,m):
            if col[j] == 1 or row[i] == 1:
                arr[i][j] = 0

    print(arr)

better_2dmatrix([[1,1,1],[1,0,1],[1,1,1]])

# method3: Optimum solution
# removing extra space we are using.