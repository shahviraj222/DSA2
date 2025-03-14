def spiral(arr):
    top,left = 0,0
    right = len(arr[0])-1 #column
    bottom = len(arr)-1   #row
    ans = []
    while left<=right and top<=bottom:
    # right
        for i in range(left,right+1):
            ans.append(arr[top][i])
        top+=1
        # bottom
        for i in range(top,bottom+1):
            ans.append(arr[i][right])
        right-=1

        if top<=bottom:
        # left
            for i in range(right,left-1,-1):
                ans.append(arr[bottom][i])
            bottom-=1
        if left<=right:    
        #up
            for i in range(bottom,top-1,-1):
                ans.append(arr[i][left]) 
            left+=1    
    print(ans)

spiral([[1,2,3],[4,5,6],[7,8,9]])