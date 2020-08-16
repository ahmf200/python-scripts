import socket as sk

ip = input('Enter the IP to scan: \n')

for port in range(1,1024):
    try:
        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        s.settimeout(5000)
        s.connect((ip, port))
        print('%d:OPEN' % (port))
        s.close
    except: continue