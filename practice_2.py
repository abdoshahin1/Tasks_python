age = int(input("what is your age? "))
if age > 10 and age < 100 :       
      months = age * 12
      weeks = months * 4
      days = weeks * 7
      hours = days * 24
      minutes = hours * 60
      seconds = minutes * 60
      print("you lived for : ")
      print(f"{months:,} Months.\n{weeks:,} Weeks.\n{days:,} Days.\n{hours:,} Hours.\n{minutes:,}"
            f" Minutes.\n{seconds:,} Seconds")
else :
      print('your age is not there in the rang')