# sockets.py

import socket

def start_server(host='localhost', port=65432):
    """start a simple TCP server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")
        
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")
                    conn.sendall(data)  # echo the received data back

def start_client(host='localhost', port=65432, message='Hello, World!'):
    """starting a simple TCP client."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024)
        print(f"Received from server: {response.decode()}")
