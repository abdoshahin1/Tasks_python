#decoration 
def deco(ts):
    def test(tst):
        test1 = tst
        return test1.strip().capitalize()
    return test

@deco
def name(user_input):
    return user_input

name_input = input("what is your name: ")
print(f"your name after decoration is : {name(name_input)}")