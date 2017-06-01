# coding=utf-8


import base64


# s = b'6Iuf5Yip5Zu95a6255Sf5q275Lul77yM5bKC5Zug56W456aP6YG/6LaL5LmL44CC'


# def safe_base64_decode(s):
#     a = base64.b64decode(s)
#     b = a.decode('utf-8')
#     print(b)


# if __name__ == "__main__":
#     safe_base64_decode(s)
#     print(base64.b64decode(b'5Zev77yM5aW95rm/5aW95rm/fg==').decode('utf-8'))
    
def safe_base64_decode(s):
    if len(s) % 4 == 0:
        return base64.urlsafe_b64decode(s)
    else:
        return safe_base64_decode(s+b'=')