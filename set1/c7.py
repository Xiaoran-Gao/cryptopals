from base64 import b64decode, b64encode
from Crypto.Cipher import AES

if __name__ == "__main__":
    key = b"YELLOW SUBMARINE"
    b64_text = open('./set1/input/7.txt', 'r').read()
    text = b64decode(b64_text)
    cipher = AES.new(key, AES.MODE_ECB)
    print(cipher.decrypt(text).decode('utf-8'))