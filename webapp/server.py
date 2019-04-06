import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 12345                                           

# bind to the port
s.bind((host, port))                                  
# queue up to 5 requests
s.listen(5)
note = "Thank You for Connecting"
while True:
   print("Trying to connect")
   print("To Send :",note)
   clientsocket,addr = s.accept()     
   print("Got a connection from %s" % str(addr))
   note = clientsocket.recv(1024).decode('ascii')
   print("Note :",note)
   clientsocket.sendall(note.encode('ascii'))
   