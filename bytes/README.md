# Bytes and Strings

A confusing subject.

The basics:
- `bytearray` is mutable
- ` bytes` is immutable

```python
>>> b = b"abcdef"
>>> b[0] = 99
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment
>>> c = bytearray(b"abcdef")
>>> c
bytearray(b'abcdef')
>>> c[0]
97
>>> c[0] = 99
>>> c
bytearray(b'cbcdef')
```

```python
>>> v = [0, 32, 64, 96, 128, 160, 192, 224]
>>> type(v)
#<class 'list'>
>>> bytes(v)
#b'\x00 @`\x80\xa0\xc0\xe0'
>>> bytearray(v)
#bytearray(b'\x00 @`\x80\xa0\xc0\xe0')

>>> w = "hello"
>>> type(w)
#<class 'str'>
>>> w.encode()
#b'hello'
>>> list(map(ord,w))
#[104, 101, 108, 108, 111]
>>> bytes(list(map(ord,w)))
#b'hello'

>>> x = b"hello"
>>> type(x)
#<class 'bytes'>
>>> bytearray(x)
#bytearray(b'hello')
>>> bytearray(b'hello')
#bytearray(b'hello')
>>> type(x.decode())
#<class 'str'>
>>> list(x)
#[104, 101, 108, 108, 111]
>>> ''.join(list(map(chr,x)))
#'hello'

>>> y = b"\xff"
>>> type(y)
#<class 'bytes'>
>>> type(y.decode())
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
>>> ''.join(list(map(chr,y)))
#'ÿ'

>>> z = "\xff"
>>> type(z)
#<class 'str'>
>>> z.encode()
#b'\xc3\xbf'
>>> bytes(z)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: string argument without an encoding
>>> bytes(list(map(ord,z)))
#b'\xff'
```
