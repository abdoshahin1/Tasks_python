# # def remove_chars(text):
# #     return text[1:len(text) - 1]
# #
# #
# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
# # cleaned_list = list(map(remove_chars, friends_map))
#
# for i in map(lambda text: text[1:len(text) - 1], friends_map):
#     print(i)

# def get_names(text):
#     return text.endswith("m")
#
#
# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
# # names = filter(get_names, friends_filter)
#
# for i in filter(lambda text: text.endswith("m"), friends_filter):
#     print(i)
#

# from functools import reduce
# nums = [2, 4, 6, 2]
#
# result = reduce(lambda num, num1: num * num1, nums)
# print(result)

# way one
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
# for i, c in enumerate(reversed(skills), 50):
#     if type(c) == int:
#         continue
#     print(f"{i} - {c}")

# second way
# test = list(skills)
# test.reverse()
# count = 50
# for i in test:
#     if type(i) == int:
#         count += 1
#         continue
#     print(f"{count} - {i}")
#     count += 1
