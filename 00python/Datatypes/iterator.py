a = [1,2]

I = iter(a)
print(I)
print(I.__next__())
print(I.__next__())


#  file refrence it self is the iterable object so we dont need to do this  I = iter(a)
f = open("/Users/virajshah/Desktop/DSA/00python/Datatypes/List.py")
print(f.__next__())