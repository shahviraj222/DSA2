# problem1: rearrange array with positive and negative pos.size==negati.size

def rearange(arr):
    positive = 0
    negative = 1
    ans = [0] * len(arr)
    for i in arr:
        if i < 0:
            ans[negative] = i
            negative += 2
        else:
            ans[positive] = i
            positive += 2
    print(ans)

rearange([1,-9,-9,10])               

# Problem2: rearrange array with positive and negative pos.size != neg.size

def rearange2(arr):
    positive =[]
    negative = []
    for i in arr:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)

    if len(positive) > len(negative):
        for i in range(len(negative)):
            arr[2*i] = positive[i]
            arr[2*i+1] = negative[i]

        index =2*len(negative)
        for i in range(len(negative),len(positive)):                
            arr[index] = positive[i]
            index+=1

    else:
         
         for i in range(len(positive)):
            arr[2*i] = positive[i]
            arr[2*i+1] = negative[i]

            index =2*len(positive)
         for i in range(len(positive),len(negative)):                
            arr[index] = negative[i]
            index+=1 

    print(arr)

rearange2([1,-9,-9,10,10,-3,-4,-4])