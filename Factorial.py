n=int(input("Enter a number: "))
def fun(num):
    factorial=1
    while num > 1:
        factorial=factorial*num
        num=num-1
    return factorial
print(f"Factorial of {n} is {fun(n)}")
