#zip() function takes iterable as argument and marge them to using them in for loop and the size of zip depends on the less size of the iterable
lis = [1,2,3,4,5]
lis2 = [6,7,8,9]
for item1, item2 in zip(lis, lis2):
    print("lis items are=> ", item1)
    print("lis2 items are=> ", item2)