myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

a = {"name":"viraj","age":"22"}
print("Simplest Dictionary Printing")
for k,v in a.items():
   print(f"{k} : {v}")

for i,obj in myfamily.items():
    print(i)
    for j in obj:
        print(j , ":" ,obj[j])

for i in range(0,len(myfamily)):
  print(i)
