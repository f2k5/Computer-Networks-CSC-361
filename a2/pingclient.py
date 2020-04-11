import time
import sys
from socket import *

ping_server_IP_addr  = str(sys.argv[1])
ping_server_port_num = int(sys.argv[2])
server_address = (ping_server_IP_addr, ping_server_port_num)
time_stamp = 0
client_socket = socket(AF_INET, SOCK_DGRAM)
untransmitted_flag = 0
for i in range(1, 101):

	start_time = time.time()
	if i == 1:
		end_time = time.time()
		time_stamp = end_time - start_time
		time_stamp = "{:.20f}".format(time_stamp)

	ping_message = "ping {} {}".format(i, time_stamp)

	client_socket.sendto(ping_message, server_address)
	message, server = client_socket.recvfrom(1024)

	if message[0] == "p":
		untransmitted_flag = 1
		while message[0] == "p":
			start_time = time.time()
			client_socket.sendto(ping_message, server_address)
			message, server = client_socket.recvfrom(1024)
			end_time = time.time()
			time_stamp = end_time - start_time
			time_stamp = "{:.20f}".format(time_stamp)
			print(message)

	elif message[0] == "P":
		if untransmitted_flag == 1:
			start_time = time.time()
			client_socket.sendto(ping_message, server_address)
			message, server = client_socket.recvfrom(1024) 
			end_time = time.time()
			time_stamp = end_time - start_time
			time_stamp = "{:.20f}".format(time_stamp)
			print(message)
		else:
			end_time = time.time()
			time_stamp = end_time - start_time
			time_stamp = "{:.20f}".format(time_stamp)
			print(message)

	print("\n")


