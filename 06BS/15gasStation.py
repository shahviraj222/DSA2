# problem: minimize max distance between two gas station

def gasstation(arr,k):
    howMany = [0 for i in range(0,(len(arr)-1))]
    for gas in range(1,k+1):
        maxiValue = -1
        maxIndex = -1
        for i in range(0,len(arr)-1):
            differ  = arr[i+1]-arr[i]
            sectlen = differ/(howMany[i]+1)
            if maxiValue < sectlen:
                maxiValue = sectlen
                maxIndex = i
        howMany[maxIndex]+=1

    maxans = -1
    for i in range(0,len(arr)-1):
        sectlen = (arr[i+1]-arr[i])/(howMany[i]+1) 
        if maxans < sectlen:
            maxans = sectlen

    return maxans

print(gasstation([1,2,3,4,5,6,7],6))               