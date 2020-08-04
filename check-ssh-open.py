import socket
import os

def checkPortOpenClosed():
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip_address = "127.0.0.1"
    ssh_port_number = 22

    error_indicator = a_socket.connect_ex((ip_address, ssh_port_number))
    # connect_ex returns an error indicator
    # e.g. 61 means ECONNREFUSED -> https://www.microfocus.com/documentation/enterprise-developer/ed40pu1/ED-VS2017/GUID-1872DF9A-0FE4-4093-9A1B-B743BFDDDBA1.html

    if error_indicator == 0:
        print("\n [--] %s: Port %s is open\n" % (os.strerror(error_indicator), ssh_port_number))
    else:
        print("\n [--] %s: Port %s is not open\n" % (os.strerror(error_indicator), ssh_port_number))
    # os.strerror converts error code into the corresponding message

    a_socket.close()

if __name__ == "__main__":
    checkPortOpenClosed()
