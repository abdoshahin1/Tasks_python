# def calc(num1, num2, operation="Addition"):
#     if operation == "Addition" or operation == "a" or operation == "A"  or operation == "AdD":
#         return num1 + num2
#     elif  operation == "subTRACT" or operation == "s" or operation == "S":
#         return num1 - num2
#     elif operation == "Multiply" or operation == "m" or operation == "M":
#         return num1 * num2
# print(calc(10, 20)) # 30
# print(calc(10, 20, "AdD")) # 30
# print(calc(10, 20, "a")) # 30
# print(calc(10, 20, "A")) # 30
# print(calc(10, 20, "S")) # -10 
# print(calc(10, 20, "subTRACT")) # -10
# print(calc(10, 20, "Multiply")) # 200
# print(calc(10, 20, "m")) # 200
# def add(*numbers):
#     test =0
#     for number in numbers:
#         if number == 10:
#             continue
#         elif number == 5:
#             test-=5
#             continue
#         test += number
#     return test
# print(add(10, 20, 30, 10, 15)) # 65
# print(add(10, 20, 30, 10, 15, 5, 100)) # 160
# def show_skills(name, *skills):
#     if skills == ():
#         print(f'hello {name} you are not have skills.')
#     else:
#         print(f"hello {name} your skills are: ")
#         for skill in skills:
#             print(f"- {skill}")
# show_skills("Osama", "HTML", "CSS", "JS", "Python")
# def say_hello(name="unknown", age="unknown", country="unknown"):
#     return f"Hello {name} Your Age Is {age} And You Live In {country}"
# print(say_hello())