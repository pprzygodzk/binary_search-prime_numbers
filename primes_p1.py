import math

def SieveofEratosthenes(n):
    """determine prime numbers from the set of natural numbers from 2 to n"""
    
    a = [i for i in range(2, n+1)]
    for i in a:
        for j in range(i*i, n+1, i):
            if j in a:
                a.remove(j)
            else:
                continue
    return a

def PrimesGenerator(n):
    """generate n prime numbers using trial division (checks if p is divided
    by any number from 2 to √p) and omitting numbers which are multiples of 2 and/or 3
    (except 2 and 3)"""
    
    a = []          # an array of prime numbers
    p = 2           # a potential prime number
    i = 1           # a number of prime numbers in the array a
    k = 1           # only numbers of the form 6*k+1 or 6*k-1 can be prime numbers
                    # numbers of the form 6*k, 6*k+/-2 and 6*k+/-3 are multiples of 2 and/or 3
    r = 1           # a number of repeats of using k
    while i <= n:
        if p == 2 or p == 3:
            a.append(p)
            i += 1
            p = p+1 if p == 2 else p+2
            continue
        for d in range(2, int(math.sqrt(p))+1):
            if p%d == 0:
                break
            if p%d != 0:
                if d == int(math.sqrt(p)):
                    a.append(p)
                    i += 1
                continue
        k = k+1 if p == 6*k+1 else k        # increase k after it has been used twice
                                            # (first is 5 = 6*1-1, second is 7 = 6*1 +1, and so on...)
        r = 1-r                             # changes r to 0 or 1
        p = 6*k+1 if r == 0 else 6*k-1      # gives a value of the next number (we have to use k twice)
    return a

def PrimorialGenerator(n):
    """generate n primorial numbers (the product of the first n successive primes)"""
    
    a = PrimesGenerator(n-1)
    b = [1]
    p = 1
    for i in a:
        p *= i
        b.append(p)
    return b

def CheckPrimarility(n):
    """checks if the given number n is a prime number using trial division"""
    
    assert n >= 2, "The least prime number is 2!"
    if n%2 == 0 and n != 2:
        return "composite"
    for d in range(3, int(n**0.5)+1):       # n**0.5 is faster than sqrt(n) - this is a comment for me, don't bother it
        if n%d == 0:
            return "composite"
        if n%d != 0:
            continue
    return "prime"

def Decompose(n):
    """decompose the given number n into primes (if n is a composite number) or returns
    it unchanged (if n is prime)"""
    
    if n == 1 or CheckPrimarility(n) == "prime":
        return [n]
    
    f = SieveofEratosthenes(math.ceil(n**0.5))        # possible factors
    i = 0
    d = f[0]
    decomposition = []
    while d*d <= n:
        if n%d == 0:
            n //= d
            decomposition.append(d)
        else:
            i += 1
            d = f[i]
    decomposition.append(n)
    return decomposition
    

if __name__ == '__main__':
    print("Prime numbers from the range 2 to 100 generated by Sieve of Eratosthenes:\n{}\n".format(SieveofEratosthenes(100)))
    print("First 25 prime numbers:\n{}\n".format(PrimesGenerator(25)))
    print("First 10 primorial numbers:\n{}\n".format(PrimorialGenerator(10)))
    primorial = PrimorialGenerator(10000)
    print("Length of 10000th primorial number: {}\n".format(len(str(primorial[9999]))))
    print("Is {0} a prime or composite number?: {0} is a {1} number".format(2, CheckPrimarility(2)))        # tests if the algorithm works (doesn't enter the loop for)
    print("Is {0} a prime or composite number?: {0} is a {1} number".format(5, CheckPrimarility(5)))        # as above (enters the loop for)
    print("Is {0} a prime or composite number?: {0} is a {1} number".format(18, CheckPrimarility(18)))      # multiple of 2 (tests if n%2)
    print("Is {0} a prime or composite number?: {0} is a {1} number\n".format(27, CheckPrimarility(27)))    # multiple of 3 (tests loop for)
    print("Prime decomposition of {0} is: {1}".format(12, Decompose(12)))
    print("Prime decomposition of {0} is: {1}".format(5, Decompose(5)))
    print("Prime decomposition of {0} is: {1}".format(2047, Decompose(2047)))
