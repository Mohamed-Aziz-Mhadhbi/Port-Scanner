import socket, threading, concurrent.futures, colorama, time, os
from colorama import fore

colorama.init()

print_lock = threading.Lock()

os.system('cls')

ip = input('Enter IP/URL To Scan: ')

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.LIGHTMAGENTA_EX + f'[{port}]' + Fore.GREEN + 'Open')
