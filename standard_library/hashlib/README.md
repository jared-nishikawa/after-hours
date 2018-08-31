# hashlib

It's worth knowing the basics of accessing hash functions in python.

**Example**

```python
import hashlib

print(hashlib.md5("Hello world".encode()).digest())
# b'>%\x96\ny\xdb\xc6\x9bgL\xd4\xecg\xa7,b'

print(hashlib.md5("Hello world".encode()).hexdigest())
# 3e25960a79dbc69b674cd4ec67a72c62
```

Notice that (in python3) we need to `encode()` strings before hashing them.  Python3 makes a strict distinction between strings and byte-strings (python2 was more lax about this).  The output from the `digest()` function is a byte string.

However, the `hexdigest()` function returns a string, with the hash in hex.

Other hash functions of note:

```python
hashlib.sha1
hashlib.sha256
hashlib.sha3_512
```
