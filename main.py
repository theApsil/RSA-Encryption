from RSA import *
from variables import *


if __name__ == "__main__":
    running()

    command = input('Do you want to chande standart bit_length = 1024? [Y/N]:  ')
    while command not in 'YN':
        print('Invalid input')
        command = input("Do you want to chande standart bit_length = 1024? [Y/N]:  ")
    if command == 'Y':
        bit_length = int(input("Enter bit length: "))
    else:
        print('Generating keys using standart bit_length = 1024')


    p = gen_prime(bit_length)
    q = gen_prime(bit_length)

    public, private = generate_keypair(p, q, bit_length)

    print(f'Public key: [{public}]\nPrivate key: [{private}]')
    # bit_length = int(input("Enter bit length: "))
    # running()
    # public, private = generate_keypair(p, q)
    # print(f'Public key: [{public}]\nPrivate key: [{private}]')

    # msg = input("Write a message to ecnrypt: ") 
    # print([ord(c) for c in msg])
    # encrypted_msg = encrypt(msg, public)
    # print("Encrypted msg: ")
    # print(''.join(map(lambda x: str(x), encrypted_msg)))
    # print("Decrypted msg: ")
    # print(decrypt(encrypted_msg, private))