password="55555dddd"
input_password=input('write your password: ')
tries=5
while input_password != password:
    tries -=1
    print(f"Wrong password, { 'last' if tries == 0 else tries} chance left")
    input_password=input('write your password: ')
    if tries == 0 and input_password != password:
        print('your tries is finished.')
        break
else:
    print('Correct password.')
    print('Welcome!')