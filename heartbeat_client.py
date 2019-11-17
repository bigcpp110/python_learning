#coding:utf8
import argparse
import socket
import time

def client(host,port,delay):
    udp_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        try:
            udp_sock.connect((host,port))
            #udp_sock.sendto('2333',address=(host,port))
            udp_sock.send('2333'.encode('ascii'))
        except:
            pass
        finally:
            time.sleep(delay)


def main():
    parse = argparse.ArgumentParser(description="Sent a message to a host")
    parse.add_argument('-H',nargs='?',default='127.0.0.1',const='127.0.0.1')
    parse.add_argument('-P',nargs='?',default=2333,const=2333,type=int)
    parse.add_argument('-D',nargs='?',default=1,const=1)
    result = parse.parse_args()
    print(result.H,result.P,result.D)
    client(result.H,result.P,result.D)


if __name__=='__main__':
    main()