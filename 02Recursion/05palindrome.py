def palindrome(a):
    start = 0
    end = len(a) - 1
    while start < end:
        if not a[start].isalnum():
            start +=1
        elif not a[end].isalnum():
            end -=1
        elif a[start] != a[end]:
            return False
        else:
            start +=1
            end -=1     
    return True

#recursive 
def recpalindrome(a,start,end):
    if start >= end:
        return True
    else:
        if a[start] == a[end]:
            return recpalindrome(a,start+1,end-1)        #you have to return the function call else the reslut stuck 
        else:
            return False     

def shortpalindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


a="abaaba"
print(recpalindrome(a,0,len(a)-1))   
print(shortpalindrome(a))             