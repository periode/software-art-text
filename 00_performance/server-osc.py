import socket

ip = "127.0.0.1"
port = 2046 #wkw

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send(w):
    message = w
    sock.sendto(message.encode('utf-8'), (ip, port))

send("hello")
