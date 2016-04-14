#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
serverSocket.bind(("localhost", 80))
serverSocket.listen(5)
while True:
    #Establish the connection
    print 'Ready to serve...'
    (connectionSocket, addr) = serverSocket.accept()
    try:
        message = connectionSocket.recv(4096)
        print message
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.0 200 OK\r\n\r\n")
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
    except IOError:
        #Send response message for file not found
        print "404"
        connectionSocket.send("HTTP/1.0 404 NOT FOUND\r\n\r\n404: File not found")
    except IndexError:
        pass
    #Close client socket
    connectionSocket.close()
serverSocket.close()

