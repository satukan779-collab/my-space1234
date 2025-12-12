list =[1,2,3,4,5,6,7,8]
#print(len(list))
list.insert(2,2.5)
list.append(9)
list.extend([9,0])
print(len(list))
print(list)
list1=[1,2,3]
list1.pop(1)#remove the element with index,ex=index is 1,so 1=2,then it will remove the 2...
print(list1)
list3=[1,2,3,4,5,6,7,8]
list3.remove(2)#not include indexing or slicing...
print(list3)
print(list3.index(7))
list3.clear()#remove the complete element from list...
print(list3)
list4=[1,2,3,4,5,6]
print(min(list4))
print(max(list4))
print(list4.count(8))#8 is not avaible in list4,so the output will be print 0,but if 8 is avaible then it will print 1,which menas true,if 0 menas false...
'''
list5=[1,2,3,4,5,6]
list6=list5.copy()
print(list6)
'''
list7=[2,1,3,5,4]
list7.sort()#not work in another available
print(list7)
list8=["e","c","b","d","a","f","g"]#reverse the whole list,means the 1st number wil be last and last number will be 2nd...
list8.reverse()
print(list8)
list9=[1,2,3,4,5,6,7]
print(list9[1:6:2])
a="hello world"
b=",finally the code is working"
c=a+b
print(c)
list10=[1,2,3,4,5]
for i in list10:
    print(i)
list11=[100,200,300,400]
print(100 in list11)
print(500 in list11)
print(300 in list11)
