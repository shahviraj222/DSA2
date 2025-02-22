# Problem 1 : Rotate Array to left one space

def rotateLeft(arr):
    for i in range(0,len(arr)-1):
        # first element saved
        if i == 0:
            temp = arr[i]

        # rest element swifting.
        arr[i] = arr[i+1]

        # last element updated
        if i ==  len(arr)-2:
            arr[i+1] = temp
    print("Rotated Elements:",arr)
    
rotateLeft([23,232,323])

# problem 2 : Rotate Array upto D

def rotateLeftD(arr,d):
    n = len(arr)
   
    d = d % len(arr)          # if d = 7 original postion we got.

    temp = arr[:d]            #store original element.

    for i in range(d,n):      #swifiting element.  
        arr[i-d] = arr[i]

    for j in range(len(temp)):  # copy pasting rest of element.
        arr[n - d + j] = temp[j]    
    print("Rotated Array Dth Times:",arr)

rotateLeftD([1,2,3,4,5],2)


# problem 3: Moves Zeroes at end
def moveZeroEnd(arr):
    i = 0
    n = len(arr)
    if n == 1:
        return
    for j in range(n):
        if arr[j] != 0:                     
            arr[i], arr[j] = arr[j], arr[i]  # Swap
            i += 1                           # Move the pointer forward
    print(arr)

moveZeroEnd([3,0,0,3,1])

