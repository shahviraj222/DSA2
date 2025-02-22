arr = [23,34,45,23,23,54,34,9,2,2,2,10]
def frequencyCount(arr):
    map = {}
    for i in arr:
        if i in map:
            map[i]+=1
        else:
            map[i] =1
    print(max(map,key=map.get))       # key takes fucntion apply before comparing. 
    print(map)        

frequencyCount(arr)        

# def recursion(n):
#     if n==1:
#         return 0
#     recursion(n-1)
#     print(n)

# recursion(4)


# def selectionSort(a,n):
#     for i in range(0,n):
#         j=k=i
#         while(j<n):
#             if(a[j]<a[k]):
#                 k=j
#             j+=1
#         temp = a[i]
#         a[i] = a[k]
#         a[k] = temp    
#     print(a)

# a =[3,4,61,1]  
# selectionSort(a,4) 
          



# def insertionsort(a,n):
#     for i in range(1,n):
#         j=i-1
#         x=a[i]

#         # swaping
#         while(a[j]>x and j>-1):
#             a[j+1] = a[j]
#             j-=1
#         a[j+1] = x

# a =[3,4,61,1]         
# insertionsort(a,4)
# print(a)

# def bubbleSort(array,size):
    
#     for i in range(0,size):
#         flag = 0
#         for j in range(0,size):
#             if array[j]>array[j+1]:
#                 temp = array[j+1]
#                 array[j+1] = array[j]
#                 array[j] = temp
#                 flag+=1
#         if not flag:
#             break
#     print(array)
# bubbleSort([2,3,454,1],4)



# class PairHash():
#     def __init__(self,size)->None:
#         self.size = size
#         self.table = [[] for _ in range(0,self.size)]
#         # table = [[[k,v]],[]]
#     def _hash(self,key):
#         return hash(key)%self.size
    
#     def insert(self,key,value):
#         index = self._hash(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 pair[1] = value
#                 return True    
#         self.table[index].append([key,value])

#     def delete(self,key):
#         index = self._hash(key)
#         for i,pair in enumerate(self.table[index]):
#             if pair[0] == key:
#                 return self.table[index].pop(i)

#     def search(self,key):
#         index = self._hash(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 return pair[1]
#         return None    

#     def display(self):
#         print(self.table)


# a = PairHash(3)
# a.insert("name","viraj")
# a.insert("age",45)
# print(a.delete("name"))
# a.display()




# class SingleHash():
#     def __init__(self,size)->None:
#         self.sizeTable = size
#         self.table = [[-1]for _ in range(self.sizeTable)]

#     def _hash(self,key) -> int:
#         return hash(key)%self.sizeTable 
      
#     def insert(self,key):
#         index = self._hash(key)
#         self.table[index].append(key)

#     def delete(self,key):
#         index = self._hash(key)
#         if key in self.table[index]:
#             self.table[index].remove(key)
#             return key
#         return False

#     def search(self,key):
#         index = self._hash(key)
#         # here in keyword search as linklist O(n) if multiply element present at one index
#         if key in self.table[index]:
#             return True
        
#         return False

# h1 = SingleHash(9)
# h1.insert(34)
# h1.insert(45)
# print(h1.search(78))
# print(h1.delete(45))
# print(h1.search(45))



# def patter14(n):
#     for row in range(0,n):
#         # star
#         for i in range(1,n-row+1):
#             print("*",end="")

#         # spaces
#         for j in range(1,2*row+1):
#             print(" ",end="")

#         # star
#         for i in range(1,n-row+1):
#             print("*",end="")
#         print()
# patter14(3)

# def print13(n):
#     for row in range(1,n+1):
#         # start
#         num = row
#         if row ==1 or row == n:
#             for col in range(1,n+1):
#                 print("*",end="")
#             print("")    
#         else:
#             for col in range(1,2):
#                 print("*",end="")

#             for col in range(1,n-1):
#                 print(" ",end="")

#             for col in range(1,2):
#                 print("*",end="")
#             print("") 


# print13(5)
# def pattern9(n):
#     for i in range(1,n+1):
#         for j in range(1,n-i+2):
#             print(chr(64+j),end=" ")
#         print("")    
# pattern9(6)

# def pattern8(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(chr(64+j),end="")
#         print()    

# pattern8(6)

# def pattern7(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             if((i+j)%2==0):
#                 print("1",end="")
#             else:
#                 print("0",end="")    
#         print()    

# pattern7(6)


# def print6(n):
#     for row in range(1,n+1):
#         for col in range(1,row):
#             print(" ",end=" ")
#         for start in range(1,2*(n-row)+2):
#             print("*",end=" ")
#         print()

# def print5(n):
#     for row in range(1,n+1):
#         for col in range(1,n-row+1):
#             print(" ",end=" ")
#         for k in range(1,2*row):
#             print("*",end=" ")
#         print()

# print5(5)
# print6(5)   



# def print4(n):
#      for row in range(1,n+1):
#         for col in range(1,row+1):
#             print(col,end="")
#         print()   


# print4(8)

# def pattern(num):
#     for row in range(1,num+1):
#         for col in range(1,row+1):
#             print("*",end=" ")
#         print()
#     for row in range(1,num+1):
#         for col in range(1,num-row+1):
#             print("*",end=" ")
#         print()          
                        

# pattern(8)


# def printAtEnd(i,num):
#     if i>num:
#         return
#     printAtEnd(i+1,num)
#     print(i)

# printAtEnd(1,3)


# def printAtBegining(i,num):
#     if i>num:
#         return 
#     print(i)
#     printAtBegining(i+1,num)

# printAtBegining(1,3)

# def sumRecursivly(i,num):
#     if i>num:
#         return 0
#     return sumRecursivly(i+1,num)+i

# print(sumRecursivly(1,5))


# def palindromRecursive(a,start,end):
#     if start >= end:
#         return True
#     else:
#         if a[start]==a[end]:
#             return palindromRecursive(a,start+1,end-1)
#         else:
#             return False     

# a = "viv"
# print(palindromRecursive(a,0,len(a)-1))

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