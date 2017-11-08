from Crypto.Cipher import AES
import base64
import json
import os
import binascii
import rsa

modulus = ('00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7'
           'b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280'
           '104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932'
           '575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b'
           '3ece0462db0a22b8e7')
nonce = '0CoJUm6Qyw8W8jud'
pubKey = '010001'


def encrypted_request(text):
    text = json.dumps(text)
    secKey = createSecretKey(16)
    encText = aesEncrypt(aesEncrypt(text, nonce), secKey)
    encSecKey = rsaEncrypt(secKey, pubKey, modulus)
    data = {'params': encText, 'encSecKey': encSecKey}
    return data


def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + chr(pad) * pad
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext).decode('utf-8')
    return ciphertext


def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = pow(int(binascii.hexlify(text), 16), int(pubKey, 16), int(modulus, 16))
    return format(rs, 'x').zfill(256)


def createSecretKey(size):
    return binascii.hexlify(os.urandom(size))[:16]


'''uid = '248958316'
limit = 10
csrf = '85b920478294103ed9b3cc4f515fa599'
req = {
                "uid":'248958316',"type":0,"limit":1000,"offset":0,"total":True
            }

my_data = encrypted_request(str(req))
params = my_data.get('params')
encSecKey = my_data.get('encSecKey')

print(params)
print(encSecKey)'''

# PRIVATEKEY = open('rsa_private_key.pem', 'r').read().strip('\n')

# def rsa_decrypt(rsa_str):
# return rsa.decrypt(base64.b64decode(rsa_str), rsa.PrivateKey.load_pkcs1(PRIVATEKEY))
# encSecKey = rsa_decrypt(encSecKey)
'''
print(len(encSecKey))
def aesDecrypt(text, secKey):
    ciphertext = base64.b64decode(text)
    encryptor = AES.new(secKey, 2, '0102030405060708')
    text = encryptor.decrypt(ciphertext)
    for i in range(0, 17):
        if str(i * chr(i)) in text:
            text = text.replace(str(i * chr(i)), "")
    return text

print(aesDecrypt(aesDecrypt(params, encSecKey), nonce))'''
