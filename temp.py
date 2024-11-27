n=2
def display(c):
    global n
    if(c > n):
        return
    display(c+1)
    print(c)


display(1)