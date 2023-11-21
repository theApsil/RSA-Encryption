from math import sqrt
import random
from random import randint as rand


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


def gen_keypair(p: int, q: int, keysize: int) -> tuple(int, int):
    