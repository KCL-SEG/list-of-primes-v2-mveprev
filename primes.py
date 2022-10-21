"""List of prime numbers generator."""

def isPrime(n):
    for i in range(2, n):
        if(n%i==0):
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError()
    list = []
    i = 2
    while len(list) < number_of_primes:
        if(isPrime(i)):
            list.append(i)
        i += 1
    return list
