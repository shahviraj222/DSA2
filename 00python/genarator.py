# genarator same as yeild one
a = (i for i in range(0,10))
print(next(a))    

# how the loop works 
a = [23,24,34]
a = a.__iter__()
print(a.__next__()) 
print(next(a)) 
print(next(a)) 

# enumerate (0,1) (1,34) (2,43)
a = [1,34,43]
a = enumerate(a)
for i in a:
    print(i)


# making over class iterable
class User:
    def __init__(self, user_id, name, email, age):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.age = age
    
    def __iter__(self):
        # iterate over specific attributes
        return iter([self.user_id, self.name])

user = User(101, "Alice", "alice@example.com", 25)
        # Iterate over the User object
for property in user:
    print(property)



