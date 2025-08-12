# client 
import socket

server_port = 8080
format = 'utf-8'
buffer_for_message_length = 16 

#creat server adrress 
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

address = (host_ip, server_port)

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server
client_socket.connect(address)

# send a message to the server
def message_to_be_sent(message):

    # encode the message
    message = message.encode(format)

    # get the length of the message
    message_length = srt(len(message)) 
    message_length = message_length.encode(format)

    # pad the message length to the buffer size
    padding = b''* (buffer_for_message_length - len(message_length))
    message_length += padding

    # send the message length
    client_socket.send(message_length)

    # send the message
    client_socket.send(message)
    print(client_socket.recv(2048).decode(format))

# main function to run the client
# message = "Hi, this is a message from the client."
# message = 'Disconnect '

while True:
    user_input = input('enter:')
    message_to_be_sent(user_input)
    if user_input() == 'disconnect':
        message_to_be_sent('Disconnect')
        break
    else:
        message_to_be_sent(user_input)