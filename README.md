# Concurrent Echo Server with Python


This project implements a concurrent echo server using Python. The server can handle multiple client connections simultaneously, echoing back any messages it receives from the clients, with clear indications of which client they are from.

## Requirements
- Python 3

## Usage

### Server
1. Run the server script:
```
python server.py
```
2. The server will start listening on `localhost` (127.0.0.1) and the port specified in the code (default: 65432).
3. You can modify the `HOST` and `PORT` variables in the server code to change the listening address and port.

### Client
1. Run the client script:
```
python client.py
```
2. The client will connect to the server using the specified `HOST` and `PORT`.
3. Enter a message and press Enter to send it to the server.
4. The server will echo back the message, and the client will display it.
5. To exit the client, enter "quit" (case-insensitive).