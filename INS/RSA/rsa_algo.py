from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_0AEP
import binascii

keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()
print(f"Public key: (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(pubKey.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))


# encryption
msg = "good morning"
encryptor = PKCS1_0AEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print(f"Encripted: {binascii.hexlify(encrypted)}")

