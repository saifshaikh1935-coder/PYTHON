def GeneratePrime(total):
    primes = []
    number = 2
    while len(primes) < total:
        prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime = False
                break
        if prime:
            primes.append(number)
        number += 1
    return primes

total = int(input("How many prime numbers do you want? "))
print(GeneratePrime(total))
