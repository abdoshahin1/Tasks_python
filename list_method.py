# method one is append()
mylist = [1,2,2,3]
print(mylist)
mylist.append(55) # add the element to the last that i add to method => 55 to the list => mylist
print(mylist[-1])
print(mylist)
mylist2=[55,66,77,88]
mylist.append(mylist2)
print(mylist[-1])
print(mylist)
print(mylist[-1][3]) # this methods when add a list to list it make the other list a one element in the first list and this way that i used it uses to access the element in list that is inside an other list
#method two is extend()
mylist3=["two","three",11,"a"]
mylist4=[1,2,3,4,5,6,7,8]
mylist3.extend(mylist4) # this method uses to marge two list 
print(mylist3)
# method three is remove() it takes one argument
mylist5=[1,1,2,2,3,3,4,4,5,5,6,6]
mylist5.remove(1) # this method uses to delete the first element form the element that i give to method
mylist5.remove(2) # this method uses to delete the first element form the element that i give to method
mylist5.remove(3) # this method uses to delete the first element form the element that i give to method
mylist5.remove(4) # this method uses to delete the first element form the element that i give to method
mylist5.remove(5) # this method uses to delete the first element form the element that i give to method
mylist5.remove(6) # this method uses to delete the first element form the element that i give to method
print(mylist5)
# method four is sort() it uses to sort the list
mylist6=[20,10,300,-1,-2,-300,0,1]
mylist6.sort()
print(mylist6)
mylist6.sort(reverse=True) # this line uses to sort the list from the biggest to lowest
print(mylist6)
# method five is reverse() it uses to reverse the list
mylist7=[1,1,12,2,2,3,3,"abdo"]
mylist7.reverse()
print(mylist7)
#method six is clear() used to remove all element and the list no
mylist8=[1,2,3,4,5,6,7,8,9]
mylist8.clear()
print(mylist8)
# method seven is copy is used to copy the list in other container
mylist9=[1,2,3,4,5]
a=mylist9.copy()
print(a)
#method eight is count it returns the number of the argument that i give to method 
b=[1,1,2,2,3,3,4,4,5,5,6,6]
print(b.count(1))
#method nine is index it returns the index of the argument that i give to method 
c=[1,2,3,4,5,4]
print(c.index(4))
#method ten is insert it uses to insert element in any place in list it takes two argument the element and the index that will use to detect the place that i will add element it
d=[1,2,3,4,5]
d.insert(0,"test")
print(d)
#method eleven is pop it takes one argument (index) and return the element in this index and remove the last element
c=[1,2,3,4,5,6,7,8,9,10]
print(c.pop(-5))