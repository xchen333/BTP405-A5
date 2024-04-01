import socket
import threading

HOST = '127.0.0.1'
PORT = 65432


def handle_client(conn, addr):
    print(f"New connection from {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f"Message Received from {addr}: {message}")
        if message.lower() == "quit":
            print(f"Closing connection with {addr}")
            conn.close()
            break
        conn.sendall(data)
    conn.close()
    print(f"Connection with {addr} closed")


def run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == "__main__":
    run()
