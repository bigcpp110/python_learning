import socket
from threading import Thread
#创建套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.connect(("127.0.0.1",8000))# 连接服务器

#收数据
def get_mesg(s):
    while True:# 不停聊天
        msg = s.recv(1024)
        msg = msg.decode("utf8")
        print("收到：", msg)

def send_msg(s):
    while True:  # 不停聊天
        sendMsg = input("回复：")
        if sendMsg == "q":  # 退出
            break
        s.send(sendMsg.encode("utf8"))


t2=Thread(target=send_msg,args=(s,))
t1=Thread(target=get_mesg,args=(s,))
t2.start()
t1.start()
t1.join()
t2.join()
s.close()
