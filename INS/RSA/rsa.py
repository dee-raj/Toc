import random
def is_prime(number):
   if number <=1:
      return False
   if number <= 3:
      return True
   if number % 2 == 0 or number % 3 == 0:
      return False
   i=5
   while i*i <= number:
      if number % i == 0 or number % (i + 2) ==0:
         return False
      i += 6
   return True
def generate_prime(bits):
   while True:
      num = random.getrandbits(bits)
      if is_prime(num):
         return num
def gcd(a,b):
   while b:
      a, b = b, a % b
   return a

def mod_inverse(a, m):
   m0, x0, x1 = m, 0, 1
   while a > 1:
      q = a//m
      m, a = a % m, m
      x0, x1 = x1 - q*x0, x0
   return x1 if x1 > 0 else x1 + m0

def generate_keypair(bits):
   p = generate_prime(bits)
   q = generate_prime(bits)
   n = p * q
   phi = (p-1)*(q-1)
   while True:
      e = random.randrange(2, phi)
      if gcd(e, phi) == 1:
         break
   d = mod_inverse(e, phi)
   return ((e, n), (d, n))

def encrypt(message, public_key):
   e, n = public_key
   encrypted = [pow(ord(char), e, n) for char in message]
   return encrypted

def decrypt(encryptedMgs, private_key):
   d, n = private_key
   decrypted = [chr(pow(ord(char), d, n)) for char in encryptedMgs]
   return ''.join(decrypted)

if __name__ == "__main__":
   bits = 10
   public_key, private_key = generate_keypair(bits)

   message = "hello RSA encryption"
   encryped_msg = encrypt(message, public_key)
   decryped_msg = decrypt(message, private_key)
