# def reverse_string(my_string):
#     for ts in range(len(my_string)):
#         yield my_string[-ts]
# for c in reverse_string("Elzero"):
#     print(c, end=" ")


# def deco(func):
#     def result():
#         print("Sugar Added From Decorators")
#         func()
#         print("####################")
#     return result

# @deco
# def make_tea():
#     print("Tea Created")

# @deco
# def make_coffe():
#     print("Coffe Created")

# make_tea()

# make_coffe()