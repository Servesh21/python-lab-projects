n = int(input("Enter number of integers in the list: "))
num = []
print("Enter integers in the list:")
for i in range(n):
    num.append(int(input()))

print("Entered list is:", num)

import hashlib
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

def encrypt(key, source):
    """
    Encrypts the input source string using AES-256 encryption.
    """
    # Generate a random salt
    salt = os.urandom(16)
    # Derive a key using PBKDF2
    key = derive_key(key, salt)
    key = base64.urlsafe_b64encode(key)
    key = hashlib.sha256(key).digest()
    # Generate a random initialization vector
    iv = os.urandom(16)
    # Pad the source string to be a multiple of the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(source.encode('utf-8')) + padder.finalize()
    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CFB8(iv), backend=default_backend()) #Using CFB8 as a replacement to the DES CBC mode
    encryptor = cipher.encryptor()
    # Encrypt the padded data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    # Return the salt, IV, and ciphertext
    return base64.b64encode(salt + iv + ciphertext).decode('utf-8')


def decrypt(key, source):
    """
    Decrypts the input source string using AES-256 decryption.
    """
    # Decode the base64 encoded source
    enc = base64.b64decode(source)
    # Extract the salt, IV, and ciphertext from the encoded source
    salt = enc[:16]
    iv = enc[16:32]
    ciphertext = enc[32:]
    # Derive the key using PBKDF2
    key = derive_key(key, salt)
    key = base64.urlsafe_b64encode(key)
    key = hashlib.sha256(key).digest()

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CFB8(iv), backend=default_backend()) #Using CFB8 as a replacement to the DES CBC mode
    decryptor = cipher.decryptor()
    # Decrypt the ciphertext
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    # Unpad the decrypted data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    # Return the decrypted string
    return data.decode('utf-8')

def derive_key(password, salt):
    """
    Derives a key from the password and salt using PBKDF2.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode('utf-8'))

l = len(num)

for i in range(l):
    for j in range(i + 1, l):
        if (choice == 1 and num[i] > num[j]) or (choice == 2 and num[i] < num[j]):
            num[i], num[j] = num[j], num[i]

if choice == 1:
    print("List sorted in ascending order:", num)
elif choice == 2:
import hashlib
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

def encrypt(key, source):
    """
    Encrypts the source string using AES-256 encryption.
    """
    key = base64.b64decode(key)
    iv = os.urandom(16)  # Generate a fresh IV for each encryption
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(source.encode('utf-8')) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CFB8(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    # Return IV + Ciphertext
    return base64.b64encode(iv + ciphertext).decode('utf-8')

def decrypt(key, source):
    """
    Decrypts the source string using AES-256 encryption.
    """
    key = base64.b64decode(key)
    source = base64.b64decode(source.encode('utf-8'))
    iv = source[:16]
    ciphertext = source[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB8(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    unpadded_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(unpadded_data) + unpadder.finalize()
    return plaintext.decode('utf-8')

def generate_key(password, salt=None):
    """
    Generates a secure AES-256 key using PBKDF2.
    """
    if salt is None:
        salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode('utf-8'))
    return base64.b64encode(key).decode('utf-8'), base64.b64encode(salt).decode('utf-8')

def verify_key(password, key, salt):
    """
    Verifies a password against a stored key and salt.
    """
    key = base64.b64decode(key)
    salt = base64.b64decode(salt)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    try:
        kdf.verify(password.encode('utf-8'), key)
        return True
    except Exception:  #Catch exceptions like InvalidKey
        return False
else:
    print("Invalid choice! Please enter 1 or 2.")
