import os
import socket
import threading
import subprocess

def menu():
    
    selector = -1
    while(selector != 0):
        selector = input('Pick a Tool\n1. TCP Client\n2. TCP Server\n3. Replacing Netcat\n0. Exit\n')
        if(selector.isnumeric):
            match selector:
                case '1':
                    tcp_client()
                case '2':
                    tcp_server()
                case '3':
                    args = input('Enter args for netcat')
                    replacing_netcat(args)
                case '0':
                    quit()
        else:
            print("Please enter a valid option")


def tcp_client():
    try:
        target_host = "127.0.0.1" #"my.chc.edu" #socket.gethostbyname(input("Please enter target_host: "))
    except socket.gaierror:
        print("Error resolving host")
        menu()
        exit()
    target_port = 9090 #int(input("Please enter target_port: "))

    # create a socket object
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as err:
        print("socket creation failed %s" %(err))
        menu()
        exit()

    # connect the client
    try:
        client.connect((target_host,target_port))
        print("connected")
    except socket.error as err:
        print('Error: ',err)
        menu()
        exit()
    
    # send some data
    client.send("Hello Server!".encode()) #client.send(input("Enter data to sent: ").encode())
    print("Data Sent")

    # receive some data
    response = client.recv(1024)

    print(response)
    client.close()  

def tcp_server():
    IP = input("Please enter IP: ")
    PORT = int(input("Please enter PORT: "))
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen()
    print(f'[*] Listening on {IP}:{PORT}')
    def handle_client(client_socket):
        with client_socket as sock:
            request = sock.recv(1024)
            print(f'[*] Received: {request.decode()}')
            sock.send('Hello Client'.encode())
    while True:
        try:
            client, address = server.accept()
            print("accepted")
        except KeyboardInterrupt:
            break
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        # client_handler = threading.Thread(target=handle_client, args=(client,))
        # client_handler.start()
        handle_client(client)
        
def replacing_netcat(args):
        os.system(f'python ./Netcat.py {args}')


        
    
if __name__ == '__main__':
    menu()