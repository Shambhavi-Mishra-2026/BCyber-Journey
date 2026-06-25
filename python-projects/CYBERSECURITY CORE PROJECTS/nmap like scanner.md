import socket
import time


def main():
 
 print("---------------WELCOME---------------")
 ip = input("IP_ADDRESS: ")
 a = int(input("Starting Port: "))
 b = int(input("End Port: "))

 if a < 1 or b > 65535:
    print("Port Range invalid")
    return False

 if a > b:
    print("Port Range invalid")
    return False

 total_port = 0
 open_port = 0

 print("---------------SCANNING START---------------")
 st = time.time()
 for port in range(a,b + 1):
    total_port += 1
    if is_open(ip,port):
        open_port += 1
        service = default_service(port)
        banner = banner_result(ip,port)
        print(f"PORT:{port} - OPEN")
        print(f"SERVICE - {service}")
        print(f"BANNER - {banner}")

 et = time.time()
 print("---------------SCANNING COMPLETE---------------")

 print(f"Total Scanned Port: {total_port}")
 print(f"Open Scanned Port: {open_port}")
 print(f"Total time taken: {et - st}")

def is_open(ip,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        c = s.connect_ex((ip,port))
        s.close()
        return c == 0
    except:
        return False

def default_service(port):
    return service_list.get(port,"Unknown")


def banner_result(ip,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) 
        s.connect((ip,port))
        banner = s.recv(1024).decode(errors = "ignore").strip()
        s.close()
        return banner
    except:
        return ""


service_list = {20: "FTP",
21: "FTP",
22: "SSH",
23: "Telnet",
25: "SMTP",
53: "DNS",
67: "DHCP",
68: "DHCP",
80: "HTTP",
110: "POP3",
143: "IMAP",
443: "HTTPS",
3306: "MySQL",
3389: "RDP",
5432: "PostgreSQL",
8080: "HTTP Alternate"}


main()
