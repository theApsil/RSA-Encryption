import math as m
from variables import *
import random


def inverse(a: int, m: int) -> int:
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def gcd(a: int, b: int) -> int:
    return a if b == 0 else m.gcd(a, a % b)


# def generate_prime(bit_length):
#     candidate = random.getrandbits(bit_length)
#     while not isPrime(candidate):
#         candidate = random.getrandbits(bit_length)
#     return candidate


def generate_keypair(p, q, bit_length):

    p = gen_prime(bit_length)
    q = gen_prime(bit_length)

    n = p * q
    phi = (p-1) * (q-1)

    # Выбираем открытый ключ e, такой что 1 < e < phi и e взаимно прост с phi
    e = random.randrange(2, phi)
    while m.gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Вычисляем закрытый ключ d, такой что d * e ≡ 1 (mod phi)
    d = inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext



def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)


def running():
    print("RSA is running...")
    print("Generating public/private keypair...")