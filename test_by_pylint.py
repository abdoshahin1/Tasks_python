"""
this file to test the pylint
and the first rate is 6.6/10
that is the good rate from first try
"""
def test(name):
    """
    this function used to compare between to string
    the build in string and the name is the parameter
    """
    if name == "ali":
        print("fuck him")
    else:
        print(f"be friend with {name}")

user_input = input("Enter the name: ")
test(user_input)