from RSA import *
from variables import *

if __name__ == "__main__":
    bit_length = int(input("Enter bit length: "))
    running()
    public, private = gen_keypair(p, q, 2 ** bit_length)
    print(f'Public key: [{public}]\nPrivate key: [{private}]')
    