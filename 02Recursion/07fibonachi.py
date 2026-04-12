#  0 1 1 2 3 5 8 13
#  0 1 2 3 4 5 6 7

# using memoiosataion 

# This is reduce time complexity to O(n)
n = 1000
Fib = [-1]*(n+1)

def fibo(n):
    if n <=1:
        return n
    else:
        if Fib[n-1] == -1:
            Fib[n-1] = fibo(n-1)
        if Fib[n-2] == -1:
            Fib[n-2] = fibo(n-2)

        return Fib[n-1] + Fib[n-2]
    
print(fibo(7))



from functools import lru_cache
@lru_cache(None)
def fibo2(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo2(7))


# | Method                 | Need to pass array? | Clean?    |
# | ---------------------- | ------------------- | --------- |
# | Default argument trick | ❌ No                | 👍 Good   |
# | Global array           | ❌ No                | 👍 Simple |
# | `lru_cache`            | ❌ No                | ⭐ Best    |
