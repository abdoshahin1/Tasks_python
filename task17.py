import datetime
# print(f"days from {datetime.datetime(2021, 6, 25)} to {datetime.datetime(2021, 8, 10)} => {(datetime.datetime(2021, 8, 10) - datetime.datetime(2021, 6, 25)).days}")
test_time = datetime.datetime(2021, 8, 10)
# print(test_time.strftime("%d-%m-%Y"))
# print(test_time.strftime("%b %d, %Y"))
# print(test_time.strftime("%d - %b - %Y"))
# print(test_time.strftime("%d / %b / %y"))
# print(test_time.strftime("%d / %B / %Y"))
print(test_time.strftime("%a, %d %B %Y"))
