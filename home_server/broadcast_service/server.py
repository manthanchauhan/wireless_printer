import socket
import threading
import time

HOST = "192.168.0.13"
PORT = 9999
available_clients = []


def _start_server_socket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            server_socket.bind((HOST, PORT))
        except OSError:
            return

        server_socket.listen(5)
        print("Listening...")

        while True:
            if len(available_clients) >= 10:
                continue

            client_socket, client_ip = server_socket.accept()
            available_clients.append((client_socket, client_ip))
            print(available_clients)


def start_server_socket():
    """
    Starts listening at server socket
    :return:
    """
    threading.Thread(target=_start_server_socket).start()

    return


def broadcast_message(msg="Hello Word"):
    for client_socket, client_ip in available_clients:
        client_socket.send(bytes(msg, "utf-8"))
