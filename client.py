import socket

HOST = '127.0.0.1'
PORT = 65432


def run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")
        while True:
            message = input("Enter a message (or 'quit' to exit): ")
            client_socket.sendall(message.encode())
            if message.lower() == "quit":
                break
            data = client_socket.recv(1024)
            print(f"Echo from server: {data.decode()}")


if __name__ == "__main__":
    run()
