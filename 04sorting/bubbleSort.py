"""

    In sorting we have two things one is adaptable and other is stable or not.
    adaptable = if flag is sorted is there any swapping happening. 
    stable =  if the array contain  duplicate then weather they are in the give position or not?

"""


a = [12, 233, 34, 3, 4, 35, 4, 5, 4, 54, 322, 54]
# a = [2,34,45]

flag = 0
for i in range(0, len(a)):
    for j in range(0, len(a) - i - 1):
        if a[j+1] < a[j]:
            flag += 1
            temp = a[j+1]
            a[j+1] = a[j]
            a[j] = temp
    if not flag:
        break 

print(a,flag)


# Complexity of the Bubble Sort is O(n^2)