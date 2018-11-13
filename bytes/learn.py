#!/usr/bin/python3

"""
In which we finally understand how to use Python3 bytes
bytes is immutable
bytearray is mutable
"""

v = [0, 32, 64, 96, 128, 160, 192, 224]
# type(v)
# <class 'list'>
# bytes(v)
# b'\x00 @`\x80\xa0\xc0\xe0'
# bytearray(v)
# bytearray(b'\x00 @`\x80\xa0\xc0\xe0')

w = "hello"
# type(w)
# <class 'str'>
# w.encode()
# b"hello"
# list(map(ord,w))
# [104, 101, 108, 108, 111]
# bytes(list(map(ord,w)))
# b'hello'

x = b"hello"
# type(x)
# <class 'bytes'>
# bytearray(x)
# bytearray(b'hello')
# type(x.decode())
# <class 'str'>
# list(x)
# [104, 101, 108, 108, 111]
# ''.join(list(map(chr,x)))
# 'hello'

y = b"\xff"
# type(y)
# <class 'bytes'>
# type(y.decode())
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 5: invalid start byte
# ''.join(list(map(chr,y)))
# 'ÿ'

z = "\xff"
# type(z)
# <class 'str'>
# z.encode()
# b'\xc3\xbf'
# bytes(z)
# TypeError: string argument without an encoding
# bytes(list(map(ord,z)))
# b'\xff'

