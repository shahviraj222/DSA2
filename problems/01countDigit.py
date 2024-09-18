n = 123342

def countdigit(n):
    counter = 0
    num = n
    while(num>0):
        num = num // 10
        counter+=1

    return counter

print("Number of digits :",countdigit(32583485))

# Complexity O(log N)
# log = base 10
# ln  = base 2 