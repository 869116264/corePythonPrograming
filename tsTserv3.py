from socket import *
from time import ctime

HOST=''
PORT=18888
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('wating for connect')
    tcpCliSock,addr=tcpSerSock.accept()
    print("connect from",addr)
    while True:
        data=tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' %(bytes(ctime(),'utf-8'),data).encode())

    tcpCliSock.close()

tcpSerSock.close()
