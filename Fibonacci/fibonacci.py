# Program to display the Fibonacci sequence

n = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0


if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence :")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1)
        sum = n1 + n2
        n1 = n2
        n2 = sum
        count += 1


def fib():
    n = int(input())
    a = 0
    b = 1
    p = []
    for i in range(n):
        p.append(a)
        a, b = b, a+b
    print(p)


fib()
