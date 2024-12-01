def reverse(n):
    isnegative = False
    if not n>=0:
        isnegative = True

    num = abs(n)
    revnum = 0
    while(num>0):
        temp = num %10
        revnum = (revnum*10)+temp 
        num = num // 10
    if isnegative:
        revnum = revnum * -1
    return revnum
n=-121
rev = reverse(n)
if rev == n:
    print("Palindrome")
else:    
    print("Not Palindrome")    


# isalpha()
# isnumeric()