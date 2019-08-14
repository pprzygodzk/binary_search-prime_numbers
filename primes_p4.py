import primes_p1 as p1
import primes_p3 as p3
import time
import itertools as it

def StrongPrimes(n):
    """generates all strong primes up to n, that is primes p(i) which are greater
    than the arithmetic mean of the previous prime and the next one
    ---                         p(i) > p(i-1)+p(i+1)/2                        ---"""
    
    assert isinstance(n, int), "Given argument has to be integer!"
    p = p1.SieveofEratosthenes(n)
    for i in range(1, len(p)-1):
        if p[i] > (p[i-1] + p[i+1])/2:
            yield p[i]
    for q in it.count(p[-1]+1):
        if p3.MillerRabinPT(q):
            if p[-1] > (p[-2] + q)/2:
                yield p[-1]
                break
            else:
                break


def WeakPrimes(n):
    """generates all strong primes up to n, that is primes p(i) which are less
    than the arithmetic mean of the previous prime and the next one
    ---                         p(i) < p(i-1)+p(i+1)/2                        ---"""
    
    assert isinstance(n, int), "Given argument has to be integer!"
    p = p1.SieveofEratosthenes(n)
    for i in range(1, len(p)-1):
        if p[i] < (p[i-1] + p[i+1])/2:
            yield p[i]
    for q in it.count(p[-1]+1):
        if p3.MillerRabinPT(q):
            if p[-1] < (p[-2] + q)/2:
                yield p[-1]
                break
            else:
                break


def GoodPrimes(m):
    """generates good primes up to m, that is primes p(n) whose square are greater
    than the product of any two primes having the same distance i from n
    ---                         p(n)^2 > p(n-i)*p(n+1)                      ---
    for all 1 <= i <= n-1"""
    
    assert isinstance(m, int), "Given argument has to be integer!"
    q = p1.SieveofEratosthenes(m)
    p = p1.PrimesGenerator(2*len(q))
    for n in range(1, len(q)):
        for i in range(1, n+1):
            if p[n]**2 <= p[n-i] * p[n+i]:
                break
        else:
            yield q[n]


def LucasLehmerTest(p):
    """checks if a Mersenne number 2^p-1 is also a prime number
    (important! -> this test works only on odd primes p)"""
    
    assert isinstance(p, int), "Given argument has to be integer!"
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    s = 4
    m = (1 << p)-1
    for i in range(p-2):
        s = ((s*s)-2) % m
    return True if s == 0 else False


def MersennePrimes_AlternativeGen(n):
    """generates all indexes (up to n) of Mersenne primes (2^p-1 where p is also prime)
    (alternative generator)"""
    
    assert isinstance(n, int), "Given argument has to be integer!"
    for p in it.accumulate(it.chain([2, 1, 2], it.cycle([2, 4]))):
        if p > n:
            break
        if p3.MillerRabinPT(p):
            if LucasLehmerTest(p):
                yield "M{}".format(p)


def UlamSpiral(n, m = 1):
    """constructs Ulam spiral of size n x n for primes starting from the given number m"""
    
    assert isinstance(n, int), "Given argument has to be integer!"
    assert n % 2 == 1, "Size of the matrix needs to be odd!"
    
    ulam_spiral = [[0] * n for i in range(n)]
    c1 = c2 = (n - 1) // 2
    ulam_spiral[c1][c2] = m
    distance = 0
    
    for i, path in zip(it.cycle([1, 2]), it.cycle(["right", "up", "left", "down"])):
        if i == 1:
            distance += 1
        if c2 + distance == n and c2 == 0:
            distance = n - 1
        for j in range(distance):
            m += 1
            if path == "right":
                c2 += 1
            elif path == "up":
                c1 -= 1
            elif path == "left":
                c2 -= 1
            elif path == "down":
                c1 += 1
            ulam_spiral[c1][c2] = m
        if c1 == n - 1 and c2 == n - 1:
            break
    
    c1 = c2 = (n - 1) // 2
    for i in range(n):
        s = ""
        for j in range(n):
            if p3.MillerRabinPT(ulam_spiral[i][j]):
                s += "{:^3d}".format(ulam_spiral[i][j])
            else:
                if i != c1 and j != c2 and (i == j or i + j == n-1):
                    s += ("{:^3}".format(" ┌─") if i < c1 else "{:^3}".format("───")) if i == j else ("{:^3}".format("─┐ ") if i < c1 else "{:^3}".format(" └─")) 
                elif (i > j and i + j < n) or (i < j and i + j >= n):
                    s += "{:^3}".format("│") if j != i+1 else "{:^3}".format("─┘ ")
                elif i == c1 and j == c2:
                    s += "{:^3}".format(" •→")
                else:
                    s += "{:^3}".format("───")
        print(s)         
    
    
if __name__ == '__main__':
    print('************************************************************************************')
    print("{:^87}".format("STRONG PRIMES"))
    time_start = time.time()
    sgp_generator = StrongPrimes(600)
    sgp_list = [i for i in sgp_generator]
    time_end = time.time()
    print(sgp_list)
    total = time_end - time_start
    print("NUMBER GENERATING TIME {:0.3f} s".format(total))
    print('************************************************************************************')
    print("{:^87}".format("WEAK PRIMES"))
    time_start = time.time()
    wp_generator = WeakPrimes(601)
    wp_list = [i for i in wp_generator]
    time_end = time.time()
    print(wp_list)
    total = time_end - time_start
    print("NUMBER GENERATING TIME {:0.3f} s".format(total))
    print('************************************************************************************')
    print("{:^87}".format("GOOD PRIMES"))
    time_start = time.time()
    gp_generator = GoodPrimes(1250)
    gp_list = [i for i in gp_generator]
    time_end = time.time()
    print(gp_list)
    total = time_end - time_start
    print("NUMBER GENERATING TIME {:0.3f} s".format(total))
    print('************************************************************************************')
    print("{:^87}".format("MERSENNE PRIMES"))
    time_start = time.time()
    mp_generator = MersennePrimes_AlternativeGen(4500)
    mp_list = [i for i in mp_generator]
    time_end = time.time()
    print(mp_list)
    total = time_end - time_start
    print("NUMBER GENERATING TIME {:0.3f} s".format(total))
    print('************************************************************************************')
    print("{:^87}".format("ULAM SPIRAL"))
    UlamSpiral(27)
    print('************************************************************************************')