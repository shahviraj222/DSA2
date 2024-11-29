a = ["apple", "banana", "cherry"]
print("List :",a[:], "Element Accessing :",a[1])

a[1] = "kiwi"
print("Editied Element In List :",a)

a.append("strawberry")
print(a)

a.insert(4,"lemon")  #insert at index not replace
print(a)

a.remove("lemon2")
print(a)

b = a.pop(0)
print(a)
print(b)


# Sort funciton closest with 70 comes first 
def sortwith70(a):
    return abs(a-70)

num = [73,55,46,95,67,86,84]
num.sort(key = sortwith70 )     
print(num)

num = [73,55,46,95,67,86,84]
num.sort(reverse = True)     
print(num)