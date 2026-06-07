import socket


HOST, PORT = '127.0.0.1', 8000


def start_server():
    server = socket.socket(
        socket.AF_INET, # IPv4
        socket.SOCK_STREAM # TCP
    )

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen(5)

    print("Server is running on port 8000...")

    while True:
        client_connection, client_address = server.accept()
        raw_request = client_connection.recv(4096).decode('utf-8')

        #print("raw_request: ", raw_request)
        print(f"--- NEW REQUEST ---")

        body = "Hello World"
        
        http_response = f"HTTP/1.1 200 OK\r\n\r\n{body}"
        
        client_connection.sendall(http_response.encode("utf-8"))
        client_connection.close()
        
    


if __name__ == "__main__":
    start_server()


