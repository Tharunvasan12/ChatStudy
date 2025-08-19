import socket

def client_program():
    host = '127.0.0.1'
    port = 8000  

    client_socket = socket.socket()
    client_socket.connect((host, port))

    while True:
        message = input(" -> ")
        client_socket.send(message.encode())

        data = client_socket.recv(1024).decode()
        print('Received from server:', data)

    client_socket.close()

if __name__ == '__main__':
    client_program()
