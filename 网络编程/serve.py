import socket
from threading import Thread
#开启多线程


#创建套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#绑定ip 端口(传递元组)

s.bind(("127.0.0.1",8000))

#等待连接,设置最大连接数
s.listen(5)

#收数据
def get_mesg(conn,addr):
    while True:# 不停聊天
        recvMsg = conn.recv(1024)  # 接收数据
        recvData = recvMsg.decode("utf8")
        print(addr, "：", recvData)
        if recvData == "q":  # 退出该循环
            print("结束与%s的会话"%addr)
            conn.close()
            break


def send_msg(conn):
    while True:  # 不停聊天
        msg = input("")
        msg = msg.encode("utf-8")
        conn.send(msg)  # 发送数据
        if msg=="q":
            conn.close()
            print("")
            break


while True:
    conn,addr=s.accept()# 不断接受连接
    t1=Thread(target=get_mesg,args=(conn,addr,))
    t2=Thread(target=send_msg,args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
s.close()


class Client():
    def __init__(self, ip, port,n):
        self.ip = ip
        self.port = port
        self.n=n

    def __enter__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.ip, self.port))
        s.listen(self.n)


    def __exit__(self,type, value, trace):
        s.close()


    def send(self,msg):
        msg=msg.encode("utf8")
        s.send(msg)

    def recv(self,msg):
        msg=msg.decode("uft8")
        s.recv(msg)
        print(">>",msg)