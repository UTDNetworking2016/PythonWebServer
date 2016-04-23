import socket, sys

address = sys.argv[1]
portnum = sys.argv[2]
filename = sys.argv[3]
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((address, int(portnum)))
soc.send("GET /" + filename +" HTTP1.1\r\n\r\n")
msg = soc.recv(2048)
print msg
