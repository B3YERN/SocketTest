#IMPORTS
import socket
import os
import builtins

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname(socket.gethostname())
    print(str(host))

main()
