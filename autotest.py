import unittest
from RSA import *


class TestRSA(unittest.TestCase):

    def test_encrypt_decrypt(self):
        p = gen_prime(bit_length)
        q = gen_prime(bit_length)
        public_key, private_key = generate_keypair(p, q, bit_length)

        messages = ["Hello, RSA!", "Testing encryption.", "12345", "!@#$%^&*()"]

        for message in messages:
            encrypted_message = encrypt(public_key, message)
            decrypted_message = decrypt(private_key, encrypted_message)

            self.assertEqual(message, decrypted_message, f"Failed for message: {message}")

    def test_invalid_key(self):
        # Test with an invalid key
        invalid_key = (123, "invalid")
        message = "Invalid key test"

        with self.assertRaises(ValueError):
            encrypt(invalid_key, message)

    def test_invalid_message(self):
        # Test with an invalid message
        p = gen_prime(bit_length)
        q = gen_prime(bit_length)
        public_key, private_key = generate_keypair(p, q, bit_length)

        invalid_messages = [123, ["not", "a", "string"], {"key": "value"}]

        for invalid_message in invalid_messages:
            with self.assertRaises(ValueError):
                encrypt(public_key, invalid_message)

if __name__ == "__main__":
    unittest.main()