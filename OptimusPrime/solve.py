from Crypto.Util.number import *
from gmpy2 import *
from pwn import *

pubs = []
enc = 0

# get 1st pub key
conn = remote('206.189.25.173', 32298)
conn.recvuntil(': ')
conn.sendline(b'4')
tmp = conn.recvuntil('proceed: ')
tmp = tmp.decode('utf-8')

tmp = tmp.split('\n')

pubs.append(int(tmp[0].split(' ')[-1]))
enc = int(tmp[1].split(' ')[-1])

# get 2nd pub key
conn.close()
conn = remote('206.189.25.173', 32298)
conn.recvuntil(': ')
conn.sendline(b'4')
tmp = conn.recvuntil('proceed: ')
tmp = tmp.decode('utf-8')

tmp = tmp.split('\n')

pubs.append(int(tmp[0].split(' ')[-1]))
enc = int(tmp[1].split(' ')[-1])


# exploit
p = gcd(pubs[0], pubs[1])
assert(p != 1)
q = pubs[1] // p
e = 65537
d = invert(e, (p-1)*(q-1))
password = pow(enc, d, pubs[1])
conn.sendline(long_to_bytes(password))
print(conn.recvuntil('\n'))
