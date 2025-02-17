def fibonachi(n):
    a = 0
    b = 1
    for i in range(1,n+1):
        print(a)
        temp = a+b
        a = b
        b = temp

def recfibonachi(n):
    if n <= 1:
        return n
    return recfibonachi(n-1)+recfibonachi(n-2)

print("Recursive Fibonachi Series:",recfibonachi(4))
fibonachi(4)