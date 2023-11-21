from math import sqrt
from variables import *


def isPrime(n: int) -> bool:
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
    
    return True


def inverse(a: int, m: int) -> int:
    for item in range(1, m):
        if a * item % m == 1:
            return item
    
    return -1


def gcd(a: int, b: int) -> int:
    return a if b == 0 else gcd(a, a % b)


def gen_keypair(p: int, q: int, keysize: int):
    _min = 1 << (keysize - 1)
    _max = (1 << keysize) - 1
    primes = [2]

    start = 1 << (keysize // 2 - 1)
    stop = 1 << (keysize // 2 + 1)

    if start >= stop:
        return []
    
    for i in range(3, stop + 1, 2):
        for nubmer in primes:
            if i % nubmer == 0:
                break
        else:
            primes.append(i)

    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_values = [q for q in primes if _min <= p * q <= _max]
        if q_values:
            q = random.choice(q_values)
            break
    print(p, q)
    n = p * q
    phi = (p - 1) * (q - 1)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    g = gcd(e, phi)

    while True:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
        d = inverse(e, phi)
        if g == 1 and e != d:
            break

    #public key (e,n)
    #private key (d,n)

    return ((e, n), (d, n))