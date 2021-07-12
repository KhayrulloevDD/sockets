import socket
import threading


HEADER = 64
PORT = 5050
SERVER_IP_ADDRESS = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER_IP_ADDRESS, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = 'DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


def handle_client(connection, address):
    print(f"New connection: {address} connected.")
    connected = True
    while connected:
        message_length = connection.recv(HEADER).decode(FORMAT)
        if message_length:
            message_int = int(message_length)
            message = connection.recv(message_int).decode(FORMAT)
            if message == DISCONNECT_MESSAGE:
                connected = False
                connection.send("You've been disconnected".encode(FORMAT))
            else:
                print(f"{address}: {message}")
                connection.send("Message Received".encode(FORMAT))

    connection.close()


def start():
    print("Server is starting...")
    server.listen()
    print(f"Server is listening on {SERVER_IP_ADDRESS}")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"Active connections: {threading.activeCount() - 1}")


start()
