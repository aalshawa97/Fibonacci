def fibonacci(num: int):
    # Each number is the sum of the last two
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, num):
        c = a + b
        a = b
        b = c
        print(c)
        # i =  i + i + 1


fibonacci(10)
