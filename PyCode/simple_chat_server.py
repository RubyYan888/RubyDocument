# simple_chat_server.py
import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, client_socket, client_address):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address

    def run(self):
        print(f"Connection from {self.client_address}")
        self.client_socket.sendall("Welcome to the chat server!".encode())

        while True:
            message = self.client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Message from {self.client_address}: {message}")
            self.client_socket.sendall(f"Echo: {message}".encode())

        self.client_socket.close()
        print(f"Connection closed from {self.client_address}")

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server started")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = ClientThread(client_socket, client_address)
        client_thread.start()

if __name__ == "__main__":
    start_server('127.0.0.1', 65432)
