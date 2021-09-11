from Crypto import Cipher
from Crypto.Cipher import DES
from secrets import token_bytes

key= token_bytes(8)

def encrypt (msg) :
    Cipher=DES.new(key,DES.MODE_EAX)
    nonce=Cipher.nonce
    chiphertext, tag =Cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce,chiphertext,tag

def decrypt(nonce,ciphertext,tag):
    Cipher=DES.new(key,DES.MODE_EAX,nonce=nonce)
    plaintext=Cipher.decrypt(ciphertext)

    try:
        Cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

nonce,ciphertext,tag=encrypt(input("Enter Plaintext: "))
print("Cipher text:", ciphertext)
plaintext=decrypt(nonce,ciphertext,tag)
if not plaintext:
    print("Message is corrupted")
else:
    print("Decrypted PlainText: ",plaintext)
