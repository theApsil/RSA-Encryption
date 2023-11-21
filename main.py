from RSA import *

if __name__ == "__main__":
    bit_length = int(input("Enter bit length: "))
    running()
    public, private = generate_keypair(p, q)
    print(f'Public key: [{public}]\nPrivate key: [{private}]')

    msg = input("Write a message to ecnrypt: ") 
    print([ord(c) for c in msg])
    encrypted_msg = encrypt(msg, public)
    print("Encrypted msg: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypted msg: ")
    print(decrypt(encrypted_msg, private))