#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('classes.csc.lsu.edu',50113))
serverSocket.listen(5)
print "Listening on http://localhost:50113"
while True:
  #Establish the connection
  print 'Ready to serve...'
  (connectionSocket, addr) = serverSocket.accept()
  try:
    message = "file: indesx.html"
    filename = message.split()[1]
    print filename
    f = open(filename, 'rb')
    outputdata = f.read()
    #Fill in start #Fill in end
    #Send one HTTP header line into socket
    connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n')
    connectionSocket.send("Content-Length: " + str(len(outputdata)) + '\n\n')
    #Send the content of the requested file to the client
    for i in range(0, len(outputdata)):
      connectionSocket.send(outputdata[i])
    connectionSocket.close()
  except IOError:
    print "zomg an error"
    #Send message for file not found
    connectionSocket.send('HTTP/1.1 404 Not Found\n\n')
    #Close client socket
    connectionSocket.close()
