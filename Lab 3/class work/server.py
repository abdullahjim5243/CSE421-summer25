# server
import socket

server_port = 8080
format = 'utf-8'
buffer_for_message_length = 16 

#creat server adrress 
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

address = (host_ip, server_port)

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to the address
server_socket.bind(address)
# listen for incoming connections
server_socket.listen()
print('server is listenning')

while True:
    conn,add = server_socket.accept()
    print(f'Connected to {add}')

    connected = True
    while connected:
        # receive the length of the message
        message_length = conn.recv(buffer_for_message_length).decode(format)
        
        print('uocoming message length:', message_length)

    
        if  message_length:
            message_length = int(message_length)
            message = conn.recv(message_length).decode(format)

            if message == 'Disconnect':
                connected = False
                print('Terninating connection with ',add)
                conn.send('The session terminated'.encode(format))
                print('\n')
        else:
            print(message)
            conn.send('the server has recieved the message'.encode(format))
            print('\n')
        
        # convert the length to an integer
        message_length = int(message_length)

        # receive the actual message
        message = conn.recv(message_length).decode(format)

        if not message:
            break

        print(f'Received: {message}')
        
        # echo the message back to the client
        conn.send(message.encode(format))
