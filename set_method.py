#set uses the clear method and using copy method and using pop method but this method in set it appear random item and set is uniq
#method number one is union() it uses to marge two sets or more with them
a={1,2,3,4,5}
b={6,7,8,9,10}
print(a | b) # we can make marge using this way
print(b.union(a))
#method number two is add use to add item to set
c={1,2,3,4,5}
c.add("ahmed")
print(c)
#method number three is remove is used to remove the element that i give to method if i want remove item is not there in set the method give me error
d={1,2,3,4,5,6,7,"error"}
d.remove('error')
print(d)
#method number four is discard is used to remove the element that i give to method if i want remove item is not there in set the method no give me error
e={1,2,4,3,6}
e.discard(3)
print(e)
#method number five is update use to marge the set with set or set with list or set with tuple  
f={1,2,3,4,5,6,7,8}
f.update((9,10))
print(f)
#method number six is difference is use to show the difference between two sets
g={1,2,3,4}
h={1,2,3}
print(g-h)
print(g.difference(h))
print(g)
#method number seven is difference_update use to show the difference between two sets and update the origin set by differences
j={1,2,3,4}
i={1,2,3}
print(j-i)
j.difference_update(i)
print(j)
#method number eight is intersection use to show the common items between sets
one={1,2,3,4,5,6}
two={1,7,8,3,9,5}
print(one)
print(one & two)
print(one.intersection(two))
print(one)
#method number nine is intersection_update use to show the common items between two sets and update the origin set by commons
j={1,2,3,4}
i={1,2,3}
print(j&i)
print(j)
j.intersection_update(i)
print(j)
#method number ten is symmetric_difference use to show the item that not there between two sets
three={1,2,3,4}
four={1,4,5,6}
print(three^four)
print("="*55)
print(three.symmetric_difference(four))
#method number ten is symmetric_difference_update use to show the item that not there between two sets and updates the origin sets by the result
three={1,2,3,4}
four={1,4,5,6}
print(three^four)
print("="*55)
three.symmetric_difference_update(four)
print(three)
print("="*55)
#method number eleven is issuperset return true or false if the all item in second set is there in first set or no
j={1,2,3,4}
i={1,2,3}
print(j.issuperset(i))#true
#method number twelve is issubset return true or false if the all item in first set is there in second set or no
j={1,2,3,4}
i={1,2,3}
print(j.issubset(i))#false
#method number thirteen is isdisjoint
j={1,2,3,4}
i={1,2,3}
print(j.isdisjoint(i))#false
z={1,1,1,1}
print(z)