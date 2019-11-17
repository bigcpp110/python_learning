from socket import *
from threading import Thread

def recv():
    while True:
        recv_data= newSocket.recv(1024)
        print('客户端：', recv_data.decode('gbk'))

def send_msg():
    while True:
        msg = input('')
        newSocket.send(msg.encode('gbk'))

# 创建socket
tcpSerSocket = socket(AF_INET, SOCK_STREAM)
# 绑定本地信息
address = (('127.0.0.1', 13000))
tcpSerSocket.bind(address)
tcpSerSocket.listen(128)
newSocket, clientAddr = tcpSerSocket.accept()

thread_rece = Thread(target=recv)
thread_send = Thread(target=send_msg)

thread_rece.start()
thread_send.start()

thread_rece.join()
thread_send.join()

# 关闭这个客户端服务的套接字，只要关闭了，就意味着不能再为这个客户端服务器了，如果还需要服务，只能再次重新连接
newSocket.close()

# 关闭监听套接字，只要这个套接字关闭了，就意味着整个程序不能再接收到任何新的客户端的连接