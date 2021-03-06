
p = int(input("Select prime number p = "))
q = int(input("Select prime number q = "))

def calc_n(p,q):
    n = p*q
    return n

n = calc_n(p,q)

print "n = ", calc_n(p,q)

e = int(input("Select e = "))

def calc_phi(n,p,q):
    phi = (p-1)*(q-1)
    return phi

phi = calc_phi(n,p,q)

k = int(input("Select integer k = "))

def private_key(n,phi,e,k):
    d = (k*phi + 1)/e
    return d

d = private_key(n,phi,e,k)

print "Public key n = ", calc_n(p,q)
print "Private key d = ", private_key(n,phi,e,k)

# encryption/decryption

plaintext = raw_input("Enter plaintext: ")

def encrypt(e,n,plaintext):
    data = [(ord(char)**e) % n for char in plaintext]
    return data

data = encrypt(e,n,plaintext)

print "Encrypted data = ", encrypt(e,n,plaintext)

def decrypt(data,d,n):
    decrypted_data = [chr((char ** d) % n) for char in data]
    return ''.join(decrypted_data)

text = decrypt(data,d,n)

print "Decrypted data = ", decrypt(data,d,n)
