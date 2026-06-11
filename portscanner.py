# Simple beginner port scanner that scans all ports from X to Y and checks if they are open or closed. 

import socket
import threading


target = input(f"Enter Target IP: ")
start_port = int(input(f"Enter Starting Port: "))
end_port = int(input(f"Enter Ending Port: "))

print (f"Scanning {target} from port {start_port} to {end_port}: ")

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
        s.settimeout(1.5)
        try:
            banner =s.recv(1024)
            if banner:
                print(f"Banner: {banner.decode('UTF-8', errors = 'ignore')}")
        except Exception as e:
            print(f"port {port} - no banner: {e}")
    s.close()


threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(target, port))
    t.start()
    threads.append(t)
    
    for t in threads:
        t.join()    
        
print(f"Scan Complete for {target} from port {start_port} to {end_port}.")