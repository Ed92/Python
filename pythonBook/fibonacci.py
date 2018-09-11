def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

fib = fibonacci()
fib2 = fib.__next__()
fib3 = fib.__next__()
print(fib2)
print(fib3)
fib3 = [fib.__next__() for i in range(10)]
print(fib3)
