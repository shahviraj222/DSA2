# Problem: Find out the longest palindrome form a string

# we have to look for diffrently for even and odd palindrome 
# try to solve in book you get the intuition
 
def expandAroundCentre(left,right,s):
    while (left>=0 and right<len(s)) and s[left]==s[right]:
        left-=1
        right+=1
    return left+1,right-1
    
def longestPalindrome(s):
    if not s and len(s)==1:
        return s
    
    start = 0
    end = 0
    
    for i in range(len(s)):
        left1,right1 = expandAroundCentre(i,i,s)

        left2,right2 = expandAroundCentre(i,i+1,s)

        if right1-left1 > end-start:
            start,end = left1,right1

        if right2-left2 > end-start:
            start,end = left2,right2

    return s[start:end+1]

print(longestPalindrome("12111111"))
            
