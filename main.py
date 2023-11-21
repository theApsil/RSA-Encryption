from RSA import *
from variables import *
import time


if __name__ == "__main__":
    running()

    command = input('Do you want to chande standart bit_length = 1024? [Y/N]:  ')
    print("Generating public/private keypair...")
    
    while command not in 'YN':
        print('Invalid input')
        command = input("Do you want to chande standart bit_length = 1024? [Y/N]:  ")
    if command == 'Y':
        bit_length = int(input("Enter bit length: "))
    else:
        print('Generating keys using standart bit_length = 1024...')


    p = gen_prime(bit_length)
    q = gen_prime(bit_length)

    public, private = generate_keypair(p, q, bit_length)
    print(f'Public key: [{public}]\nPrivate key: [{private}]')
    

    message = input('Enter message to ecnrypt:  ')
    encrypted_message = encrypt(public, message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(private, encrypted_message)
    print("Decrypted message:", decrypted_message)

    time.sleep(5000)