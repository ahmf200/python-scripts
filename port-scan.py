import socket as sk
import time

def scan_port(min_port_range, max_port_range):
    ip = input('Enter the IP to scan: \n')
    start = time.perf_counter()
    for port in range(min_port_range, max_port_range):
        try:
            createdSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
            createdSocket.settimeout(2000)
            createdSocket.connect((ip, port))
            print("{}:OPEN".format(port))
            createdSocket.close
        except: continue
    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 3)}')

def main():
    scan_port(1, 1024)

if __name__ == "__main__":
    main()

