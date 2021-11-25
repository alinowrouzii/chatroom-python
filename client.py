from threading import Thread
import socket            
 
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
 
# connect to the server on local computer

# receive data from the server and decoding to get the string.
# print (s.recv(1024).decode())
# close the connection




def handle_printing(socket):
    while True:
        received_msg = socket.recv(1024).decode()
        
        if not received_msg:
            break
        print("received: "+str(received_msg))


port = 12345              
s.connect(('127.0.0.1', port))
print("client connected to server successfully!")

thread = Thread(target = handle_printing, args = (s, ))
thread.start()

while True:
    text = input()
    if text == "-1":
        break
    
    s.send(text.encode())


s.close()