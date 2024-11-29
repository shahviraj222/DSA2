a = [2,34,5,6,1]

def func():
	for i in a:
		yield i
    
thislist = [100, 50, 65, 82, 23]

thislist.sort(key = func())

print(thislist)
