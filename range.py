"""
for i in range(5):
    print(i)
for i in range(2,7):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(10,0,-2):
    print(i)    

numbers=list(range(5))
print(numbers)

total=0
for i in range(1,11):
    total+=i
    print(total)

list=['a','b',"c",'d']
for i in range(len(list)):
    print(i,list[i])

fl=[1,2,3]
ls=[6,7,8]
fl.extend(ls)
fl.pop()
for i in range(1,5):
    print(fl[i])

a=[1,2,3,4,5]
b=a.pop(2)#empty pops removes the last value,but if we fill it it will remove as a index...
print(a,b)#now this will do that whatever this function removes it will show the number that he removed,outside the list in output...
"""
for o in range(1,6):
    print(o,"hello") 