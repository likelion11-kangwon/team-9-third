import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad


def hash(value: bytes):
    h = hashlib.sha256()
    h.update(value)
    result = bytes.fromhex(h.hexdigest())
    return result


def encrypt(b: bytes, password: bytes):
    cipher = AES.new(password, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(b, 16)) 
    return encrypted

def decrypt(b: bytes, password: bytes):
    cipher = AES.new(password, AES.MODE_ECB)
    decrypted = cipher.decrypt(b)
    return unpad(decrypted, 16)
