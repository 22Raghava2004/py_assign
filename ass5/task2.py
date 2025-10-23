test=[]

for i in range(10):
    entry1=input("enter the element in  list")
    test.append(entry1)
    
print(test)
test_2=test[0:5]



print(f"the first five elements are {test[0:5]}")
print(f"the reverse of the first five elements{test_2[::-1]}")
