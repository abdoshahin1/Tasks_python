# this excepration use to detect the mobile number => \s\d{4}\s?\d{3}\s?\d{4}\s
# this excepration use to detect the email => [A-z0-9]+(.?-?)[A-z0-9]+(.?-?)[A-z0-9]+@[A-z]+.[A-z]+ other one [A-z0-9\.\-]+@[A-z0-9]+\.\w+
import re
# findall()=> return match or empty list
# split(regex, string, maxsplit)
# sub(regex, replace, string, countreplace)
# print(dir(re))

# test one:
user_input = input("what is your email: ")
my_search = re.search(r"\s\d{4}\s?\d{3}\s?\d{4}\s", user_input)
print(my_search)
# print(my_search.span())
# print(my_search.string())
# print(my_search.group())

# test two:
# valid_mail = []
# user_input = input('Enter your Email: ')
# Detect_correct = re.findall("[A-z0-9\.\-]+@[A-z0-9]+\.\w+", user_input)
# if Detect_correct != []:
#     print("Valid email.")
#     valid_mail.append(Detect_correct)
# else:
#     print('invalid email.')
# if valid_mail != []:
#     for email in valid_mail:
#         print(email)
# else:
#     print('the list is empty.')

# test there:
