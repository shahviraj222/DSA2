# 1 recursion function
# 2 base condition
# 3 stack overflow
def recursionfun(i,n):
    # base condition
    if i > n :
        return
    print(i,"Viraj")
    i = i +1
    recursionfun(i,n) 

recursionfun(1,5)    