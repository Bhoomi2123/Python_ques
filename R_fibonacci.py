def fib(x):
    if(x == 0 or x == 1):
        return x
    fibo = fib(x-1) + fib(x-2)
    return fibo

num = int(input("Enter number : "))

for i in range(num):
    print(fib(i))