def sum(i,n):
    if i > n:
        return 0
    
    return i+sum(i+1,n)



def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

n=4
print("Sum:",sum(1,n))
print("Factorial:",factorial(n))
