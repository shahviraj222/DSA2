import math
def print1(n):
    for num in range(1,n+1):
        for col in range(1,n+1):
            print("* ",end="")
        print()    

def print2(n):
    print("Second Pattern")
    # *
    # **   
    # ***

    for row in range(1,n+1):
        for col in range(1,row+1):
            print("* ",end="")
        print()    

def print3(n):
    print("Third Pattern")
    # ***
    # **    
    # *

    for row in range(1,n+1):
        for col in range(1,n+2-row):
            print("* ",end="")
        print() 

def print4(n):
     for row in range(1,n+1):
        for col in range(1,row+1):
            print(col,end="")
        print()    

def print5(n):
    #   *
    #  ***
    # *****
    
     for row in range(1,n+1):
        
        # space
        for col in range(1,n+1-row):
            print(" ",end=" ")

        # star
        for col in range(1,((2*row)-1)+1):
            print("*",end=" ")

        # space not necessary
        for col in range(1,n+1-row):
            print(" ",end=" ")
            
        print()    

def print6(n):
# * * * * * * * 
#   * * * * *   
#     * * *     
#       *      
    for row in range(1,n+1):

        # space
        for col in range(1,row):
            print(" ",end=" ")
        # star
        for col in range(1,(((n-row)*2)+1)+1):
            print("*",end=" ")
        # space
        for col in range(1,row):
            print(" ",end=" ")

        print()    

def print7(n):
    print5(n)
    print6(n) 

# 
def print8(n):
# *
# **
# ***
# ****
# ***
# **
# *
    for row in range(1,((2*n)-1)+1):
        star = row
        if(row>n):
            star = n - (row-n)
        for col in range(1,star+1):
            print("*",end="")
        print()   

#
def print9(n):
    for row in range(1,n+1):
        for col in range(1,row+1):
            print((int(not(row+col) % 2)),end="")
        print()    

def print10(n):
    for row in range(1,n+1):
        # Numbers
        num = row
        for col in range(1,num+1):
            print(col,end="")

        # Space
        s = (n-row)*2 
        for col in range(1,s+1):
            print(" ",end="")

        # Numbers
        for col in range(row,0,-1):
            print(col,end="")
        print()

def print11(n):
# ABCDEF
# ABCDE
# ABCD
# ABC
# AB
# A    
    for i in range(1,n+1):
        for j in range(65,65+n-i+1):
            print(chr(j),end="")
        print()    

def print12(n):
# *      *
# **    **
# ***  ***
# ********
# ***  ***
# **    **
# *      *
    for row in range(1,((2*n)-1)+1):
        num = row
        if row > n:
            num = 2*n-row
        # star
        for col in range(1,num+1):
            print("*",end="")

        # space
        for col in range(1,((n-num)*2)+1):
            print(" ",end="")

        # start 
        for col in range(1,num+1):
            print("*",end="")

        print("")

def print13(n):
    for row in range(1,n+1):
        # start
        num = row
        if row ==1 or row == n:
            for col in range(1,n+1):
                print("*",end="")
            print("")    
        else:
            for col in range(1,2):
                print("*",end="")
            
            temp = n-2  

            for col in range(1,temp+1):
                print(" ",end="")

            for col in range(1,2):
                print("*",end="")
            print("")    

# 
def print14(n):
# 33333
# 32223
# 32123
# 32223
# 33333
    for row in range(1,2*n):
        for col in range(1,2*n):
            top = row-1
            bottom = ((2*n)-1)-row
            left = col-1
            right = ((2*n)-1)-col
            print(n-min(min(top,bottom),min(right,left)),end="")
        print("")


n = 3
print14(n)

