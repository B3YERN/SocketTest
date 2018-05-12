#IMPORTS
import socket
import os
import builtins
import urllib.request

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname(socket.gethostname())
    port = 5050
    ip = urllib.request.urlopen('http://ip.42.pl/raw').read()
    print(str(ip.decode('utf-8')))
    print(str(host))

    s.bind((host,port))

    s.listen()
    print('listening...')
    c,addr = s.accept()
    print('connected to : '+str(addr))

    while True:
        msg = c.recv(1024).decode('utf-8')
        print(str(msg))

if __name__=='__main__':
    main()
    
