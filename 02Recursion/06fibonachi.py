# fibonachi series      1 1 2 3 5 8
# counting is done from 1 onwards [ not include 0 ]

def recfibona(n):
    if n <= 1:
        return n
    first = recfibona(n-1)
    second=recfibona(n-2)
    return first + second

def fibona(n):
    a = 1                   #first
    b = 1                   #second
    if n == 1 or n==2:
        return 1

    for i in range(3,n+1):
        next = a+b
        a = b
        b = next

    return next

def printfibona(n):
    a = 1
    b = 1
    if n == 1:
        print(1,end=", ")
        return True 
    
    if n == 2:
        print(1,end=", ")
        return True
    
    for i in range(3,n+1):
        next = a+b
        a = b
        b = next
        print(next,end=", ")

n = 6 
print(recfibona(n))
print(fibona(n))
printfibona(n)
