fib=int(input("Enter a number of the desired fibonacci: "))
a1=0
a2=1
print(a1)
print(a2)
for i in range(1,fib):
    a3=a1+a2
    print(a3)
    a1,a2=a2,a3