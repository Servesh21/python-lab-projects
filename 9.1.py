import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("StudentsPerformance.csv")

# 1. Number of independent and dependent variables
independent_vars = df.drop(columns=['math score'])  # Treat 'math score' as dependent
dependent_var = 'math score'

print("Columns:", df.columns.tolist())
print(f"Number of independent variables: {independent_vars.shape[1]}")
print("Number of dependent variables: 1 (math score)\n")

# 2. Display top 5 and last 5 rows
print("Top 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())

import hashlib
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.exceptions import InvalidTag
import base64


class EncryptionError(Exception):
    pass


def generate_salt():
    """Generates a random salt for encryption."""
    return os.urandom(16)


def derive_key(password, salt):
    """Derives an encryption key from the password and salt using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256 key size
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


def encrypt(data, password):
    """
    Encrypts the given data using AES-256 with CBC mode.

    Args:
        data (bytes): The data to encrypt.
        password (str): The encryption password.

    Returns:
        bytes: The encrypted data (ciphertext), prepended with the salt and IV.
    """
    salt = generate_salt()
    key = derive_key(password, salt)
    iv = os.urandom(16)  # Initialization Vector
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # PKCS7 padding to ensure data is a multiple of the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    # Prepend the salt and IV to the ciphertext for decryption
    return salt + iv + ciphertext


def decrypt(ciphertext, password):
    """
    Decrypts the given data using AES-256 with CBC mode.

    Args:
        ciphertext (bytes): The encrypted data (ciphertext).
        password (str): The encryption password.

    Returns:
        bytes: The decrypted data (plaintext).
    """
    salt = ciphertext[:16]
    iv = ciphertext[16:32]
    ciphertext = ciphertext[32:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    try:
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()

        # Remove PKCS7 padding
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
        return data
    except Exception as e:
        raise EncryptionError("Decryption failed: {}".format(e))
import hashlib
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


class AESCipher:
    def __init__(self, key):
        # Derive a 256-bit key from the input key using PBKDF2
        salt = os.urandom(16)  # Generate a unique salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # 256 bits
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        self.key = kdf.derive(key.encode())
        self.salt = salt  # Store the salt

    def encrypt(self, data):
        # Generate a random IV
        iv = os.urandom(16)
        # Construct an AES-256-CBC cipher object with the key and IV
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # Pad the data
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data.encode()) + padder.finalize()

        # Encrypt the padded data
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        # Return the IV, salt, and ciphertext
        return base64.b64encode(self.salt + iv + ciphertext)

    def decrypt(self, data):
        # Decode the base64 encoded data
        data = base64.b64decode(data)

        # Extract the salt and IV
        salt = data[:16]
        iv = data[16:32]
        ciphertext = data[32:]

        # Re-derive the key using the stored salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # 256 bits
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(self.key.decode()[:32].encode()) #self.key.encode()) #.decode('utf-8').encode())

        # Construct an AES-256-CBC cipher object with the key and IV
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        # Decrypt the ciphertext
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()

        # Unpad the data
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()

        return data.decode()
import hashlib
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode

def generate_salt():
    """Generates a random salt for encryption."""
    return os.urandom(16)

def derive_key(password, salt):
    """Derives an encryption key from the password and salt using SHA256."""
    derived_key = hashlib.sha256(password.encode() + salt).digest()
    return derived_key

def encrypt(data, password):
    """Encrypts data using AES-256 with a derived key and CBC mode."""
    salt = generate_salt() # Generate a unique salt for this encryption
    key = derive_key(password, salt) # Derive key from password and salt
    iv = os.urandom(16)  # Initialization vector

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Store salt and IV along with ciphertext (separated by delimiters)
    return b64encode(salt + iv + ciphertext).decode('utf-8')

def decrypt(encrypted_data, password):
    """Decrypts data encrypted with AES-256."""
    combined = b64decode(encrypted_data)
    salt = combined[:16]
    iv = combined[16:32]
    ciphertext = combined[32:]

    key = derive_key(password, salt) # Derive key from password and salt

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    return data.decode('utf-8')

# 4. Independent variable with minimum average value (numeric only)
numeric_cols = df.select_dtypes(include=np.number).drop(columns=[dependent_var])
min_avg_col = numeric_cols.mean().idxmin()
print(f"\nIndependent variable with minimum average value: {min_avg_col}")

# 5. Independent variable with highest standard deviation
std_col = numeric_cols.std().idxmax()
print(f"Independent variable with highest std deviation: {std_col}")

# 6. Total count of missing values in each column
missing_vals = independent_vars.isnull().sum()
print("\nMissing values in each independent column:")
print(missing_vals)

# Visualize missing values
plt.figure(figsize=(10, 6))
sns.heatmap(independent_vars.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Identify column with maximum missing values
if missing_vals.sum() > 0:
    max_missing_col = missing_vals.idxmax()
    print(f"Independent variable with max missing values: {max_missing_col}")
else:
    print("✅ No missing values found in any independent variable.")

# 7. Replace missing values in one numeric column with mean
if 'reading score' in df.columns and df['reading score'].isnull().sum() > 0:
    df['reading score'].fillna(df['reading score'].mean(), inplace=True)
    print("Missing values in 'reading score' filled with column mean.\n")
else:
    print("✅ No missing values found in 'reading score'.\n")

# 8. Histogram for one independent variable
plt.figure(figsize=(8, 5))
sns.histplot(df['writing score'], bins=20, kde=True)
plt.title("Histogram: Writing Score")
plt.xlabel("Writing Score")
plt.ylabel("Frequency")
plt.show()

# 9. Boxplot to visualize outliers
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['reading score'])
plt.title("Boxplot: Reading Score")
plt.show()

# 10. Line chart for correlation (e.g., reading score vs writing score)
plt.figure(figsize=(10, 5))
plt.plot(df['reading score'], df['writing score'], 'o-', alpha=0.5)
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.title("Line Chart: Reading vs Writing Score")
plt.show()

# 11. Correlation Matrix
corr_matrix = df.select_dtypes(include=np.number).corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Strongest positive and negative correlations
corr_pairs = corr_matrix.unstack().drop_duplicates()
corr_pairs = corr_pairs[corr_pairs.index.get_level_values(0) != corr_pairs.index.get_level_values(1)]

strong_pos = corr_pairs[corr_pairs < 1].idxmax()
neg_corrs = corr_pairs[corr_pairs < 0]
if not neg_corrs.empty:
    strong_neg = neg_corrs.idxmin()
else:
    strong_neg = None

print(f"\nStrongest positive correlation: {strong_pos}")
if strong_neg:
    print(f"Strongest negative correlation: {strong_neg}")
else:
    print("⚠️ No negative correlation found.")

# 12. Scatter plots for correlation
plt.figure(figsize=(12, 5))

# Positive correlation
plt.subplot(1, 2, 1)
sns.scatterplot(x=df[strong_pos[0]], y=df[strong_pos[1]])
plt.title(f"Positive Correlation: {strong_pos[0]} vs {strong_pos[1]}")

# Negative correlation (if exists)
if strong_neg:
    plt.subplot(1, 2, 2)
    sns.scatterplot(x=df[strong_neg[0]], y=df[strong_neg[1]])
    plt.title(f"Negative Correlation: {strong_neg[0]} vs {strong_neg[1]}")
else:
    plt.subplot(1, 2, 2)
    plt.text(0.5, 0.5, "No negative correlation found", fontsize=14, ha='center')
    plt.axis('off')

plt.tight_layout()
plt.show()
