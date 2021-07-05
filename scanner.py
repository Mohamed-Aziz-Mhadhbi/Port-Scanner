import socket, threading, concurrent.futures, colorama, time, os
from colorama import Fore

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
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1000): # Scans through 1k ports
        executor.submit(scan, ip, port + 1)

print(Fore.LIGHTMAGENTA_EX + f' Done Scanning {ip}')
time.sleep(5000)