def factorial(n):
    fact = 1

    for i in range(1,n+1):
        fact = fact*i

    return fact


for n in range(1,11):
    print(n, "!", "=", factorial(n))