# #fun_01 is all() used to check if all element in the iterable is true or not
# mylist=[1,2,3,4]
# if all(mylist):
#     print('done')
# else:
#     print('there is false')
# #fun_02 is any() used to check if one element in the iterable is true or not
# mylist=[1,0,0,0]
# if any(mylist):
#     print('done')
# else:
#     print('there is false')
# #fun_03 is id() used to return the location of variable in the memory
# print(id(mylist))
# #fun_04 is bin() used to convert the number to binary number
# print(bin(2))
# #fun_05 is sum() used to plus to numbers and takes two argument iterable and start that is number plus over the result from function
# print(sum(mylist))
# #fun_06 is range() used to generate numbers and takes two argument start and end
# # test=range(1, 10)
# # for t in test:
# #     print(t)
# #fun_07 is print() used to print in consol and has some properties such sep used to make symbol between words when use , between string and end that default value is \n that uses to write in newline
# print('ahmed','fouad', end=" ")
# #fun_08 is round() used to 1.5 => 2 and take two argument number and the number of 0.123 that i want to appear it after the point
# print(round(1.5))
# #fun_09 is abs() used to convert the negative value to positive value | | absolute value
# print(abs(-1))
# #fun_10 is min() used to return the minimum value in the iterable
mylist=[1,2,3,4,56]
# print(min(mylist))
# #fun_11 is pow() used to make this equation 2^2=4 there is mod used to make the result of (2**2)%2
# print(pow(2, 2))
# #fun_12 is max() used to return the maximum value in the iterable
# print(max(mylist))
# #fun_13 is slice() used to make slicing into string
# a='abderahman'
# print(a[slice(8)])
# fun_14 is map() used to map the element in the iterable in function
mylist2=[4,6,312,7,3,565,8]
for test in map(lambda num, num1: num + num1, mylist, mylist2):
    print(test)
#fun_15 is filter() used to run a certain function on the element in the iterable
# mylist2=[4,6,312,7,3,565,8]
# for test in filter(lambda num: num == pow(2,3), mylist2):
#     print(test)
#fun_16 is reduce() used to reduce the element in iterable by using the fun that i give it 
# from functools import reduce
# a=reduce((lambda num1, num2 : num1 + num2), mylist2)
# for test in a:
#     print(test)
# fun_17 is enumerate() add counter when use loop such as:
# member_list=["Ahmed","Ali","Abdo","Mohammed","Omer","Hanaa","Fatema","Yassmeen"]
# for counter, name in enumerate(member_list, 2):
#     print(f"counter is {counter} and name is{name.center(len(name)+2)}")
# fun_18 is help() show you explain to certain method such as reduce
# from functools import reduce
# print(help(reduce))
# fun_19 is reversed() reverse the iterable that i give it to it
# name='abdo'
# for n in reversed(name):
#     print(n, end="")
# test
# from functools import reduce
# member_list=["Ahmed", "Ahmed", "Abdo", "Mohammed", "Omer", "Hanaa", "Fatema", "Yasmeen"]
# print(reduce(lambda num1, num2: num1.startswith("A"), member_list))