# coding=utf-8


import struct


with open('test.bmp', 'rb') as f:
    if len(f.read()) < 30:
        print('the file is not a BMP.')
    else:
        f.seek(0)
        a = f.read(30)
        b = struct.unpack('<ccIIIIIIHH', a) 
        print(a)
        print(b)
        if b[0] == b'B' and b[1] == b'M':
            print("the pic's size is %d and num of color is %d." % (b[2], b[-1]))
        else:
            print('the file is not a BMP.')