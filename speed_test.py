from time import time
def deco(func):
    def speed_test():
        start = time()
        func()
        end = time()
        print(f"the function take: {end - start}")
    return speed_test
@deco
def test():
    for n in range(1, 15000000):
        if n % 2 == 0:
            print(n)

test()