# codint=utf-8
# 服务器编程


import socket, time, threading


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定监听的地址和端口
s.bind(('127.0.0.1', 9999))

# 监听端口
s.listen()
print('Waiting for connection...')

while True:
    # 接受一个新的连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

