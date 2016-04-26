def run_thread(connectionSocket, addr):
    try:
        message = connectionSocket.recv(4096)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send HTTP message over socket
        connectionSocket.send("HTTP/1.0 200 OK\r\n\r\n" + outputdata)
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.0 404 NOT FOUND\r\n\r\n404: File not found")
    except IndexError:
        pass
    #Close client socket
    connectionSocket.close()

#import socket module
from socket import *
import thread
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
serverSocket.bind(("localhost", 80))
serverSocket.listen(5)
serverSocket.settimeout(3)
print 'Ready to serve...'
try:
    while True:
        try:
            #Establish the connection
            (connectionSocket, addr) = serverSocket.accept()
            if connectionSocket == None:
                continue
            #start thread
            thread.start_new_thread(run_thread, (connectionSocket, addr))
        except timeout:
            pass
except KeyboardInterrupt:
    pass
print "Closing down"
serverSocket.close()


