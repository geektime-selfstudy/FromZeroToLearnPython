def tips(func):
    print(func.__name__)

    def nei(a, b):
        print("start")
        func(4, 5)
        print("end")
    
    return nei


@tips
def add(a, b):
    print(a + b)


@tips
def sub(a, b):
    print(a - b)

add(4, 5)
sub(4, 5)

