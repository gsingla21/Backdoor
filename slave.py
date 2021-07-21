import os
import socket
s=socket.socket()
host="192.168.1.71"
port=4444
#host=input(str("Enter server address: "))
s.connect((host,port))
print("")
print("Connection Successful")
print("")
while(1):
        command=s.recv(1024)
        command=command.decode()
        print("Command received")
        print("")
        if command is "cwd":
                files=os.getcwd()
                files=str(files)
                s.send(files.encode())
                print("Command Executed Successfully")
        else:
                print("")
                print("Command not recognised")
                exit(0)
                
