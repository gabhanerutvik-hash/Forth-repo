import math
n=int(input("Enter a number : "))
sine=math.sin(n)
print(f"sine : {sine}")
if n>=0:
    sr=math.sqrt(n)
    print(f"square root : {sr}")
else:
    print(f"square root is not defined for negative number ")
if n>0:
    log=math.log(n)
    print(f"logarithm : {log}")
else:
    print(f"logarithm are not defined for 0 and negative number ")
