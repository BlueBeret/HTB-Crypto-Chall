# import string
# from secret import MSG

# def encryption(msg):
#     ct = []
#     for char in msg:
#         ct.append((123 * char + 18) % 256)
#     return bytes(ct)

# ct = encryption(MSG)
# f = open('./msg.enc','w')
# f.write(ct.hex())
# f.close()


enc = ""
with open('./BabyEncryption/msg.enc', 'r') as f:
    enc = f.read()

enc = bytes.fromhex(enc)

def decrypt(ct):
    msg = []
    for char in ct:
        for i in range(1000):
            if (123* i + 18) % 256 == char:
                msg.append(i)
                break
    return msg

print("".join(chr(x) for x in decrypt(enc)))