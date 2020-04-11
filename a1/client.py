from socket import *
import sys

clientSocket = socket(AF_INET, SOCK_STREAM)

host_name = str(sys.argv[1])
port_number = int (sys.argv[2])
file_requested = str(sys.argv[3])

clientSocket.connect((host_name, port_number))

#print out the file content you requested:
file_content = "GET /"+file_requested+" HTTP/1.1\r\n\r\n"
clientSocket.send(file_content.encode())

while True:
    response = clientSocket.recv(4096)
    if response == "":
        break
    print response