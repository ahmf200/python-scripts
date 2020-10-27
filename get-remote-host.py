import socket


def get_remote_machine_info():
    host_address_name = input("Enter the address you want to get the IP of: ")
    try:
        print(f"IP address of {host_address_name}: {socket.gethostbyname(host_address_name)}")
    except socket.error as err_msg:
        print(f"{host_address_name}:{err_msg}")


def get_remote_machine_info_from_file():
    file_to_choose = input("Enter the file you want to use, including the file extension (e.g. file.txt): ")
    try:
        with open(file_to_choose, 'r') as addresses:
            for urls in addresses:
                print(f"\nIP address of {urls}: |-----> {socket.gethostbyname(urls.strip())}\n")
    except socket.error as err_msg:
        print(f"{urls}:{err_msg}")

    
if __name__ == '__main__':
    # get_remote_machine_info()
    get_remote_machine_info_from_file()