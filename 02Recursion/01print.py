# 1 recursion function
# 2 base condition
# 3 stack overflow
def recursionfun(i,n):
    # base condition
    if i > n :
        return
    print(i,"Viraj")
    recursionfun(i+1,n) 

recursionfun(1,5)    