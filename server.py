# import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
serverSocket.bind(('localhost',50113))
serverSocket.listen(5)
print 'Listening on http://localhost:50113'
print 'Ready to serve...'
while True:
  # Establish connection
  (connectionSocket, addr) = serverSocket.accept()
  try:
    message = 'file: index.html'
    filename = message.split()[1]
    print 'Opening file "' + filename + '" to serve'
    f = open(filename, 'rb')
    outputdata = f.read()
    # Send HTTP header
    connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n')
    connectionSocket.send('Content-Length: ' + str(len(outputdata)) + '\n\n')
    for i in range(0, len(outputdata)):
      connectionSocket.send(outputdata[i]) # So much datas!
    connectionSocket.close()
    print 'Sucessfully served file "' + filename + '", connection closed'
  except IOError:
    # Couldn't open file, send 404 & close connection
    errorMessage = '404: File "' + filename + '" not found\n\n'
    print errorMessage
    connectionSocket.send(errorMessage)
    connectionSocket.close()
