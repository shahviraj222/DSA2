def printAtEnd(i,num):
    if i>num:
        return
    printAtEnd(i+1,num)
    print(i)

printAtEnd(1,3)


# def palindrome(num):
#     start = 0
#     end = len(num)-1
#     while start<end:
#         if num[start] == num[end]:
#             start+=1
#             end-=1
#             continue
#         else:
#             return False

#     return True

# print(palindrome("abaa"))   