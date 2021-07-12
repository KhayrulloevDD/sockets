import socket


HEADER = 64
PORT = 5050
SERVER_IP_ADDRESS = '192.168.88.8'
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = 'DISCONNECT'
ADDRESS = (SERVER_IP_ADDRESS, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def send_message(message):
    message = message.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send_message("Салам алейкум!")
send_message(DISCONNECT_MESSAGE)
