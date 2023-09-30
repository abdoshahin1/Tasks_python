import re
# assignment one 
# ([A-z]\s)
# my_string = "eeeeE llllLl lllzzZzzzz eroe operationr pollo "
# regex = re.findall(r"([A-z]\s)", my_string)
# print(regex)

# assignment two
# L([A-z]+)
# my_string = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"
# regex = re.findall(r"L([A-z]+)", my_string)
# print(regex)

# assignment three 
# (\+?\(\d{4}\)\s\d+?-\d{4})
# my_string = '''
# +(0100) 600-1234
# +(0100) 60-1234
# (0100) 6000-1234
# 01006001234
# 0100 600 1234
# (0100) 600-1
# (0100) 600-12
# '''
# regex = re.findall(r"(\+?\(\d{4}\)\s\d+?-\d{4})", my_string)
# print(regex)

# assignment four
# (https?://(www\.)?\w+\.(org|com)(:\d{4})?/\w+.(py|php)) or (https?://(www\.)?\w+\.(\w+)(:\d+)?/link(.+))
# my_string = """
# http://www.elzero.org:8888/link.php
# https://elzero.org:8888/link.php
# http://www.elzero.com/link.py
# https://elzero.com/link.py
# http://www.elzero.net
# https://elzero.net
# """
# regex = re.findall(r"(https?://(www\.)?\w+\.(\w+)(:\d+)?/link(.+))", my_string)
# print(regex)

# assignment five
# https? or h\w+ or \wtt\w+ or \w{3}ps? or h.+