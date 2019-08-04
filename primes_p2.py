import primes_p1 as p1

def ShowAsFactors(n):
    """shows the given number n as a multiplication of its factors"""
    
    f = p1.Decompose(n)
    if len(f) == 1:
        print("{} = {}".format(n, f[0]))
        return
    s = "{} = ".format(n)
    cnt = 1
    for i, f_i in enumerate(f):
        if cnt > 1:
            cnt -= 1
            continue
        cnt = f.count(f_i)
        s += ("{}^{} × ".format(f_i, cnt) if i != len(f)-1 and cnt != len(f)-i else "{}^{}".format(f_i, cnt)) if cnt > 1 else ("{} × ".format(f_i) if i != len(f)-1 else "{}".format(f_i))
    print(s)
    return

def PolyCoefficients(p, c = [1, 1]):
    """calculates coefficients for the expanded polynomials (x-1)^p from 1 to p
    or, if given an array c other than default, from len(c)-1 to p"""
    
    if p == 0:
        return [1]
    p_i = len(c)-1
    while p_i < p:
        a = c
        c = [1, 1]
        for i in range(-1, -len(a), -1):
            c.insert(1, a[i]+a[i-1])
        p_i += 1
    return c

def PolyExpansion(p):
    """shows the expanded polynomials (x-1)^p from 0 to p"""
    
    p_i = 0
    c = [1, 1]
    while p_i <= p:
        s = "(x-1)^{} = ".format(p_i)
        if p_i == 0 or p_i == 1:
            s += "1" if p_i == 0 else "x-1"
        else:
            c = PolyCoefficients(p_i, c)
            for i in range(len(c)):
                if i == 0:
                    s += "x^{}".format(p_i)
                elif i == len(c)-1:
                    s += " + 1" if i%2 == 0 else " - 1"
                else:
                    s += " + " if i%2 == 0 else " - "
                    s += "{}*x^{}".format(c[i], p_i-i) if p_i-i > 1 else "{}*x".format(c[i])
        p_i += 1
        print(s)
    return

def AKSPrimeTest(p, c):
    """returns whether p is prime using AKS theorem:
    *************************************************************************
    p is prime if and only if all coefficients of the polynomial expansion of
                                (x-1)^p-(x^p-1)
    are divisible by p
    *************************************************************************"""
    if p < 2: # both 0 and 1 aren't prime
        return False
    div = lambda x: 1 if x%p == 0 else 0 # checks divisibility
    return all([div(c[i]) for i in range (1, len(c)-1)])

if __name__ == '__main__':
    print('***************************************************************************************')
    print("{:^87}".format("NUMBERS AS MULTIPLICATION OF THEIR FACTORS"))
    for n in range(6550, 6576): # larger numbers to test if it works good
        ShowAsFactors(n)
    print('***************************************************************************************')  
    print("{:^87}".format("POLYNOMIALS"))
    PolyExpansion(9)
    print('***************************************************************************************')
    print("{:^87}".format("FIRST 100 PRIME NUMBERS"))
    primes = []
    for n in range(542):
        c = PolyCoefficients(n) if n <= 1 else PolyCoefficients(n, c)
        if AKSPrimeTest(n, c):
            primes.append(n)
    print(primes)
    print("LENGTH OF THE LIST: {}".format(len(primes)))
    print('***************************************************************************************')
