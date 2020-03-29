from cryptography.fernet import Fernet
import ujson as json
import base64
import time

# Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)

def encode():
    d = {'test': [1,2,3]}
    token = f.encrypt(json.dumps(d).encode('utf-8'))
    return base64.b64encode(token)

def decode(s):
    z = f.decrypt(base64.b64decode(s))
    k = z.decode('utf-8')
    return json.loads(k)

m = encode()

st = time.time()
for _ in range(200000):
    decode(m)

print('time: {}'.format(time.time() - st))
