# my_nums = [15, 81, 5, 17, 20, 21, 13]
# my_nums.sort(reverse=True)
# i = 0
# for num in my_nums:
#     if num % 5 == 0:
#         i += 1
#         print(f"{i} => {num}")
# print("all number in list printed")
# i = 0
# while i < 20:
#     i += 1
#     if i < 10:
#         if i == 8 or i == 6:
#             continue
#         print(str(i).zfill(2))
#     else:
#         if i == 12:
#             continue
#         print(i)
# print("all number printed")
# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }
# a, b, c, d, total = 100, 80, 40, 20, 0
# for key, value in my_ranks.items():
#     if value == "A":
#         print(f"my rank in {key} is A and this equal {a} points")
#         total += a
#     elif value == "B":
#         print(f"my rank in {key} is B and this equal {b} points")
#         total += b
#     elif value == "C":
#         print(f"my rank in {key} is C and this equal {c} points")
#         total += c
# print(f'total point are {total}')
# first way to solve the task
# # a, b, c, d, total = 100, 80, 40, 20, 0
# # for key in students:
# #     print('-' * 30)
# #     print(f"-- student name => {key}")
# #     print('-' * 30)
# #     for ky in students[key]:
# #       if students[key][ky]== "A":
# #           print(f"- {ky} => {a} points")
# #           total += a
# #       elif students[key][ky]== "B":
# #           print(f"- {ky} => {b} points")
# #           total += b
# #       elif students[key][ky]== "C":
# #           print(f"- {ky} => {c} points")
# #           total += c
# #       elif students[key][ky]== "D":
# #           print(f"- {ky} => {d} points")
# #           total += d
# #     print(f"total point is {total}")
# #     total=0
# # print('-' * 30)
# students = {
#   "Ahmed": {
#     "Math": "A",
#     "Science": "D",
#     "Draw": "B",
#     "Sports": "C",
#     "Thinking": "A"
#   },
#   "Sayed": {
#     "Math": "B",
#     "Science": "B",
#     "Draw": "B",
#     "Sports": "D",
#     "Thinking": "A"
#   },
#   "Mahmoud": {
#     "Math": "D",
#     "Science": "A",
#     "Draw": "A",
#     "Sports": "B",
#     "Thinking": "B"
#   }
# }
# a, b, c, d, total = 100, 80, 40, 20, 0
# for key, value in students.items():
#     print('-' * 30)
#     print(f"-- student name => {key}")
#     print('-' * 30)
#     for ky, vl in value.items():
#         if vl == "A":
#             print(f"- {ky} => {a} points")
#             total += a
#         elif vl == "B":
#             print(f"- {ky} => {b} points")
#             total += b
#         elif vl == "C":
#             print(f"- {ky} => {c} points")
#             total += c
#         elif vl == "D":
#             print(f"- {ky} => {d} points")
#             total += d
#     print(f"total point is {total}")
#     total=0
# print('-' * 30)