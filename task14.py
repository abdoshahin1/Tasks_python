# values = (0, 1, 2)

# if any(values):
#     my_var = 0

# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
#     print("Good")
# # Good
# else:
# #     print("Bad")
# v = 40

# my_range = list(range(v))

# print(sum(my_range, v) + pow(v, v, v))  # 820
# n = 21

# l = list(range(n))

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

#   print("Good")

# # Output => Good



# my_all
# def my_all(mylist):
#     check = 0
#     for test in mylist:
#         if test:
#             check +=1
#     if len(mylist) == check:
#         return True
#     else:
#         return False

# print(my_all([1, 2, 3, []])) # False

# my_any
# def my_any(test):
#     check = len(test)
#     for te in test:
#         if te:
#             check -=1
#         else:
#             continue
#     if  check == len(test):
#         return False
#     elif  check >= 0:
#         return True

# print(my_any([0, 1, [], False])) # True
# print(my_any([(), 0, False,1])) # true



# my_min
# def my_min(test):
#     check = 0
#     for i in test:
#         if check > i:
#             check = i
#     return check

# print(my_min([10, 100, -20, -100, 50, -200])) # -200
# print(my_min((10, 100, -20, -100, 50, -200))) # -200

# my_max 
# def my_max(test):
#     check = 0
#     for i in test:
#         if check < i:
#             check = i
#     return check

# print(my_max([10, 100, -20, -100, 50, 700])) # 700
# print(my_max((10, 100, -20, -100, 50, 700))) # 700