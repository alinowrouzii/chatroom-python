from threading import Thread
import socket

# next create a socket object
s = socket.socket()
print("Socket successfully created")


port = 12345

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("", port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")


clients = {}
paired_clients = {}

def handle_client(new_connection, new_addr):
    # receive host address from new connection
    host_address = new_connection.recv(1024).decode()
    
    # print(clients)
    # print(host_address)
    if host_address not in clients.keys(): # host_address not exist in clients dict
        # new_connection.send("shit".encode())
        return
    host_conn = clients[host_address]
    
    
    if host_address not in paired_clients.keys():
        paired_clients[new_addr] = host_address
        paired_clients[host_address] = new_addr
    elif paired_clients[host_address] != new_addr:
        new_connection.send("sorry! the host is busy for now!".encode())
        return
        
    
    while True:
        received_msg = new_connection.recv(1024).decode()

        # send back message to client. just for test
        print("received from client "+ str(received_msg))
        
        
        host_conn.send(f"send to host: {received_msg}".encode())
        



while True:

    # Establish connection with client.
    conn, addr = s.accept()
    
    address = str(addr[1])
    clients[address] = conn
    
    print("Got connection from", address)
    # send a thank you message to the client. encoding to send byte type.
    conn.send(f"Welcome, your address is {address} enter address of your pair".encode())
    
    thread = Thread(target = handle_client, args = (conn,address, ))
    thread.start()


   


s.close()

        