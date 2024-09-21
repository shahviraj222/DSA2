def startprintpattern(i,n):
    if not i>n:
        print(i)
        startprintpattern(i+1,n)



def tailprintpattern(i,n):
    # printing at the time of coming back
    if i <= n:
        tailprintpattern(i+1,n)
        print(i) 


startprintpattern(1,5) 
tailprintpattern(1,5)