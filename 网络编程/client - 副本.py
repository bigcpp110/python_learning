from socket import *
from threading import Thread

def recv():
    while True:
        data_recv = tcp_socket_client.recv(1024)
        print('服务端：', data_recv.decode('gbk'))

def send_msg():
    while True:
        msg = input('')
        tcp_socket_client.send(msg.encode('gbk'))


# 1、创建套接字
tcp_socket_client = socket(AF_INET,SOCK_STREAM)
# 2、创建链接
dest_ip = input('请输入服务端ip:')
dest_port = int(input('请输入服务端端口:'))
tcp_socket_client.connect((dest_ip,dest_port))

thread_rece = Thread(target=recv)
thread_send = Thread(target=send_msg)

thread_rece.start()
thread_send.start()

thread_rece.join()
thread_send.join()
# 4、关闭
tcp_socket_client.close()