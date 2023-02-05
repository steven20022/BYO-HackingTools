import socket
import threading
import subprocess

def menu():
    selector = -1
    while(selector != 0):
        selector = input('Pick a Tool\n1. TCP Client Creator\n2. TCP Server\n0. Exit\n')
        if(selector.isnumeric):
            match selector:
                case '1':
                    tcp_client()
                case '2':
                    tcp_server()
                case '0':
                    quit()
        else:
            print("Please enter a valid option")


def tcp_client():
    target_host = input("Please enter target_host: ")
    target_port = int(input("Please enter target_port: "))

    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    client.connect((target_host, target_port))

    # send some data
    client.send(input("Enter data to sent: ").encode())

    # receive some data
    response = client.recv(100)

    print("Server Response: \n",response.decode())
    client.close()

def tcp_server():
    IP = '0.0.0.0'
    PORT = 9998
    
if __name__ == '__main__':
    menu()